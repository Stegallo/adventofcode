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
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

    def _calculate_1(self):
        result = 0
        result_grid = Grid.from_h_l(10, 10)
        for x in self.grid.keys():
            if self.grid.grid.get(x) != "@":
                continue
            c = 0
            for y in x.crown():
                if y in self.grid.keys():
                    c += 1 if self.grid.grid.get(y) == "@" else 0
            if c <= 3:
                result += 1
            if self.grid.grid.get(x) == "@":
                result_grid.grid[x] = str(c)
        return result

    def _calculate_2(self):
        result = 0
        grid = self.grid
        while True:
            removed = 0
            result_grid = Grid.from_h_l(10, 10)
            for x in grid.keys():
                if grid.grid.get(x) != "@":
                    continue
                c = 0
                for y in x.crown():
                    if y in grid.keys():
                        c += 1 if grid.grid.get(y) == "@" else 0
                if c <= 3:
                    result += 1
                    removed += 1
                if grid.grid.get(x) == "@":
                    result_grid.grid[x] = "x" if str(c) <= "3" else "@"
            if removed == 0:
                break
            grid = result_grid
        return result
