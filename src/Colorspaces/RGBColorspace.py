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
        elif size == RGBColorspaceSizes.SIXTEEN:
            self._max_red = 32
            self._max_green = 64
            self._max_blue = 32
        elif size == RGBColorspaceSizes.TWENTYFOUR:
            self._max_red = 256
            self._max_green = 256
            self._max_blue = 256

        self._max_red = min(max_value, self._max_red) if max_value > 0 else self._max_red
        self._max_green = min(max_value, self._max_green) if max_value > 0 else self._max_green
        self._max_blue = min(max_value, self._max_blue) if max_value > 0 else self._max_blue
        self._size = size

    def convert(self, red: float, green: float, blue: float) -> int:
        r_bits = int(red * self._max_red)
        g_bits = int(green * self._max_green)
        b_bits = int(blue * self._max_blue)

        if self._size == RGBColorspaceSizes.EIGHT:
            return (b_bits << 5) + (g_bits << 2) + r_bits
        elif self._size == RGBColorspaceSizes.SIXTEEN:
            return (b_bits << 11) + (g_bits << 5) + r_bits
        elif self._size == RGBColorspaceSizes.TWENTYFOUR:
            return (b_bits << 16) + (g_bits << 8) + r_bits

        # shouldn't happen
        return 0
