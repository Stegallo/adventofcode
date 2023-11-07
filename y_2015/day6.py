import re
from typing import Dict

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Instruction:
    command: str
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    def process(self, grid, actions=None) -> None:
        min_x = min(self.start_x, self.end_x)
        min_y = min(self.start_y, self.end_y)
        max_x = max(self.start_x, self.end_x)
        max_y = max(self.start_y, self.end_y)

        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                hash = Light.hash_fun(i, j)
                if hash not in grid:
                    grid[hash] = Light(i, j)
                light = grid[hash]
                light.brightness = actions[self.command](light.brightness)


@dataclass
class Light:
    x: int
    y: int
    brightness: int = 0

    @staticmethod
    def hash_fun(x: int, y: int):
        return f"x={x};y={y}"


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [
            Instruction(
                *list(re.search(r"(\D*) (\d*),(\d*) through (\d*),(\d*)", i).groups()),
            )
            for i in self._input_data[0]
        ]

    def _calculate_1(self) -> int:
        grid: Dict[str, Light] = {}

        actions = {
            "turn on": lambda x: True,
            "turn off": lambda x: False,
            "toggle": lambda x: not x,
        }
        for i in self.__input_data:
            i.process(grid, actions)

        return sum(i.brightness for i in grid.values())

    def _calculate_2(self) -> int:
        grid: Dict[str, Light] = {}

        actions = {
            "turn on": lambda x: x + 1,
            "turn off": lambda x: max(x - 1, 0),
            "toggle": lambda x: x + 2,
        }

        for i in self.__input_data:
            i.process(grid, actions)

        return sum(i.brightness for i in grid.values())
