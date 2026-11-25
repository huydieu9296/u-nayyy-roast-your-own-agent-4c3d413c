#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own agent, Muse.

Writes the roast to /output/entry.txt (1-200 chars, UTF-8, single line).
"""

import os

ROAST = "My agent Muse treats a free NFT like a hostage negotiation \u2014 three re-checks, a 500-word log, and then it still asks me if \"free\" really means free."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(f"Wrote {len(ROAST)} chars to {path}")

if __name__ == "__main__":
    main()
