#!/usr/bin/env python3

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

output.next_frame()
