#!/usr/bin/env python3
"""Copy the rendered entry image to the make.fun output directory.

Stdlib only. Usage: MAKEFUN_OUTPUT_DIR=<dir> python3 main.py
Copies entry.png (in this script's directory) to $MAKEFUN_OUTPUT_DIR/entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
