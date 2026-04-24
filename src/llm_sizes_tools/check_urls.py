"""Check a batch of URLs for HTTP reachability.

Used by the researcher for pre-commit sanity on the URLs it cited, and by
the orchestrator when a verifier reports mass fetch failures — this tool
confirms whether the failures are real (bad slugs / typos) or just a
Cloudflare bot-block on the verifier's WebFetch user agent.

Emits one aligned `STATUS  URL [-> FINAL]` line per URL. Exit code 0 iff
every URL returned a 2xx/3xx final status; exit 1 otherwise.

Examples
--------
$ uv run check-urls https://openai.com/index/hello-gpt-4o/ https://example.com/nope
200  https://openai.com/index/hello-gpt-4o/
404  https://example.com/nope

$ uv run check-urls --from-csv --field release_url,supporting_url 52-60
200  https://openai.com/index/language-unsupervised/
...
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from pathlib import Path

DEFAULT_CSV = Path(__file__).resolve().parents[2] / "llm_sizes.csv"
DEFAULT_UA = "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"


def _parse_lines(tokens: list[str]) -> list[int]:
    out: list[int] = []
    for tok in tokens:
        for piece in tok.split(","):
            piece = piece.strip()
            if not piece:
                continue
            if "-" in piece:
                lo_s, hi_s = piece.split("-", 1)
                lo, hi = int(lo_s), int(hi_s)
                if lo > hi:
                    raise ValueError(f"empty range: {piece}")
                out.extend(range(lo, hi + 1))
            else:
                out.append(int(piece))
    return out


def _collect_csv_urls(
    csv_path: Path, lines: list[int], fields: list[str]
) -> list[str]:
    with csv_path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    if len(rows) < 2:
        raise SystemExit(f"error: CSV has no data rows: {csv_path}")
    header = rows[0]
    missing = [f for f in fields if f not in header]
    if missing:
        raise SystemExit(
            f"error: unknown field(s): {', '.join(missing)}. "
            f"Available: {', '.join(header)}"
        )
    idx = [header.index(f) for f in fields]
    urls: list[str] = []
    for n in lines:
        if n < 2 or n > len(rows):
            raise SystemExit(f"error: line {n} out of range (2..{len(rows)})")
        row = rows[n - 1]
        for i in idx:
            val = row[i].strip()
            if val:
                urls.append(val)
    # preserve order but drop duplicates
    seen: set[str] = set()
    deduped: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


def _check(url: str, ua: str, timeout: int) -> tuple[int, str]:
    """Return (status_code_or_0, final_url). 0 means curl itself failed."""
    proc = subprocess.run(
        [
            "curl",
            "-sI",
            "-L",
            "-A",
            ua,
            "--max-time",
            str(timeout),
            "-o",
            "/dev/null",
            "-w",
            "%{http_code} %{url_effective}",
            url,
        ],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        return 0, proc.stderr.strip() or "curl failed"
    code_s, _, final = proc.stdout.strip().partition(" ")
    try:
        code = int(code_s)
    except ValueError:
        code = 0
    return code, final


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="check-urls",
        description=(
            "HEAD-check a batch of URLs with a browser user agent. "
            "Exit nonzero if any URL is not 2xx/3xx."
        ),
    )
    parser.add_argument(
        "targets",
        nargs="+",
        help=(
            "URLs to check, OR (with --from-csv) line numbers / ranges "
            "whose URL fields should be checked."
        ),
    )
    parser.add_argument(
        "--from-csv",
        action="store_true",
        help="Treat targets as CSV line numbers / ranges rather than URLs.",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help=f"CSV file path for --from-csv (default: {DEFAULT_CSV}).",
    )
    parser.add_argument(
        "--field",
        default="release_url,supporting_url",
        help=(
            "Comma-separated URL fields to pull when --from-csv "
            "(default: release_url,supporting_url)."
        ),
    )
    parser.add_argument(
        "--ua",
        default=DEFAULT_UA,
        help="User-Agent header to send.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=15,
        help="Per-request timeout in seconds (default: 15).",
    )
    args = parser.parse_args(argv)

    if args.from_csv:
        try:
            lines = _parse_lines(args.targets)
        except ValueError as e:
            print(f"error: bad line spec: {e}", file=sys.stderr)
            return 2
        fields = [f.strip() for f in args.field.split(",") if f.strip()]
        urls = _collect_csv_urls(args.csv, lines, fields)
    else:
        urls = list(args.targets)

    if not urls:
        print("error: no URLs to check", file=sys.stderr)
        return 2

    any_fail = False
    results: list[tuple[int, str, str]] = []
    for u in urls:
        code, final = _check(u, args.ua, args.timeout)
        results.append((code, u, final))
        if not (200 <= code < 400):
            any_fail = True

    width = max(len(str(c)) for c, _, _ in results) if results else 3
    for code, url, final in results:
        status = f"{code:<{width}}" if code else "ERR".ljust(width)
        if final and final != url:
            print(f"{status}  {url} -> {final}")
        else:
            print(f"{status}  {url}")
    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
