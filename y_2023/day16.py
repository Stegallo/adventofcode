from typing import Optional
import time
from pydantic.dataclasses import dataclass

from common.aoc import AoCDay

from common.utilities import Grid

# @dataclass
# class Row:
#     original: str
#     processed: Optional[str] = None
#
#     def __post_init__(self) -> None:
#         self.processed = ""  # self.original

ENERGY = set()
X = None
C=0
VISITED = set()
@dataclass
class Beam:
    grid: Grid

    def move(self, curr_pos = (0,0), dir = (1,0)) -> None:
        try:
            x = self.grid.grid[curr_pos]
            # print(f"{curr_pos=}, {self.grid.grid[curr_pos]=}, {dir=}")
        except:
            return
        global C
        while True:
            if (curr_pos, dir) in VISITED:
                break
            VISITED.add((curr_pos, dir))
            # if C>105:
            #     break
            # time.sleep(.5)
            C+=1
            ENERGY.add(curr_pos)
            tile = self.grid.grid[curr_pos]
            if tile == '.':
                curr_pos = curr_pos[0]+dir[0], curr_pos[1]+dir[1]

            if tile == '|':
                # continue
                if dir in [(1,0), (-1,0)]:
                    # print("split")
                    bup = Beam(self.grid)
                    dir_up = (0,-1)
                    bup.move((curr_pos[0]+dir_up[0], curr_pos[1]+dir_up[1]), dir_up)

                    bdown = Beam(self.grid)
                    dir_down = (0,1)
                    bdown.move((curr_pos[0]+dir_down[0], curr_pos[1]+dir_down[1]), dir_down)
                    break
                if dir in [(0, 1), (0, -1)]:
                    curr_pos = curr_pos[0]+dir[0], curr_pos[1]+dir[1]

            if tile == '-':
                # continue
                if dir in [(1,0), (-1,0)]:
                    curr_pos = curr_pos[0]+dir[0], curr_pos[1]+dir[1]
                if dir in [(0, 1), (0, -1)]:
                    # print("split")
                    bright = Beam(self.grid)
                    dir_right = (1,0)
                    bright.move((curr_pos[0]+dir_right[0], curr_pos[1]+dir_right[1]), dir_right)

                    bleft = Beam(self.grid)
                    dir_left = (-1,0)
                    bleft.move((curr_pos[0]+dir_left[0], curr_pos[1]+dir_left[1]), dir_left)
                    break

            if tile == '\\':
                if dir == (1,0):
                    dir = (0,1)
                elif dir == (-1,0):
                    dir = (0,-1)
                elif dir == (0,1):
                    dir = (1,0)
                elif dir == (0,-1):
                    dir = (-1,0)

                curr_pos = curr_pos[0]+dir[0], curr_pos[1]+dir[1]

            if tile == '/':
                # print(f"{dir=}")
                if dir == (1,0):
                    dir = (0,-1)
                elif dir == (-1,0):
                    dir = (0,1)
                elif dir == (0,1):
                    dir = (-1,0)
                elif dir == (0,-1):
                    dir = (1,0)

                curr_pos = curr_pos[0]+dir[0], curr_pos[1]+dir[1]
                # print(f"{curr_pos=}, {dir=}")
            try:
                # print(f"{curr_pos=}, {self.grid.grid[curr_pos]}")
                x = self.grid.grid[curr_pos]
            except:
                return
            # y = Grid(X)
            # y.grid = {i:'#' for i in ENERGY}
            # y.grid[curr_pos] = 'O'
            # for x in y.rows:
            #         print(f"{x}")


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = Grid(self._input_data[0])
        global X
        X = self._input_data[0]

    def _calculate_1(self):
        # for x in self.__input_data.rows:
        #     print(f"{x}")
        b = Beam(self.__input_data)
        b.move()
        y = Grid(self._input_data[0])
        # y.grid = {i:'#' for i in ENERGY}
        # for x in y.rows:
        #         print(f"{x}")
        return len(ENERGY)


    def _calculate_2(self):
        result = 0
        global ENERGY
        global X
        global C
        global VISITED

        b = Beam(self.__input_data)

        for r in range(b.grid.row_num):
            for d in [(1,0), (0,1), (0,-1)]:
                ENERGY = set()
                X = None
                C=0
                VISITED = set()
                b.move((0, r), d)
                if len(ENERGY) > result:
                    result = len(ENERGY)
            for d in [(-1,0), (0,-1), (0,1)]:
                ENERGY = set()
                X = None
                C=0
                VISITED = set()
                b.move((b.grid.row_num-1, r), d)
                if len(ENERGY) > result:
                    result = len(ENERGY)

        for c in range(b.grid.col_num):
            for d in [(1,0), (-1,0), (0, 1)]:
                ENERGY = set()
                X = None
                C=0
                VISITED = set()
                b.move((c, 0), d)
                if len(ENERGY) > result:
                    result = len(ENERGY)
            for d in [(1,0), (-1,0), (0, -1)]:
                ENERGY = set()
                X = None
                C=0
                VISITED = set()
                b.move((c, b.grid.col_num-1), d)
                if len(ENERGY) > result:
                    result = len(ENERGY)
        # for i in range(self.__input_data.row_num):
        #     for d in
        return result
