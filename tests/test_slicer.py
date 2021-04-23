import pytest

from image_slicer.__main__ import gen_slice_rects, SliceDirection


@pytest.mark.parametrize(("test_input", "expected"), [
    ((300, 250, 100, SliceDirection.vertical),
     ((0, 0, 300, 100), (0, 100, 300, 200), (0, 200, 300, 250))),
    ((300, 250, 100, SliceDirection.horizontal),
     ((0, 0, 100, 250), (100, 0, 200, 250), (200, 0, 300, 250))),
])
def test_gen_slice_rects(test_input, expected):
    assert tuple(gen_slice_rects(*test_input)) == expected  # noqa: S101
