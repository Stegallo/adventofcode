from collections import defaultdict

from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def __get_priority(self, char: str) -> int:
        k = ord(char)
        if k <= 122 and k >= 97:
            return k - 96
        return k - 64 + 26 if k <= 90 and k >= 65 else 0

    def _calculate_1(self):
        x = self.__input_data
        t = 0
        for i in x:
            a = set(i[: len(i) // 2])
            b = set(i[len(i) // 2 :])
            k = list(a & (b))[0]
            t += self.__get_priority(k)
        return t

    def _calculate_2(self):
        x = self.__input_data
        d = defaultdict(list)
        t = 0
        for c, i in enumerate(x):
            d[c // 3].append(i)
        for i in d.values():
            k = list(set(i[0]) & set(i[1]) & set(i[2]))[0]
            t += self.__get_priority(k)
        return t
