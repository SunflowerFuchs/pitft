#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv()

xSize = int(os.getenv('xSize', 240))
ySize = int(os.getenv('ySize', 320))
with open(os.getenv('outFile', './out.bin'), 'wb') as f:
    f.write((0).to_bytes(xSize * ySize * 2, byteorder="little"))
