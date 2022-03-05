#!/usr/bin/env python3
from enum import Enum, auto
from src.OutputModules.OutputManager import OutputManager


class GradientColor(Enum):
    Red = auto()
    Green = auto()
    Blue = auto()


def generate_gradient_images(
        start_color: GradientColor = GradientColor.Blue,
        end_color: GradientColor = GradientColor.Red
) -> None:
    output = OutputManager().get_output()

    for y in range(0, output.height):
        y_val = y / output.height
        for x in range(0, output.width):
            x_val = x / output.width
            red = 0
            green = 0
            blue = 0
            if start_color == GradientColor.Red:
                red = x_val
            elif start_color == GradientColor.Green:
                green = x_val
            else:
                blue = x_val

            if end_color == GradientColor.Red:
                red = y_val
            elif end_color == GradientColor.Green:
                green = y_val
            else:
                blue = y_val

            output.add_pixel(red, green, blue)
    output.next_frame()


if __name__ == '__main__':
    generate_gradient_images()
