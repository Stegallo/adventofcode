from typing import NamedTuple

from .utils import prod

from .common import AoCDay


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


def calculate_1(x, a=3, b=1):
    class Pos(NamedTuple):
        x: int
        y: int

    width = len(x[0])
    lenght = len(x)
    pos = Pos(0, 0)
    c = 0
    while pos.y < lenght:
        if x[pos.y][pos.x] == "#":
            c += 1
        pos = Pos((pos.x + a) % width, pos.y + b)
    return c


def calculate_2(x):
    rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod([calculate_1(x, *a) for a in rules])
