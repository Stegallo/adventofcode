from collections import defaultdict
from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import DIRS, Cursor, Direction, Grid, Point


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original


ASSINGED_REGION: dict[Point, str] = {}


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _area(self):
        return

    def _perim(self):
        return

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

    def next_char(self, c):
        return chr(ord(c) + 1)

    def navigate(self, x):
        # print(f"{ASSINGED_REGION=}")
        # if x in ASSINGED_REGION:
        #     return
        for i in DIRS:
            cur = Cursor(x, Direction.from_symbol(i))
            # print(f"{i=}, {cur}")
            if (
                self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x)
                and cur.ahead() not in ASSINGED_REGION
            ):
                ASSINGED_REGION[cur.ahead()] = ASSINGED_REGION[x]
                self.navigate(cur.ahead())

    def _calculate_1(self):
        visited = set()
        result = 0

        reg_n = 0
        for x in self.grid.grid.keys():
            if x in ASSINGED_REGION:
                ...

            else:
                reg_n += 1
                ASSINGED_REGION[x] = reg_n
                visited.add(self.grid.grid.get(x))

            self.navigate(x)

        region_grid = Grid.from_grid(
            {k: str(ASSINGED_REGION[k]) for k, v in self.grid.grid.items()},
            self.grid.height,
            self.grid.length,
        )
        region_grid.display()

        perims = defaultdict(list)
        for k, v in region_grid.items():
            for i in DIRS:
                cur = Cursor(k, Direction.from_symbol(i))

                if self.grid.grid.get(cur.ahead(), "*") != self.grid.grid.get(k):
                    perims[v].append("*")

        result = 0
        for k, v in region_grid.values.items():
            result += len(v) * len(perims[k])

        return result

    def _calculate_2(self):
        visited = set()
        result = 0

        reg_n = 0
        for x in self.grid.grid.keys():
            if x in ASSINGED_REGION:
                ...
            else:
                reg_n += 1
                ASSINGED_REGION[x] = reg_n
                visited.add(self.grid.grid.get(x))

            self.navigate(x)

        region_grid = Grid.from_grid(
            {k: str(ASSINGED_REGION[k]) for k, v in self.grid.grid.items()},
            self.grid.height,
            self.grid.length,
        )

        perims = defaultdict(list)

        sides = {}
        for k, v in region_grid.items():
            temp = []
            for i in DIRS:
                cur = Cursor(k, Direction.from_symbol(i))
                if self.grid.grid.get(cur.ahead(), "*") != self.grid.grid.get(k):
                    temp.append(cur)
            perims[v].extend(temp)

        sides = {}
        for k, v in perims.items():
            reduced_v = []
            for i in v:
                if i.dir.y == 0:
                    reduced_v.append(i)

            vicini_potenziali = {}  # defaultdict(list)
            vicini_potenziali_bound = {}
            print(f"{len(reduced_v)=}")

            for i in reduced_v:
                vicini_potenziali[i] = []
                vicini_potenziali_bound[i] = i.pos.y

                for j in reduced_v:
                    if i == j:
                        continue

                    if i.dir != j.dir:
                        continue
                    if i.pos.x != j.pos.x:
                        continue
                    vicini_potenziali[i].append(j)
                    vicini_potenziali_bound[i] = i.pos.y

            for kk, vvv in vicini_potenziali.items():
                vv = sorted(vvv, key=lambda x: x.pos.y)
                for j in vv:
                    if vicini_potenziali_bound[kk] + 1 == j.pos.y:
                        vicini_potenziali_bound[kk] = j.pos.y
            tmp = set(
                (k.pos.x, v, k.dir.icon) for k, v in vicini_potenziali_bound.items()
            )
            sides[k] = 2 * (len(tmp))

        result = 0
        for k, v in region_grid.values.items():
            result += len(v) * sides[k]

        return result
