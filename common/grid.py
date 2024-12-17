from typing import Optional, Any

from pydantic.dataclasses import dataclass

# from dataclasses import dataclass  # disabling pydantic may lead to 5x speed

from collections import defaultdict

DIRS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
DIRS_8 = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "1": (-1, -1),
    "7": (-1, 1),
    "L": (1, 1),
    "J": (1, -1),
}


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    @staticmethod
    def from_dir(d) -> Any:
        return Point(d.x, d.y)


@dataclass
class Direction:
    y: int
    x: int
    icon: str

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def right(self):
        if self.icon == "^":
            return Direction(0, 1, ">")
        if self.icon == ">":
            return Direction(1, 0, "v")
        if self.icon == "v":
            return Direction(0, -1, "<")
        if self.icon == "<":
            return Direction(-1, 0, "^")
        raise Exception

    def left(self):
        if self.icon == "^":
            return Direction(0, -1, "<")
        if self.icon == ">":
            return Direction(-1, 0, "^")
        if self.icon == "v":
            return Direction(0, 1, ">")
        if self.icon == "<":
            return Direction(1, 0, "v")
        raise Exception

    @staticmethod
    def from_symbol(symbol: str):
        return Direction(
            *DIRS[symbol],
            symbol,
        )

    @staticmethod
    def from_symbol8(symbol: str):
        return Direction(
            *DIRS_8[symbol],
            symbol,
        )


@dataclass
class Cursor:
    pos: Point
    dir: Direction
    x: int = 0
    y: int = 0

    def ahead(self):
        return Point(self.pos.x + self.dir.x, self.pos.y + self.dir.y)

    def all_ahead(self):
        # self.x = 0
        # self.y = 0
        while True:
            self.x += 1
            self.y += 1
            return Point(
                self.pos.x + self.x * self.dir.x,
                self.pos.y + self.y * self.dir.y,
            )

    def turn_right(self):
        self.dir = self.dir.right()

    def move_forward(self):
        self.pos = self.ahead()

    def move_right(self):
        self.pos = self.p_right()
        self.dir = self.dir.right()

    def move_left(self):
        self.pos = self.p_left()
        self.dir = self.dir.left()

    def p_right(self):
        return Point(
            self.pos.x + self.dir.x + self.dir.right().x,
            self.pos.y + self.dir.y + self.dir.right().y,
        )

    def p_left(self):
        return self.pos
        # Point(self.pos.x + self.dir.x + self.dir.left().x,
        # self.pos.y + self.dir.y + self.dir.left().y)

    def __hash__(self) -> int:
        return hash((self.pos.__hash__, self.dir.__hash__))


@dataclass
class Grid:
    grid: dict[Point, str]
    height: int
    length: int
    values: Optional[dict[str, list]] = None

    def __post_init__(self) -> None:
        self.recalculate_values()

    def recalculate_values(self):
        self.values = defaultdict(list)
        for i, k in self.grid.items():
            self.values[k].append(i)

    @staticmethod
    def from_h_l(height, length):
        grid = {}
        for c in range(height):
            for i in range(length):
                grid[Point(i, c)] = "."
        return Grid(grid, c + 1, i + 1)

    @staticmethod
    def from_input(input_data):
        input = [list(chunk) for chunk in input_data]

        grid = {}
        for y in input:
            for c, x in enumerate(y):
                for i, k in enumerate(x):
                    grid[Point(i, c)] = k

        return Grid(grid, c + 1, i + 1)

    @staticmethod
    def from_grid(grid, height, length):
        return Grid(grid, height, length)

    def display(self) -> None:
        for i in range(self.height):
            line = [self.grid[Point(j, i)] for j in range(self.length)]
            print("".join(line))

    def display_param(self, grid) -> None:
        for i in range(self.height):
            line = [grid.get(Point(j, i), ".") for j in range(self.length)]
            print("".join(line))

    def items(self):
        return self.grid.items()

    def keys(self):
        return self.grid.keys()

    def has_4_in_row(self, grid):
        for i in range(self.height):
            line = [grid.get(Point(j, i), ".") for j in range(self.length)]
            if "********" in "".join(line):
                print("".join(line))
                # input()
                return True
        return False
