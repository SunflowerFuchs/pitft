from src.Colorspaces.RGBColorspace import RGBColorspace, RGBColorspaceSizes
from src.OutputModules.AbstractOutput import AbstractOutput


class PPMOutput(AbstractOutput):
    max_color_value = 31
    num_bytes = RGBColorspaceSizes.TWENTYFOUR

    def flush(self):
        filename = f'output{self._frame_count}.ppm'
        output = bytearray()
        with open(filename, 'wb') as f:
            output += bytes(f'P6\n{self._x_res}\n{self._y_res}\n{self.max_color_value}\n', 'utf-8')
            for y in range(0, self._y_res):
                for x in range(0, self._x_res):
                    output += self._frame[y][x].to_bytes(self.num_bytes, byteorder="little")
            f.write(output)
            f.close()

    def __init__(self, x_res: int, y_res: int):
        super().__init__(x_res, y_res, RGBColorspace(self.num_bytes, self.max_color_value))
        return
