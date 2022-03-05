from enum import Enum
from os import getenv
from dotenv import load_dotenv
from src.OutputModules.AbstractOutput import AbstractOutput


class OutputTypes(str, Enum):
    PiTFT = 'pitft'
    Emulated = 'emulated'
    HighQuality = 'hqppm'


class OutputManager:
    default_width = 240
    default_height = 320
    default_type = OutputTypes.Emulated
    emulated_quality = 31

    _output = None

    def __init__(self):
        load_dotenv()

    def get_output(self) -> AbstractOutput:
        width = int(getenv('xSize', self.default_width))
        height = int(getenv('ySize', self.default_height))
        output_type = getenv('output', self.default_type)

        if self._output is None:
            if output_type == OutputTypes.PiTFT:
                from src.OutputModules.PiTFTOutput import PiTFTOutput
                self._output = PiTFTOutput(width, height)
            elif output_type == OutputTypes.Emulated:
                from src.OutputModules.PPMOutput import PPMOutput
                self._output = PPMOutput(width, height, self.emulated_quality)
            elif output_type == OutputTypes.HighQuality:
                from src.OutputModules.PPMOutput import PPMOutput
                self._output = PPMOutput(width, height)
            else:
                raise ValueError(f'Unknown output type {output_type}')

        return self._output
