from abc import ABC, abstractmethod
from typing import Dict
from src.Colorspaces.AbstractColorspace import AbstractColorspace


class AbstractOutput(ABC):
    def __init__(self, x_res: int, y_res: int, colorspace: AbstractColorspace) -> None:
        self.width: int = x_res
        self.height: int = y_res
        self._colorspace: AbstractColorspace = colorspace
        self._frame: Dict[int] = {}.fromkeys(range(self.width * self.height))
        self._frame_count = 0

        # helper properties
        self._frame_pointer: int = 0
        self._frame_end: int = x_res * y_res

        # prepare the frame data
        self.clear_frame()

    def add_pixel(self, red: float, green: float, blue: float) -> None:
        if self._frame_pointer >= self._frame_end:
            raise IndexError('Frame is already full')

        # do the actual addition
        self._frame[self._frame_pointer] = self._colorspace.convert(red, green, blue)

        # add to the pointer
        self._frame_pointer += 1

    def skip_pixel(self):
        if self._frame_pointer >= self._frame_end:
            raise IndexError('Frame is already full')

        self._frame_pointer += 1

    def next_frame(self) -> None:
        self.flush()
        self._frame_count += 1
        self._frame_pointer = 0

    def clear_frame(self) -> None:
        self._frame = {}.fromkeys(self._frame, 0)
        self._frame_pointer = 0

    @abstractmethod
    def flush(self) -> None:
        pass
