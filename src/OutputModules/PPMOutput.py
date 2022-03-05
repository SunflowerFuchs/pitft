from src.Colorspaces.RGBColorspace import RGBColorspace, RGBColorspaceSizes
from src.OutputModules.AbstractOutput import AbstractOutput


class PPMOutput(AbstractOutput):
    num_bytes = RGBColorspaceSizes.TWENTYFOUR

    def flush(self) -> None:
        filename = f'output{self._frame_count}.ppm'
        output = bytearray()
        output += bytes(f'P6\n{self.width}\n{self.height}\n{self._max_color_value}\n', 'utf-8')
        for pos in range(0, self.height * self.width):
            output += self._frame[pos].to_bytes(self.num_bytes, byteorder="little")
        with open(filename, 'wb') as f:
            f.write(output)
            f.close()

    def __init__(self, x_res: int, y_res: int, max_color_value: int = 255) -> None:
        self._max_color_value = max_color_value
        super().__init__(x_res, y_res, RGBColorspace(self.num_bytes, self._max_color_value))
