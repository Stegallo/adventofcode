from typing import Optional

from pydantic.dataclasses import dataclass
from collections import defaultdict


@dataclass
class Grid:
    grid: dict[tuple[int, int], str]
    height: int
    length: int
    values: Optional[dict[str, list]] = None

    def __post_init__(self) -> None:
        self.values = defaultdict(list)
        for i, k in self.grid.items():
            self.values[k].append(i)

    @staticmethod
    def from_input(input_data):
        input = [[i for i in chunk] for chunk in input_data]

        grid = {}
        for y in input:
            for c, x in enumerate(y):
                for i, k in enumerate(x):
                    grid[(c, i)] = k

        return Grid(grid, c + 1, i + 1)

    def display(self) -> None:
        for i in range(self.height):
            line = []
            for j in range(self.length):
                line.append(self.grid[(i, j)])
            print("".join(line))

    def items(self):
        return self.grid.items()

    def keys(self):
        return self.grid.keys()
