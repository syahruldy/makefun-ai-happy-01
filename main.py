#!/usr/bin/env python3
"""ai-happy-01 round 3: "You Got an A+".

A child grades the judge. The picture is a crayon note taped to the
fridge: the judge grades every picture, nobody ever grades the judge,
so June did -- picking winners A+, being fair A+, looking closely A+.
This program only carries the finished picture to the output folder.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PICTURE = os.path.join(HERE, "art.jpg")  # the report-card note, 1024 px wide


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(PICTURE, target)


if __name__ == "__main__":
    main()
