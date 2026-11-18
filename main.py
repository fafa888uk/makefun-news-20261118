"""News image entry for make.fun, 18 November 2026.

The program copies the finished front page, entry.png, which sits
beside this file in the repository, to the output directory.
It uses only the Python standard library, makes no network calls,
and always writes the same bytes, so two runs match.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        sys.exit("entry.png not found beside main.py")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) == 0:
        sys.exit("entry.png copied empty")


if __name__ == "__main__":
    main()
