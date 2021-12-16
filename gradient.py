#!/usr/bin/env python3

import math
import os
from dotenv import load_dotenv

load_dotenv()

xSize = 240
ySize = 320
with open(os.getenv('OUTPUT'), 'wb') as f:
    output = bytearray()
    for y in range(0, ySize):
        for x in range(0, xSize):
            xb = math.floor((x / xSize * 32)) << 0
            # xg = math.floor((x/xSize*32)) << 5
            # xr = math.floor((x/xSize*32)) << 11
            # yb = math.floor((y/ySize*32)) << 0
            # yg = math.floor((y/ySize*32)) << 5
            yr = math.floor((y / ySize * 32)) << 11
            output += (xb + yr).to_bytes(2, byteorder='little')
    f.write(output)
