from typing import Optional, List, Any, Tuple

from pydantic.dataclasses import dataclass
from functools import lru_cache

from common.aoc import AoCDay
from common.utilities import Grid
# @dataclass
# class Grido:
#     original: List[str]
#     grid: Optional[Any] = None
#     row_num: Optional[int] = None
#     col_num: Optional[int] = None
#
#     def __post_init__(self) -> None:
#         self.grid = {}
#         self.row_num = len(self.original)
#         self.col_num = len(self.original[0])
#         for y, t in enumerate(self.original):
#             for x, u in enumerate(t):
#                 self.grid[(x,y)] = u
#
#     @property
#     def rows(self):
#         result = []
#         for y in range(self.row_num):
#             interm = []
#             for x in range(self.col_num):
#                 interm.append(self.grid[(x,y)])
#             result.append(''.join(interm))
#         return result
#
#     @property
#     def cols(self):
#         result = []
#         for x in range(self.col_num):
#             interm = []
#             for y in range(self.row_num):
#                 interm.append(self.grid[(x,y)])
#             result.append(''.join(interm))
#         return result
#
#     def __hash__(self):
#         return hash(tuple(self.original))

#
# @dataclass
# class Row:
#     original: str
#     processed: Optional[str] = None
#
#     def __post_init__(self) -> None:
#         self.processed = ""  # self.original

@lru_cache
def tilt_n(grid):
    new_input = []
    for x in grid.cols:
        col = []
        space=0
        for y in x:
            if y == 'O':
                col.append(y)
            if y == '.':
                space+=1
            if y == '#':
                col.append('.'*space+y)
                space=0
        col.append('.'*space)
        new_input.append(''.join(col))
    return Grid(new_input)

@lru_cache
def tilt_w(grid):
    # rows and cols are flipped !!!
    new_input = []
    for x in grid.cols:
        col = []
        space=0
        for y in x:
            if y == 'O':
                col.append(y)
            if y == '.':
                space+=1
            if y == '#':
                col.append('.'*space+y)
                space=0
        col.append('.'*space)
        new_input.append(''.join(col))
    return Grid(new_input)

@lru_cache
def tilt_s(grid):
    new_input = []
    for x in grid.cols:
        col = []
        space=0
        for y in x[::-1]:
            if y == 'O':
                col.append(y)
            if y == '.':
                space+=1
            if y == '#':
                col.append('.'*space+y)
                space=0
        col.append('.'*space)
        # print(f"{x=}, {x[::-1]}, {col=}")
        new_input.append(''.join(col))
    return Grid(new_input)

@lru_cache
def tilt_e(grid):
    # rows and cols are flipped !!!
    new_input = []
    # print(grid.cols[::-1])
    for x in grid.cols[::-1]:
        col = []
        space=0
        zero=0
        # print(f"{x=}")
        for y in x:
            if y == 'O':
                zero+=1
            if y == '.':
                col.append(y)
            if y == '#':
                col.append('O'*zero+y)
                zero=0
        col.append('O'*zero)
        # print(f"{x=}, {col=}")
        new_input.append(''.join(col))
    return Grid(new_input)

def cycle(grid, times):
    new_grid = grid
    seen = set()
    seen_locs = []
    repeat = None
    remaining = None
    for i in range(times):
        # detecs cycle
        if new_grid.__hash__() in seen:
            # in case of already seen waits for the next one to mesure length
            seen = {new_grid.__hash__()}
            seen_locs.append(i)
            if len(seen_locs)>1:
                # calculate how many steps to get to desired number of iters
                remaining = (times-i)%(seen_locs[1]-seen_locs[0])
                break
        else:
            seen.add(new_grid.__hash__())
        new_grid = tilt_n(new_grid)
        # for i in new_grid.cols:
        #     print(i)
        # print()
        new_grid = tilt_w(new_grid)
        # for i in new_grid.rows:
        #     print(i)
        # print()
        new_grid = tilt_s(new_grid)
        # for i in new_grid.cols[::-1]:
        #     print(i)
        # print()
        new_grid = tilt_e(new_grid)
        # for i in new_grid.rows:
            # print(i)
        # print()

    for i in range(remaining):
        # remaining number of iterations
        new_grid = tilt_n(new_grid)
        new_grid = tilt_w(new_grid)
        new_grid = tilt_s(new_grid)
        new_grid = tilt_e(new_grid)
    return new_grid

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = Grid(self._input_data[0])

    def _calculate_1(self):
        new_grid = tilt_n(self.__input_data)

        result = 0
        for c, x in enumerate(new_grid.cols):
            # print(x, new_grid.col_num-c, sum(1 for i in x if i == 'O'))
            result+=((new_grid.col_num-c) * sum(1 for i in x if i == 'O'))
        return result

    def _calculate_2(self):
        N_LOOP = 1_000_000_000
        # N_LOOP = 1_000_000
        # N_LOOP = 1_000
        new_grid = cycle(self.__input_data, N_LOOP)
        result = 0
        for c, x in enumerate(new_grid.rows):
            print(x, new_grid.row_num-c, sum(1 for i in x if i == 'O'))
            result+=((new_grid.row_num-c) * sum(1 for i in x if i == 'O'))
        return result
