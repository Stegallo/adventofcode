from typing import Optional, List, Tuple, Dict

from pydantic.dataclasses import dataclass


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
            "".join([self.grid[(x, y)] for x in range(self.col_num)]) for y in range(self.row_num)  # type: ignore # noqa: E501
        ]

    @property
    def cols(self) -> List[str]:
        return [
            "".join([self.grid[(x, y)] for y in range(self.row_num)]) for x in range(self.col_num)  # type: ignore # noqa: E501
        ]

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.grid.items())))  # type: ignore
