from typing import Optional

from pydantic.dataclasses import dataclass
from collections import defaultdict


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


@dataclass
class Direction:
    y: int
    x: int
    icon: str

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def right(self):
        if (self.y, self.x) == (-1, 0):
            return Direction(0, 1, ">")
        if (self.y, self.x) == (0, 1):
            return Direction(1, 0, "v")
        if (self.y, self.x) == (1, 0):
            return Direction(0, -1, "<")
        if (self.y, self.x) == (0, -1):
            return Direction(-1, 0, "^")
        raise Exception


@dataclass
class Cursor:
    pos: Point
    dir: Direction

    def ahead(self):
        return Point(self.pos.x + self.dir.x, self.pos.y + self.dir.y)

    def turn_right(self):
        self.dir = self.dir.right()

    def move_forward(self):
        self.pos = self.ahead()


@dataclass
class Grid:
    grid: dict[Point, str]
    height: int
    length: int
    values: Optional[dict[str, list]] = None

    def __post_init__(self) -> None:
        self.values = defaultdict(list)
        for i, k in self.grid.items():
            self.values[k].append(i)

    @staticmethod
    def from_input(input_data):
        input = [list(chunk) for chunk in input_data]

        grid = {}
        for y in input:
            for c, x in enumerate(y):
                for i, k in enumerate(x):
                    grid[Point(i, c)] = k

        return Grid(grid, c + 1, i + 1)

    def display(self) -> None:
        for i in range(self.height):
            line = [self.grid[Point(j, i)] for j in range(self.length)]
            print("".join(line))

    def items(self):
        return self.grid.items()

    def keys(self):
        return self.grid.keys()
