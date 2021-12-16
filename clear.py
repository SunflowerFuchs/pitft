#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv()

xsize = 240
ysize = 320
with open(os.getenv('OUTPUT'), 'wb') as f:
  output = bytearray()
  for y in range(0,ysize):
    for x in range(0,xsize):
      output += (0).to_bytes(1, byteorder='little')
      output += (0).to_bytes(1, byteorder='little')

  f.write(output)
