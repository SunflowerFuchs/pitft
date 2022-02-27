from abc import ABC, abstractmethod


class AbstractColorspace(ABC):
    @abstractmethod
    def convert(self, red: float, green: float, blue: float) -> int:
        pass
