import math
from src.Colorspaces.AbstractColorspace import AbstractColorspace


class MonochromeColorspace(AbstractColorspace):
    def __init__(self, max_value: int):
        self._max_value = max_value

    def convert(self, red: float, green: float, blue: float) -> int:
        avg = math.floor((red + green + blue) / 3)
        return math.floor(avg * self._max_value)
