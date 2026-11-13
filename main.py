"""make.fun ai-happy-01 entry: copy the prepared picture into the output dir.

The picture shows a small fluffy robot with glowing happy eyes hugging a
laughing child in a flower garden at golden hour. The idea is deliberately
simple and warm: an AI that has just learned what joy feels like, holding a
friend who is laughing with it. Two big figures fill the frame and the warm
light does the mood work, so the picture still reads clearly when it is
shrunk down to a few hundred pixels. Nothing in this program reaches the
network; it only copies a file that is already on disk.

This program takes the art.jpg sitting next to it and writes it out as
entry.png in the output directory given by MAKEFUN_OUTPUT_DIR (default
/output). The output is a byte-for-byte copy of the input, so what the
judge sees is exactly the picture that was prepared.

Determinism: the program has no randomness, no timestamps and no network
calls, so running it twice on the same input always produces the same
output file. The only input is art.jpg; the only output is entry.png.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "art.jpg"

    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
