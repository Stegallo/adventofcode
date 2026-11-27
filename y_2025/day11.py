from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from functools import lru_cache
from frozendict import frozendict


@dataclass
class Row:
    original: str
    p1: Optional[str] = None
    p2: Optional[list] = None

    def __post_init__(self) -> None:
        self.p1 = self.original.split(" ")[0][:-1]
        self.p2 = self.original.split(" ")[1:]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        # print(f"{len(self._input_data)=}")
        # print(f"{len(self._input_data[0])=}")
        # self.grid = Grid.from_input(self._input_data)
        # self.grid.display()
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data = [Row(i) for j in self._input_data for i in j]
        # for x in self.__input_data:
        #     print(f"{x}")

    def _calculate_1(self):
        result = 0
        return 0
        d = {}
        for x in self.__input_data:
            d[x.p1] = x.p2
        print(d)

        def search(s, d):
            if s == "out":
                return 1
            rez = 0
            for i in d[s]:
                rez += search(i, d)
                # print(i)
            return rez

        s = "you"
        return search(s, d)
        return result

    def _calculate_2(self):
        result = 0
        d = {}
        for x in self.__input_data:
            d[x.p1] = tuple(x.p2)
        print(d)
        d = frozendict(d)

        @lru_cache(maxsize=None)
        def search(s, d, end):
            # print(path)
            # path = list(path)
            if s == end:
                return 1
                # if 'dac' in path and 'fft' in path:
                #     return 1
                # else:
                #     return 0
            if s == "out":
                return 0
            rez = 0
            for i in d[s]:
                rez += search(i, d, end)
            return rez

        s = "svr"
        return search(s, d, "dac") * search("dac", d, "fft") * search(
            "fft",
            d,
            "out",
        ) + search(s, d, "fft") * search("fft", d, "dac") * search("dac", d, "out")
        return result
