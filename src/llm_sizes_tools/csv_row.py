"""Print CSV rows with fields labelled by their header names.

Uses csv.reader so RFC 4180 quoting (commas inside quoted strings) is handled
correctly — unlike naive comma-splitting, which misaligns columns whenever a
quoted field contains a comma.

Accepts one or more line numbers and/or hyphen ranges. When more than one
row is printed, each row is prefixed with `=== line N ===` so you don't
need to wrap the command in a shell for-loop.

Examples
--------
$ uv run csv-row 5
model_name               Mixtral 8x22B
organization             Mistral AI
...

$ uv run csv-row 5 --field cap_tool_use
true

$ uv run csv-row 5 --field cap_tool_use,context_window
cap_tool_use     true
context_window   65536

$ uv run csv-row 52 71 78 --field model_name,param_source_note
=== line 52 ===
model_name         GPT-1
param_source_note  117M params per paper architecture (12 layers x 768 dim x 12 heads)
=== line 71 ===
...

$ uv run csv-row 52-60 --field model_name
=== line 52 ===
GPT-1
=== line 53 ===
GPT-2
...
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

DEFAULT_CSV = Path(__file__).resolve().parents[2] / "llm_sizes.csv"


def _parse_lines(tokens: list[str]) -> list[int]:
    """Expand `5`, `52-60`, `5,7,12` tokens into a flat ordered int list."""
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


def _render_row(
    header: list[str],
    row: list[str],
    requested: list[str] | None,
) -> list[str]:
    if requested is not None:
        if len(requested) == 1:
            return [row[header.index(requested[0])]]
        width = max(len(f) for f in requested)
        return [
            f"{name:<{width}}  {row[header.index(name)]}"
            for name in requested
        ]
    width = max(len(h) for h in header)
    return [f"{name:<{width}}  {value}" for name, value in zip(header, row)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="csv-row",
        description="Print one or more CSV rows with each field labelled.",
    )
    parser.add_argument(
        "lines",
        nargs="+",
        help=(
            "One or more 1-based line numbers (>=2). Accepts ranges "
            "like 52-60 and comma-lists like 5,7,12."
        ),
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help=f"CSV file path (default: {DEFAULT_CSV}).",
    )
    parser.add_argument(
        "--field",
        help=(
            "Comma-separated list of header names to print. "
            "If omitted, all fields are printed."
        ),
    )
    args = parser.parse_args(argv)

    try:
        line_nums = _parse_lines(args.lines)
    except ValueError as e:
        print(f"error: bad line spec: {e}", file=sys.stderr)
        return 2
    if not line_nums:
        print("error: no line numbers given", file=sys.stderr)
        return 2

    try:
        with args.csv.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
    except FileNotFoundError:
        print(f"error: CSV not found: {args.csv}", file=sys.stderr)
        return 2

    if len(rows) < 2:
        print(f"error: CSV has no data rows: {args.csv}", file=sys.stderr)
        return 2

    header = rows[0]

    requested: list[str] | None = None
    if args.field:
        requested = [f.strip() for f in args.field.split(",") if f.strip()]
        missing = [f for f in requested if f not in header]
        if missing:
            print(
                f"error: unknown field(s): {', '.join(missing)}. "
                f"Available: {', '.join(header)}",
                file=sys.stderr,
            )
            return 2

    multi = len(line_nums) > 1
    for n in line_nums:
        if n < 2 or n > len(rows):
            print(
                f"error: line {n} out of range (2..{len(rows)})",
                file=sys.stderr,
            )
            return 2
        row = rows[n - 1]
        if len(row) != len(header):
            print(
                f"error: line {n} has {len(row)} fields but header has "
                f"{len(header)}; CSV may be malformed.",
                file=sys.stderr,
            )
            return 2
        if multi:
            print(f"=== line {n} ===")
        for out in _render_row(header, row, requested):
            print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
