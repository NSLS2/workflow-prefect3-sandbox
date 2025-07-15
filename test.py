from __future__ import annotations

import os
import sys


def test(stuff=""):
    if stuff:
        print(f"test: {stuff}")  # noqa: T201
    else:
        print("test: EMPTY")  # noqa: T201


if __name__ == "__main__":
    args = sys.argv
    print(f"environ: {os.environ['TILED_API_KEY']}")  # noqa: T201
    if len(sys.argv) > 1:
        test(sys.argv[1])
    else:
        test()
