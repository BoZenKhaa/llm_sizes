"""Print a CSV row's fields labelled with their headers.

Uses csv.reader so RFC 4180 quoting (commas inside quoted strings) is handled
correctly — unlike naive comma-splitting, which misaligns columns whenever a
quoted field contains a comma. Intended for the verifier agent to inspect
rows without having to hand-count commas.

Examples
--------
$ uv run csv-row 5
model_name               Mixtral 8x22B
organization             Mistral AI
...
cap_tool_use             true
release_url              https://mistral.ai/news/mixtral-8x22b
supporting_url

$ uv run csv-row 5 --field cap_tool_use
true

$ uv run csv-row 5 --field cap_tool_use,context_window
cap_tool_use     true
context_window   65536
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

DEFAULT_CSV = Path(__file__).resolve().parents[2] / "llm_sizes.csv"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="csv-row",
        description="Print a CSV row with each field labelled by its header.",
    )
    parser.add_argument(
        "line",
        type=int,
        help="1-based line number (>=2; line 1 is the header).",
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
        with args.csv.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
    except FileNotFoundError:
        print(f"error: CSV not found: {args.csv}", file=sys.stderr)
        return 2

    if len(rows) < 2:
        print(f"error: CSV has no data rows: {args.csv}", file=sys.stderr)
        return 2

    header = rows[0]
    if args.line < 2 or args.line > len(rows):
        print(
            f"error: line {args.line} out of range (2..{len(rows)})",
            file=sys.stderr,
        )
        return 2

    row = rows[args.line - 1]
    if len(row) != len(header):
        print(
            f"error: row has {len(row)} fields but header has {len(header)}; "
            "CSV may be malformed.",
            file=sys.stderr,
        )
        return 2

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
        if len(requested) == 1:
            print(row[header.index(requested[0])])
            return 0
        width = max(len(f) for f in requested)
        for name in requested:
            print(f"{name:<{width}}  {row[header.index(name)]}")
        return 0

    width = max(len(h) for h in header)
    for name, value in zip(header, row):
        print(f"{name:<{width}}  {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
