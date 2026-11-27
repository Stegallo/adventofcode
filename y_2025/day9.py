from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import DIRS, Cursor, Direction, Grid, Point

# from math import dist


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = tuple(int(i) for i in self.original.split(","))


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        # print(f"{len(self._input_data)=}")
        # print(f"{len(self._input_data[0])=}")
        # self.grid = Grid.from_input(self._input_data)
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data = [Row(i) for j in self._input_data for i in j]
        # hh = 0
        # ll = 0
        # for x in self.__input_data:
        #     # print(f"{x}")
        #     hh =  max(hh, int(x.processed[1]))
        #     ll =  max(ll, int(x.processed[0]))
        # # print(f"{hh=}, {ll=}")
        # self.grid = Grid.from_h_l(hh+2, ll+3)
        # for x in self.__input_data:
        #     # print(Point(int(x.processed[0]), int(x.processed[1])))
        #     self.grid.grid[ Point(int(x.processed[0]), int(x.processed[1])) ] = "#"
        # self.grid.display()

    def _calculate_1(self):
        # result = 0
        # for x in self.__input_data:
        # print(x.processed)
        # max_dist = 0
        # max_t = None
        max_a = 0
        for i in range(len(self.__input_data[:-1])):
            for j in range(i + 1, len(self.__input_data)):
                ll = self.__input_data[i].processed
                mm = self.__input_data[j].processed
                max_a = max(max_a, (abs(ll[0] - mm[0]) + 1) * (abs(ll[1] - mm[1]) + 1))
                # print(ll ,mm, dist(ll, mm))
        #         if dist(ll, mm) > max_dist:
        #             max_dist =  dist(ll, mm)
        #             max_t = (ll, mm)
        # print(max_t[0], max_t[1])
        # return (abs(max_t[0][0] - max_t[1][0])+1) * (abs(max_t[0][1] - max_t[1][1])+1)
        return max_a
        # 4735136763

    def _calculate_2(self):
        # result = 0
        xs = []
        ys = []
        for i in self.__input_data:
            # print(i.processed[0])
            xs.append(i.processed[0])
            ys.append(i.processed[1])
        print(len(xs), len(ys))
        print(xs, ys)
        uxs = sorted(set(xs))
        uys = sorted(set(ys))
        print(uxs, uys)
        mx = {v: i + 1 for i, v in enumerate(uxs)}
        my = {v: i + 1 for i, v in enumerate(uys)}
        print(mx, my)
        # for i in self.__input_data:
        #     mx[]
        g = Grid.from_h_l(len(uys) + 2, len(uxs) + 2)
        for i in self.__input_data:
            g.grid[Point(mx[i.processed[0]], my[i.processed[1]])] = "#"
        for i in self.__input_data:
            p = Point(mx[i.processed[0]], my[i.processed[1]])
            for j in DIRS:
                c = Cursor(p, Direction.from_symbol(j))
                # print(f"{c.ahead()=}")
                path = []
                border = False
                while c.ahead() in g.grid:
                    path.append(c.ahead())
                    if g.grid[c.ahead()] == "#":
                        border = True
                        break
                    c.move_forward()
                    # print(c.pos)
                if border:
                    for k in path:
                        if g.grid[k] != "#":
                            g.grid[k] = "x"
            # g.display()
            print()
        # g.display()
        for i in range(len(uys) + 2):
            for j in range(len(uxs) + 2):
                if g.grid[Point(j, i)] in [".", "0"]:
                    g.grid[Point(j, i)] = "0"
                else:
                    break
        for i in range(len(uys) + 2):
            for j in range(len(uxs) + 2):
                if g.grid[Point(len(uxs) + 1 - j, i)] in [".", "0"]:
                    g.grid[Point(len(uxs) + 1 - j, i)] = "0"
                else:
                    break
        for j in range(len(uxs) + 2):
            for i in range(len(uys) + 2):
                if g.grid[Point(j, i)] in [".", "0"]:
                    g.grid[Point(j, i)] = "0"
                else:
                    break
        for j in range(len(uxs) + 2):
            for i in range(len(uys) + 2):
                if g.grid[Point(j, len(uys) + 1 - i)] in [".", "0"]:
                    g.grid[Point(j, len(uys) + 1 - i)] = "0"
                else:
                    break
        g.display()
        max_a = 0
        for i in range(len(self.__input_data[:-1])):
            for j in range(i + 1, len(self.__input_data)):
                ll = self.__input_data[i].processed
                mm = self.__input_data[j].processed
                if ll[0] == mm[0] or ll[1] == mm[1]:
                    continue
                mll = mx[ll[0]], my[ll[1]]
                mmm = mx[mm[0]], my[mm[1]]

                bx = min(mll[0], mmm[0])
                ex = max(mll[0], mmm[0])
                by = min(mll[1], mmm[1])
                ey = max(mll[1], mmm[1])
                try:
                    for v in range(by, ey + 1):
                        for u in range(bx, ex + 1):
                            if g.grid[Point(u, v)] == "0":
                                raise
                except:  # noqa: E722
                    continue
                # breakpoint()
                max_a = max(max_a, (abs(ll[0] - mm[0]) + 1) * (abs(ll[1] - mm[1]) + 1))
        return max_a
