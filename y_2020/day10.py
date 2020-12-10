import re

from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(10)

    def _preprocess_input(self):
        self.__input = [int(i) for i in self._input_data]

    def _calculate_1(self):
        print(self.__input)

        y = sorted(self.__input)
        j1 = 0
        j3 = 0
        first = 0
        print(y)
        for i in range(1, len(y)):
            print(f"{y[i]=}, {y[i-1]+1=}")
            if y[i] == y[i - 1] + 1:
                print("incr1")
                j1 += 1
            else:
                print("incr3")
                j3 += 1
        print(j1 + 1)
        print(j3 + 1)
        return (j1 + 1) * (j3 + 1)

