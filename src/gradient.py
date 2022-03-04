#!/usr/bin/env python3

import math
import os
from dotenv import load_dotenv
from src.OutputModules.PPMOutput import PPMOutput
from src.OutputModules.PiTFTOutput import PiTFTOutput


def generate_gradient_images():
    load_dotenv()

    x_size = int(os.getenv('xSize', 240))
    y_size = int(os.getenv('ySize', 320))
    output_type = os.getenv('output', 'ppm')
    if output_type == 'ppm':
        output = PPMOutput(x_size, y_size)
    elif output_type == 'pitft':
        output = PiTFTOutput(x_size, y_size)
    else:
        raise ValueError(f'Unknown output type {output_type}')

    for y in range(0, y_size):
        for x in range(0, x_size):
            x_val = x / x_size
            y_val = y / y_size

            output.add_pixel(x_val, 0, y_val)
    output.next_frame()

    for y in range(0, y_size):
        for x in range(0, x_size):
            x_val = x / x_size
            y_val = y / y_size

            output.add_pixel(0, y_val, x_val)
    output.next_frame()

    for y in range(0, y_size):
        for x in range(0, x_size):
            x_val = x / x_size
            y_val = y / y_size

            output.add_pixel(y_val, x_val, 0)
    output.next_frame()


if __name__ == '__main__':
    generate_gradient_images()
