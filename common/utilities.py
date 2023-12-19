from typing import Dict, List, Optional, Tuple

from pydantic.dataclasses import dataclass
from math import inf

def bitand(x: int, y: int) -> int:
    return x & y


def bitor(x: int, y: int) -> int:
    return x | y


def lshift(x: int, y: int) -> int:
    return x << y


def rshift(x: int, y: int) -> int:
    return x >> y


def bitnot(x: int) -> int:
    return x ^ 65535


@dataclass
class Grid:
    original: List[str]
    grid: Optional[Dict[Tuple[int, int], str]] = None
    row_num: Optional[int] = None
    col_num: Optional[int] = None

    def __post_init__(self) -> None:
        self.grid = {}
        self.row_num = len(self.original)
        self.col_num = len(self.original[0])
        for y, t in enumerate(self.original):
            for x, u in enumerate(t):
                self.grid[(x, y)] = u

    @property
    def rows(self) -> List[str]:
        return [
            "".join([self.grid[(x, y)] for x in range(self.col_num)])  # type: ignore
            for y in range(self.row_num)  # type: ignore
        ]

    @property
    def dia1(self) -> List[str]:
        result = []
        for k in range(self.col_num+self.row_num-1):
            # print((self.col_num+self.row_num)//2)
            p = k+1-max(self.col_num,self.row_num)
            r = []
            for i in range(self.col_num+self.row_num-1):
                # print(f"{k=}, {i=}, {p=}")
                # print(f"{i+p,i}, \t\t{i=}, {p=}, {(i+p,i)=}, {k=}, {i=}")
                try:
                    r.append(self.grid[(i+p,i)])
                    # print(f", \t\t{self.grid[(i+p,i)]}")
                except:
                    ...

            result.append(''.join(r))
            # print()
        return result

    @property
    def dia2(self) -> List[str]:
        return []


    @property
    def cols(self) -> List[str]:
        return [
            "".join([self.grid[(x, y)] for y in range(self.row_num)])  # type: ignore
            for x in range(self.col_num)  # type: ignore
        ]

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.grid.items())))  # type: ignore

    def viz(self) -> None:
        for i in self.rows:
            print(i)

    @staticmethod
    def from_grid(grid, frame=0):
        max_c = -inf
        max_r = -inf
        min_c = inf
        min_r = inf
        for i in grid:
            # print(i)
            if i[0] > max_c:
                max_c = i[0]
            if i[1] > max_r:
                max_r = i[1]
            if i[0] < min_c:
                min_c = i[0]
            if i[1] < min_r:
                min_r = i[1]

        # print(f"{min_c=}, {min_r=}, {max_c=}, {max_r=}")
        c = []
        for y in range(max_r-min_r+1+2*frame):
            r = []
            for x in range(max_c-min_c+1+2*frame):
                r.append(grid.get((-1*frame+x,-1*frame+y), '.'))
            # print(f"here: {''.join(r)}")
            c.append(''.join(r))
        return Grid(c)
