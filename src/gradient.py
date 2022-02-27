#!/usr/bin/env python3

import math
import os
from dotenv import load_dotenv
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

for y in range(0, ySize):
    for x in range(0, xSize):
        xVal = x / xSize
        yVal = y / ySize

        output.add_pixel(xVal, 0, yVal)
output.next_frame()

for y in range(0, ySize):
    for x in range(0, xSize):
        xVal = x / xSize
        yVal = y / ySize

        output.add_pixel(0, yVal, xVal)
output.next_frame()

for y in range(0, ySize):
    for x in range(0, xSize):
        xVal = x / xSize
        yVal = y / ySize

        output.add_pixel(yVal, xVal, 0)
output.next_frame()
