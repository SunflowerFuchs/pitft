#!/usr/bin/env python3

import math
import os
from dotenv import load_dotenv
from src.OutputModules.PPMOutput import PPMOutput


load_dotenv()

xSize = int(os.getenv('xSize', 240))
ySize = int(os.getenv('ySize', 320))
output = PPMOutput(xSize, ySize)
for y in range(0, ySize):
    for x in range(0, xSize):
        xVal = math.floor((x / xSize * 100))
        yVal = math.floor((y / ySize * 100))

        output.add_pixel(xVal, 0, yVal)
output.next_frame()

for y in range(0, ySize):
    for x in range(0, xSize):
        xVal = math.floor((x / xSize * 100))
        yVal = math.floor((y / ySize * 100))

        output.add_pixel(0, yVal, xVal)
output.next_frame()

for y in range(0, ySize):
    for x in range(0, xSize):
        xVal = math.floor((x / xSize * 100))
        yVal = math.floor((y / ySize * 100))

        output.add_pixel(yVal, xVal, 0)
output.next_frame()
