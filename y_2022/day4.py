from typing import Set, Tuple

from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def __get_assignments(self, pair: str) -> Tuple[Set, Set]:
        r = []
        for k in pair.split(","):
            a, b = k.split("-")
            r.append(set(range(int(a), int(b) + 1)))
        return r[0], r[1]

    def _calculate_1(self):
        tot = 0
        for i in self.__input_data:
            s, t = self.__get_assignments(i)
            if s & t in [s, t]:
                tot += 1

        return tot

    def _calculate_2(self):
        x = self.__input_data
        tot = 0
        for i in x:
            s, t = self.__get_assignments(i)
            if (s & t) != set():
                tot += 1

        return tot
