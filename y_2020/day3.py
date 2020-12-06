from typing import NamedTuple

from .common import AoCDay
from .utils import prod


class Pos(NamedTuple):
    x: int
    y: int


class Day(AoCDay):
    def __init__(self):
        super().__init__(3)

    def _preprocess_input(self, input_data):
        return input_data

    def _calculate_1(self, a=3, b=1):
        x = self._input_data

        width = len(x[0])
        lenght = len(x)
        pos = Pos(0, 0)
        c = 0
        while pos.y < lenght:
            if x[pos.y][pos.x] == "#":
                c += 1
            pos = Pos((pos.x + a) % width, pos.y + b)
        return c

    def _calculate_2(self):
        rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return prod([self._calculate_1(*a) for a in rules])
