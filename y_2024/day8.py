from typing import Optional

from pydantic.dataclasses import dataclass
from collections import defaultdict
from common.aoc import AoCDay


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


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

    def _anti2(self, a, b, i, include) -> list:
        x = []
        start = 0 if include else 1
        for i in range(start, i):
            x.extend(
                (
                    (a[0] - i * (b[0] - a[0]), a[1] - i * (b[1] - a[1])),
                    (b[0] + i * (b[0] - a[0]), b[1] + i * (b[1] - a[1])),
                )
            )
        return x

    def _common(self, i, include):
        antin = {}
        antennas = {k: v for k, v in self.grid.values.items() if k != "."}
        for j in antennas.values():
            for x in range(len(j)):
                for y in range(len(j)):
                    if j[x] == j[y]:
                        continue
                    ants = self._anti2(j[x], j[y], i, include)
                    for m in ants:
                        antin[m] = "O"

        return sum(bool(antin.get(i)) for i in self.grid.keys())

    def _calculate_1(self):
        return self._common(2, False)

    def _calculate_2(self):
        return self._common(100, True)
