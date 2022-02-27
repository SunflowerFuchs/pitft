#!/usr/bin/env python3

import os

from dotenv import load_dotenv
from noise import snoise3
from src.OutputModules.PPMOutput import PPMOutput
from src.OutputModules.PiTFTOutput import PiTFTOutput

load_dotenv()

xSize = int(os.getenv('xSize', 240))
ySize = int(os.getenv('ySize', 320))
outputType = os.getenv('output', 'ppm')
if outputType == 'ppm':
    output = PPMOutput(xSize, ySize)
elif outputType == 'pitft':
    output = PiTFTOutput(xSize, ySize)
else:
    raise ValueError(f'Unknown output type {outputType}')

max_frame_count = 10
frame_count = 0
while frame_count < max_frame_count:
    for y in range(0, ySize):
        for x in range(0, xSize):
            red = (1 + snoise3(x / 100, y / 100, 1 + (0.05 * frame_count))) / 2
            green = (1 + snoise3(x / 100, y / 100, 2 + (0.05 * frame_count))) / 2
            blue = (1 + snoise3(x / 100, y / 100, 3 + (0.05 * frame_count))) / 2

            output.add_pixel(red, green, blue)
    output.next_frame()
    frame_count += 1
