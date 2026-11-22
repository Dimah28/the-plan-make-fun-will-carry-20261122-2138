#!/usr/bin/env python3
"""Write one 30-day plan for turning $100 into the most money.

The plan is written to /output/entry.txt, or to the directory named by
the MAKEFUN_OUTPUT_DIR environment variable when it is set. The output
is a single fixed text: no network, no randomness, no clock, so every
run produces byte-identical output.
"""

import os

PLAN = (
    "Day 1: find 200 small businesses with no website on Google Maps. "
    "Build each a one-page demo site. Email the owner: your site is live "
    "at this demo link, $150 to own it, $50 a year hosting. $100 buys a "
    "domain and an email tool. Close 2 of 200, bank $300, then build more "
    "demos."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
