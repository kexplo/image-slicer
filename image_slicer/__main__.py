from enum import Enum
import os
from pathlib import Path

from PIL import Image
from typer import Typer

app = Typer()


class SliceDirection(str, Enum):
    vertical = "v"
    horizontal = "h"


def gen_slice_rects(
    width: int, height: int, delta_pixel: int, direction: SliceDirection
):
    cursor = 0
    if direction == SliceDirection.vertical:
        while cursor < height:
            # (left, upper, right, lower)
            yield (0, cursor, width, min(height, cursor + delta_pixel))
            cursor += delta_pixel
    else:
        while cursor < width:
            # (left, upper, right, lower)
            yield (cursor, 0, min(width, cursor + delta_pixel), height)
            cursor += delta_pixel


@app.command()
def run(
    image_path: Path,
    direction: SliceDirection = SliceDirection.vertical,
    delta_pixel: int = 2000,
):
    with Image.open(image_path) as image:
        width, height = image.size
        count = 0
        filename, ext = os.path.splitext(os.path.basename(image_path))
        for crop_rect in gen_slice_rects(
            width, height, delta_pixel, direction
        ):
            cropped_image = image.crop(crop_rect)
            output_filename = f"{filename}_{count:03d}.{ext}"
            cropped_image.save(output_filename)
            count += 1
