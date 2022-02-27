from src.Colorspaces.RGBColorspace import RGBColorspace, RGBColorspaceSizes
from src.OutputModules.AbstractOutput import AbstractOutput


class PiTFTOutput(AbstractOutput):
    num_bytes = RGBColorspaceSizes.SIXTEEN

    def flush(self):
        filename = '/dev/fb1'
        output = bytearray()
        with open(filename, 'wb') as f:
            for y in range(0, self._y_res):
                for x in range(0, self._x_res):
                    output += self._frame[y][x].to_bytes(self.num_bytes, byteorder="little")
            f.write(output)
            f.close()

    def __init__(self, x_res: int, y_res: int):
        super().__init__(x_res, y_res, RGBColorspace(self.num_bytes))
        return
