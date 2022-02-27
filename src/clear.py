#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from src.OutputModules.PPMOutput import PPMOutput


load_dotenv()

xSize = int(os.getenv('xSize', 240))
ySize = int(os.getenv('ySize', 320))
output = PPMOutput(xSize, ySize)
output.next_frame()
