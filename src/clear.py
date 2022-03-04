#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from src.OutputModules.PPMOutput import PPMOutput
from src.OutputModules.PiTFTOutput import PiTFTOutput


def clear():
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

    output.clear_frame()
    output.next_frame()


if __name__ == '__main__':
    clear()
