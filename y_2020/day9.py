import re

from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(9)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def _calculate_1(self):
        info(self._input_data)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        self.__input
        return 0

    def _calculate_2(self):
        self.__input
        return 0


def info(x):
    print(f"{type(x)=}, {len(x)=}")
    hf = len(x) // 2 + 1
    try:
        print(f"{x[+0]=}")
        print(f"{x[hf]=}")
        print(f"{x[-1]=}")
    except:
        ...

    # regex = "([\d]+)-([\d]+) ([\D]): ([\D]*)$"
    # fa = re.findall(regex, x[0])[0]
    # # print(*fa, sep="\n")
