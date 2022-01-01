#!/usr/bin/env python3

import math
import os
from dotenv import load_dotenv

load_dotenv()

bShift = 0
gShift = 5
rShift = 11

xSize = int(os.getenv('xSize', 240))
ySize = int(os.getenv('ySize', 320))
with open(os.getenv('outFile', './out.bin'), 'wb') as f:
    output = bytearray()
    for y in range(0, ySize):
        for x in range(0, xSize):
            xVal = math.floor((x / xSize * 32))
            yVal = math.floor((y / ySize * 32))

            xCol = xVal << rShift
            yCol = yVal << bShift
            output += (xCol + yCol).to_bytes(2, byteorder='little')
    f.write(output)
