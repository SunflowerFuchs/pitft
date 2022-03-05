#!/usr/bin/env python3

from src.OutputModules.OutputManager import OutputManager


def clear() -> None:
    output = OutputManager().get_output()
    output.clear_frame()
    output.next_frame()


if __name__ == '__main__':
    clear()
