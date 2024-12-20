from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid, Cursor, Direction, DIRS
import math
import heapq


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
        # self.__input_data = [Row(i) for j in self._input_data for i in j]
        # for x in self.__input_data:
        #     print(f"{x}")

    def _calculate_1(self):
        result = 0
        # for x in self.__input_data:
        # ...
        x = self.grid.values["S"][0]
        # print(x)
        visited = set()
        costs = {}
        # current_pos = x
        # current_dir =
        queue = []  # deque()
        # costs[] = 0
        # step_forward = 0
        # rotations = 0
        opposite_dir = {"^": "v", ">": "<", "v": "^", "<": ">"}

        heapq.heappush(queue, (0, Cursor(x, Direction.from_symbol(">"))))
        print("\n\n")

        while True:
            element = heapq.heappop(queue)

            print(f"{element=}, {len(queue)=}")
            cost, cursor = element
            visited.add(cursor)
            print(f"{cursor.pos}, {self.grid.grid.get(cursor.pos)=}, {cost}")
            # breakpoint()
            if self.grid.grid.get(cursor.pos) == "E":
                print(f" {len(queue)=}")
                return cost

            for i in DIRS:
                if i == opposite_dir[cursor.dir.icon]:
                    # print('not consider this')
                    continue
                elif i == cursor.dir.icon:
                    # print('same Direction')
                    c = Cursor(cursor.pos, cursor.dir)
                    # print(f"\n{c}, {self.grid.grid.get(c.pos)=}\n")
                    if self.grid.grid.get(c.ahead()) == "#":
                        continue
                    c.move_forward()
                    move_cost = 1
                    if costs.get(cursor, 0) + move_cost < costs.get(c, math.inf):
                        costs[c] = costs.get(cursor, 0) + move_cost
                        heapq.heappush(queue, (cost + move_cost, c))
                else:
                    # print('rotate 90')
                    c = Cursor(cursor.pos, Direction.from_symbol(i))
                    if self.grid.grid.get(c.ahead()) == "#":
                        continue
                    # print(f"\n{c}, {self.grid.grid.get(c.pos)=}\n")
                    move_cost = 1000
                    if (
                        costs.get(cursor, 0) + move_cost < costs.get(c, math.inf)
                        and c not in visited
                    ):
                        costs[c] = costs.get(cursor, 0) + move_cost
                        heapq.heappush(queue, (cost + move_cost, c))

                # print(cursor.dir.icon, i)
            # print(*queue, sep="\n")
            # print(costs)
            # input()
            # break

        return result

    def _calculate_2(self):
        result = 0
        return result
