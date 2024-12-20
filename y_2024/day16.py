from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid, Cursor, Direction, DIRS
import math


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
        print(x)
        visited = set()
        costs = {}
        # current_pos = x
        # current_dir =
        queue = []  # deque()
        # costs[] = 0
        # step_forward = 0
        # rotations = 0
        opposite_dir = {"^": "v", ">": "<", "v": "^", "<": ">"}
        current_cur = Cursor(x, Direction.from_symbol(">"))
        print("\n\n")
        while True:
            # print(f"{current_cur=}")
            # breakpoint()
            for i in DIRS:
                # print(current_cur.dir.icon, i)
                # continue
                if i == opposite_dir[current_cur.dir.icon]:
                    # print('not consider this')
                    continue
                c = Cursor(current_cur.pos, Direction.from_symbol(i))
                c.move_forward()
                # print(f"{c.pos=}, {self.grid.grid[c.pos]=}")
                if self.grid.grid[c.pos] == "#":
                    continue

                # breakpoint()
                move_cost = 1 if current_cur.dir.icon == i else 1001
                # print(move_cost)
                if self.grid.grid[c.pos] == "E":
                    # return
                    return costs[current_cur] + move_cost
                # continue
                # breakpoint()

                if costs.get(current_cur, 0) + move_cost < costs.get(c, math.inf):
                    costs[c] = costs.get(current_cur, 0) + move_cost
                    # self.grid.grid[current_pos] = str(costs[current_pos])
                # c.move_forward()
                if c not in visited:
                    queue.append(c)
                # print(f"{i}, {costs}, {c.ahead()=}, {len(queue)=}, {queue=}")
                # print(f"{i}, {costs}, {len(queue)=}, {queue=}")
            # break
            # input()
            # breakpoint()
            min = math.inf
            min_index = None
            for c, i in enumerate(queue):
                # print(i, costs[i])
                if costs[i] < min:
                    min = costs[i]
                    min_index = c
                    current_cur = i
            visited.add(current_cur)
            # print(f"before pop left: {queue}")
            queue = queue[:min_index] + queue[min_index + 1 :]
            print(f"{len(queue)=}")
            # print(f"after pop left: {queue}")
            # print("\n\n")
            # current_cur.move_forward()
            # breakpoint()
            # current_cur = queue.popleft()
            # current_pos = current_cur.pos
            # current_dir = current_cur.dir
            # self.grid.display()
            # break
        return result

    def _calculate_2(self):
        result = 0
        return result
