#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from noise import snoise3
from random import randint
from src.OutputModules.PPMOutput import PPMOutput
from src.OutputModules.PiTFTOutput import PiTFTOutput


def generate_perlin_images(max_frame_count: int = 10):
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

    frame_count = 0
    x_offset = randint(1, 10000)
    y_offset = randint(1, 10000)
    red_offset = randint(1, 10000)
    green_offset = randint(1, 10000)
    blue_offset = randint(1, 10000)
    while frame_count < max_frame_count:
        z = (0.05 * frame_count)
        red_z = red_offset + z
        green_z = green_offset + z
        blue_z = blue_offset + z
        for y in range(0 + y_offset, y_size + y_offset):
            y_val = y / 100
            for x in range(0 + x_offset, x_size + x_offset):
                x_val = x / 100
                red = (1 + snoise3(x_val, y_val, red_z)) / 2
                green = (1 + snoise3(x_val, y_val, green_z)) / 2
                blue = (1 + snoise3(x_val, y_val, blue_z)) / 2

                output.add_pixel(red, green, blue)
        output.next_frame()
        frame_count += 1


if __name__ == '__main__':
    generate_perlin_images()
