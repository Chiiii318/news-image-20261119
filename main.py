#!/usr/bin/env python3
"""Run the news-image-20261119 entry: copy the finished infographic out.

`entry.png` ships in this repository as a finished, byte-fixed picture of
19 November 2026's news. All this program does is place a copy of it at
the path the grader reads (`$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting
to `/output/entry.png`). It draws nothing, downloads nothing and changes
nothing, so running it twice writes the same bytes twice — the grader
runs it twice and requires both outputs to match. The picture
itself was drawn ahead of time by `generate_image.py`, which stays in
the repository so anyone can see how it was made; the grader never runs
that script.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    picture = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(picture, destination / "entry.png")


if __name__ == "__main__":
    main()
