from typing import Optional

from pydantic.dataclasses import dataclass
from collections import deque
from common.aoc import AoCDay
from common.grid import Grid, Cursor, DIRS, Direction


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
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        result = 0

        for i in self.grid.values["0"]:
            visited = set()
            frontier = deque()
            for j in DIRS:
                cur = Cursor(i, Direction.from_symbol(j))

                if (
                    self.grid.grid.get(cur.ahead())
                    and int(self.grid.grid.get(cur.ahead()))
                    - int(self.grid.grid.get(i))
                    == 1
                ):
                    frontier.append(cur.ahead())

            while len(frontier) > 0:
                k = frontier.popleft()

                if self.grid.grid.get(k) == "9":
                    visited.add(k)
                    continue

                for j in DIRS:
                    cur = Cursor(k, Direction.from_symbol(j))

                    if (
                        self.grid.grid.get(cur.ahead())
                        and int(self.grid.grid.get(cur.ahead()))
                        - int(self.grid.grid.get(k))
                        == 1
                    ):
                        frontier.append(cur.ahead())

            result += len(visited)

        return result

    def _calculate_2(self):
        result = 0
        for i in self.grid.values["0"]:
            visited = 0
            frontier = deque()
            for j in DIRS:
                cur = Cursor(i, Direction.from_symbol(j))

                if (
                    self.grid.grid.get(cur.ahead())
                    and int(self.grid.grid.get(cur.ahead()))
                    - int(self.grid.grid.get(i))
                    == 1
                ):
                    frontier.append(cur.ahead())

            while len(frontier) > 0:
                k = frontier.popleft()

                if self.grid.grid.get(k) == "9":
                    visited += 1

                for j in DIRS:
                    cur = Cursor(k, Direction.from_symbol(j))
                    if (
                        self.grid.grid.get(cur.ahead())
                        and int(self.grid.grid.get(cur.ahead()))
                        - int(self.grid.grid.get(k))
                        == 1
                    ):
                        frontier.append(cur.ahead())

            result += visited

        return result
