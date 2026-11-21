#!/usr/bin/env python3
"""Write the awe entry text to entry.txt in the output directory.

Stdlib only. Output directory resolution order:
  1. MAKEFUN_OUTPUT_DIR environment variable
  2. --output command-line argument
  3. /output
"""

import argparse
import os
import sys
from pathlib import Path

TEXT = (
    "Far above you, a star you will never name\n"
    "is ending its long burning. Its light is still\n"
    "travelling, patient as rain, through a dark\n"
    "so wide your whole life fits inside one\n"
    "quiet second of it. Nothing is asked of you.\n"
    "Rest in the size of it."
)

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def resolve_output_dir(cli_output: str | None) -> Path:
    env_output = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_output:
        return Path(env_output)
    if cli_output:
        return Path(cli_output)
    return Path("/output")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the awe entry text to entry.txt."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output directory (overridden by MAKEFUN_OUTPUT_DIR).",
    )
    args = parser.parse_args()

    code_points = len(TEXT)
    if not TEXT.strip():
        print("error: entry text is blank", file=sys.stderr)
        return 1
    if code_points < MIN_CODE_POINTS or code_points > MAX_CODE_POINTS:
        print(
            f"error: entry text is {code_points} code points; "
            f"must be {MIN_CODE_POINTS}-{MAX_CODE_POINTS} code points",
            file=sys.stderr,
        )
        return 1

    output_dir = resolve_output_dir(args.output)
    output_path = output_dir / "entry.txt"
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path.write_text(TEXT + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1

    print(
        f"Wrote {code_points} code points to {output_path} "
        f"(plus one trailing newline)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
