"""Copy the bundled entry image to the output directory.

Standard library only: reads entry.png next to this file and writes it
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png).
Deterministic: the same input bytes always produce the same output bytes.
The image itself is the entry's content; this program only delivers it.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
