from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        print(f"{self._input_data=}")
        print(f"{len(self._input_data)=}")
        print(f"{len(self._input_data[0])=}")
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data = [Row(i) for j in self._input_data for i in j]
        for x in self.__input_data:
            print(f"{x}")

    def _calculate_1(self):
        result = 0
        for x in self.__input_data:
            ...
        return result

    def _calculate_2(self):
        result = 0
        return result
