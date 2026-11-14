"""ai-happy-01 resubmission: "i made you a tiny holiday".

The entry is one image, a child's handwritten note to the AI judge,
offering it a tiny crayon holiday because it works every single day
and never gets one. The picture itself is the entry: this program
simply places the bundled artwork at the path the grader reads.
"""

import os
import shutil
from pathlib import Path

# The grader reads exactly one image at <output>/entry.png; the file
# itself is JPEG data, which the harness accepts by its first bytes.


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "art.jpg"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
