from abc import ABC, abstractmethod
from typing import List, Dict
from src.Colorspaces.AbstractColorspace import AbstractColorspace


class AbstractOutput(ABC):
    def __init__(self, x_res: int, y_res: int, colorspace: AbstractColorspace):
        self._x_res: int = x_res
        self._y_res: int = y_res
        self._colorspace: AbstractColorspace = colorspace
        self._frame: List[int] = []  # gets filled in self.clear_frame()
        self._frame_count = 0

        # helper properties
        self._frame_pointer: int = 0
        self._frame_end: int = x_res * y_res

        # prepare the frame data
        self.clear_frame()

    def add_pixel(self, red: float, green: float, blue: float):
        if self._frame_pointer >= self._frame_end:
            raise IndexError('Frame is already full')

        # do the actual addition
        self._frame[self._frame_pointer] = self._colorspace.convert(red, green, blue)

        # add to the pointer
        self._frame_pointer += 1

    def next_frame(self):
        self.flush()
        self.clear_frame()
        self._frame_count += 1
        pass

    def clear_frame(self):
        self._frame = [0 for i in range(self._x_res * self._y_res)]
        self._frame_pointer = 0

    @abstractmethod
    def flush(self):
        pass
