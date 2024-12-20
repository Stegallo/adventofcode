from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid, DIRS, Point
import math
import heapq
from collections import defaultdict


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

    def ahead(self, cursor):
        x = DIRS[cursor[1]][1]
        y = DIRS[cursor[1]][0]
        return Point(cursor[0].x + x, cursor[0].y + y)

    def move_forward(self, cursor):
        x = DIRS[cursor[1]][1]
        y = DIRS[cursor[1]][0]
        return (Point(cursor[0].x + x, cursor[0].y + y), cursor[1])

    def _calculate_1(self):
        # result = 0
        precs = defaultdict(set)
        # for x in self.__input_data:
        # ...
        x = self.grid.values["S"][0]
        # print(x)
        # visited = set()
        costs = {}
        # current_pos = x
        # current_dir =
        queue = []  # deque()
        # costs[] = 0
        # step_forward = 0
        # rotations = 0
        opposite_dir = {"^": "v", ">": "<", "v": "^", "<": ">"}

        heapq.heappush(queue, (0, (x, ">"), None))
        print("\n\n")

        while True:
            element = heapq.heappop(queue)

            # print(f"{element=}, {len(queue)=}")
            cost, cursor, prec = element
            # breakpoint()
            precs[cursor] = precs[cursor] | precs[prec]
            if prec:
                precs[cursor].add(prec)
            # breakpoint()
            # print(cursor)
            # breakpoint()
            # visited.add(cursor)
            # print(f"{cursor.pos}, {self.grid.grid.get(cursor.pos)=}, {cost}")
            # breakpoint()
            if self.grid.grid.get(cursor[0]) == "E":
                # breakpoint()
                # print(f" {len(queue)=}")
                break  # return cost

            for i in DIRS:
                if i == opposite_dir[cursor[1]]:
                    # print('not consider this')
                    continue
                elif i == cursor[1]:
                    # print('same Direction')
                    c = cursor
                    # print(f"\n{c}, {self.grid.grid.get(c.pos)=}\n")
                    if self.grid.grid.get(self.ahead(c)) == "#":
                        continue
                    c = self.move_forward(c)
                    move_cost = 1
                    if costs.get(cursor, 0) + move_cost <= costs.get(c, math.inf):
                        costs[c] = costs.get(cursor, 0) + move_cost
                        heapq.heappush(queue, (cost + move_cost, c, cursor))
                else:
                    # print('rotate 90')
                    c = (cursor[0], i)
                    if self.grid.grid.get(self.ahead(c)) == "#":
                        continue
                    # print(f"\n{c}, {self.grid.grid.get(c.pos)=}\n")
                    move_cost = 1000
                    if costs.get(cursor, 0) + move_cost <= costs.get(c, math.inf):
                        costs[c] = costs.get(cursor, 0) + move_cost
                        heapq.heappush(queue, (cost + move_cost, c, cursor))

                # print(cursor.dir.icon, i)
            # print(*queue, sep="\n")
            # print(costs)
            # input()
            # break
        # print(precs)
        # max = 0
        # for k,v in precs.items():
        #     print(k, len(v), v)
        #     if len(v)>max:
        #         max = len(v)
        # print(max)
        self.grid.display()

        return len(set(i[0] for i in precs[cursor])) + 1
        return cost

    def _calculate_2(self):
        result = 0
        return result
