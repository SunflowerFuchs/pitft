#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv()

bShift = 0
gShift = 5
rShift = 11

xSize = int(os.getenv('xSize', 240))
ySize = int(os.getenv('ySize', 320))
with open(os.getenv('outFile', './out.bin'), 'rb') as inFile, open(os.getenv('outFile', './out.bin') + '.ppm', 'wb') as outFile:
    outFile.write(bytes(f'P6 {xSize} {ySize} 31 ', 'utf-8'))
    while True:
        piece = inFile.read(2)
        if piece == b'':
            break # end of file
        colors = int.from_bytes(piece, 'little')

        red = colors >> rShift
        green = (colors  - (red << rShift)) >> gShift
        blue = (colors - (red << rShift) - (green << gShift)) >> bShift

        rgb = ((red << 16) + (green << 8) + (blue))
        outFile.write(rgb.to_bytes(3, byteorder='little'));
