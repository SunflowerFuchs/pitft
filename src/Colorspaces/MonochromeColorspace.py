import math
from src.Colorspaces.AbstractColorspace import AbstractColorspace


class MonochromeColorspace(AbstractColorspace):
    def __init__(self, max_value: int):
        self._max_value = max_value

    def convert(self, red: float, green: float, blue: float) -> int:
        avg = (red + green + blue) // 3
        return int(avg * self._max_value)
