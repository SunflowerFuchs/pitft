from src.Colorspaces.RGBColorspace import RGBColorspace, RGBColorspaceSizes
from src.OutputModules.AbstractOutput import AbstractOutput


class PiTFTOutput(AbstractOutput):
    num_bytes = RGBColorspaceSizes.SIXTEEN

    def flush(self) -> None:
        filename = '/dev/fb1'
        output = bytearray()
        for pos in range(0, self.height * self.width):
            output += self._frame[pos].to_bytes(self.num_bytes, byteorder="little")
        with open(filename, 'wb') as f:
            f.write(output)
            f.close()

    def __init__(self, x_res: int, y_res: int) -> None:
        super().__init__(x_res, y_res, RGBColorspace(self.num_bytes))
