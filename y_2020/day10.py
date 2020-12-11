from .common import AoCDay
from collections import defaultdict


class Day(AoCDay):
    def __init__(self):
        super().__init__(10)

    def _preprocess_input(self):
        self.__input = [int(i) for i in self._input_data]

    def _calculate_1(self):
        y = sorted(self.__input)
        j1 = 0
        j3 = 0
        for i in range(1, len(y)):
            if y[i] == y[i - 1] + 1:
                j1 += 1
            else:
                j3 += 1
        return (j1 + 1) * (j3 + 1)

    def _calculate_2(self):
        y = sorted(self.__input)
        y = [0] + y + [y[-1] + 3]
        d = defaultdict(int)
        counter = 1
        for i in range(1, len(y)):
            contiguous = y[i] == y[i - 1] + 1
            if contiguous:
                counter += 1
            else:
                d[counter] += 1
                counter = 1
        res = 1
        for i in d:
            x = 1
            if i >= 5:
                x = (2 ** (i - 2) - 1) ** d[i]
            elif i > 2:
                x = (2 ** (i - 2)) ** d[i]
            res *= x
        return res
