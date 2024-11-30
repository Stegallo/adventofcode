from typing import Optional, List, Any
import copy
from pydantic.dataclasses import dataclass

from common.aoc import AoCDay

@dataclass
class Grid:
    original: List[str]
    grid: Optional[Any] = None
    row_num: Optional[int] = None
    col_num: Optional[int] = None
    original_vertical_mirror: Any = None
    original_orizontal_mirror: Any = None

    def __post_init__(self) -> None:
        self.grid = {}
        self.row_num = len(self.original)
        self.col_num = len(self.original[0])
        for y, t in enumerate(self.original):
            for x, u in enumerate(t):
                self.grid[(x,y)] = u

    @property
    def rows(self):
        result = []
        for y in range(self.row_num):
            interm = []
            for x in range(self.col_num):
                interm.append(self.grid[(x,y)])
            result.append(''.join(interm))
        return result

    @property
    def cols(self):
        result = []
        for x in range(self.col_num):
            interm = []
            for y in range(self.row_num):
                interm.append(self.grid[(x,y)])
            result.append(''.join(interm))
        return result

    def flip(self, index):
        clone_grid = {k: v for k,v in self.grid.items()}
        local_copy = copy.deepcopy(self)
        flipped_value = '.' if self.grid[index] == '#' else '#'
        clone_grid[index] = flipped_value
        local_copy.grid = clone_grid
        return local_copy

    def find_mirr(self, part=None):
        possible_m_r = []
        possible_m_c = []
        for i in range(self.row_num-1):
            if self.rows[i] == self.rows[i+1]:
                possible_m_r.append((i, i+1))

        for j in range(self.col_num-1):
            if self.cols[j] == self.cols[j+1]:
                possible_m_c.append((j, j+1))



        vertical_cols = 0
        for i, j in possible_m_c:
            if (i, j) == self.original_vertical_mirror:
                continue
            a,b=i,j
            while True:
                if a<0 or b>=self.col_num:
                    # print('vertical mirrow!')
                    if not part:
                        self.original_vertical_mirror = (i,j)
                    vertical_cols = i+1
                    break
                if self.cols[a] != self.cols[b]:
                    # print('No vertical mirror')
                    break
                a = a-1
                b=b+1


        orizontal_rows = 0
        for i, j in possible_m_r:
            if (i, j) == self.original_orizontal_mirror:
                continue
            a,b=i,j
            while True:
                if a<0 or b>=self.row_num:
                    # print('orizontal mirrow!')
                    if not part:
                        self.original_orizontal_mirror = (i,j)
                    orizontal_rows = i+1
                    break
                if self.rows[a] != self.rows[b]:
                    # print('No orizontal mirror')
                    break
                a = a-1
                b=b+1


        return orizontal_rows*100+vertical_cols

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.new_grids = [Grid(i) for i in self._input_data]


    def _calculate_1(self): # 34202
        result = 0
        for x in self.new_grids:
            result+=x.find_mirr()
        return result


    def _calculate_2(self): # 34230
        result = 0
        for g in self.new_grids:
            found = False
            for y in range(g.row_num):
                for x in range(g.col_num):
                    flipped_g = g.flip((x,y))
                    rez=flipped_g.find_mirr(part=2)
                    if rez:
                        result+=rez
                        found = True
                    if found:
                        break
                if found:
                    break

        return result
