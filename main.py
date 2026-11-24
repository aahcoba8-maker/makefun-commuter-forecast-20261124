#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (max 140 characters) for an invented
city to /output/entry.txt (MAKEFUN_OUTPUT_DIR when set, else the script dir).
Stdlib only.
"""

import os

ENTRY = (
    "In Wobbleford, sun by 7:40 and the 8:05 bus runs on time \u2014 "
    "dry shoes, hot coffee, and the last window seat has your name on it."
)


def main():
    if not (1 <= len(ENTRY) <= 140):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-140")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line with no surrounding space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
