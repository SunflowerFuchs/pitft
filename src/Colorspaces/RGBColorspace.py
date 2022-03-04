import enum
import math
from src.Colorspaces.AbstractColorspace import AbstractColorspace


class RGBColorspaceSizes(enum.IntEnum):
    EIGHT = 1
    SIXTEEN = 2
    TWENTYFOUR = 3


class RGBColorspace(AbstractColorspace):
    def __init__(self, size: RGBColorspaceSizes, max_value: int = 0):
        if size == RGBColorspaceSizes.EIGHT:
            self._max_red = 7
            self._max_green = 7
            self._max_blue = 3
            self._blue_shift = 5
            self._green_shift = 2
        elif size == RGBColorspaceSizes.SIXTEEN:
            self._max_red = 32
            self._max_green = 64
            self._max_blue = 32
            self._blue_shift = 11
            self._green_shift = 5
        elif size == RGBColorspaceSizes.TWENTYFOUR:
            self._max_red = 256
            self._max_green = 256
            self._max_blue = 256
            self._blue_shift = 16
            self._green_shift = 8
        else:
            raise ValueError('Only one of RGBColorSpaceSizes.* allowed for size param')

        self._max_red = min(max_value, self._max_red) if max_value > 0 else self._max_red
        self._max_green = min(max_value, self._max_green) if max_value > 0 else self._max_green
        self._max_blue = min(max_value, self._max_blue) if max_value > 0 else self._max_blue
        self._size = size

    def convert(self, red: float, green: float, blue: float) -> int:
        r_bits = int(red * self._max_red)
        g_bits = int(green * self._max_green)
        b_bits = int(blue * self._max_blue)

        return (b_bits << self._blue_shift) + (g_bits << self._green_shift) + r_bits
