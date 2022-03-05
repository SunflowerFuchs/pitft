#!/usr/bin/env python3
from enum import Enum, auto
from src.OutputModules.OutputManager import OutputManager


class GradientColor(Enum):
    Red = auto()
    Green = auto()
    Blue = auto()


def generate_gradient_images(
        horizontal_color: GradientColor = GradientColor.Blue,
        vertical_color: GradientColor = GradientColor.Red
) -> None:
    output = OutputManager().get_output()

    red = 0
    green = 0
    blue = 0
    for y in range(0, output.height):
        y_val = y / output.height
        for x in range(0, output.width):
            x_val = x / output.width

            if horizontal_color == GradientColor.Red:
                red = x_val
            elif horizontal_color == GradientColor.Green:
                green = x_val
            else:
                blue = x_val

            if vertical_color == GradientColor.Red:
                red = y_val
            elif vertical_color == GradientColor.Green:
                green = y_val
            else:
                blue = y_val

            output.add_pixel(red, green, blue)
    output.next_frame()


if __name__ == '__main__':
    generate_gradient_images()
