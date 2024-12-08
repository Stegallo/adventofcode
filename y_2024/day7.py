from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def conc(a, b):
    return int(str(a) + str(b))


OPS = [add, mul]


@dataclass
class Row:
    original: str
    result: Optional[int] = None
    op_list: Optional[list[int]] = None

    def __post_init__(self) -> None:
        self.result = int(self.original.split(": ")[0])
        self.op_list = [int(i) for i in self.original.split(": ")[1].split(" ")]

    def do(self, lst, ops):
        if len(lst) == 1:
            if lst[0] == self.result:
                return True
            return False

        op1 = lst[0]
        op2 = lst[1]

        rex = []
        for i in ops:
            l_i = [i(op1, op2)]
            l_i.extend(lst[2:])
            rex.append(self.do(l_i, ops))
        if any(rex):
            return True
        return False


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        print(f"{self._input_data=}")
        print(f"{len(self._input_data)=}")
        print(f"{len(self._input_data[0])=}")
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        result = 0
        for x in self.__input_data:
            if x.do(x.op_list, [add, mul]):
                result += x.result
        return result

    def _calculate_2(self):
        result = 0
        for x in self.__input_data:
            if x.do(x.op_list, [add, mul, conc]):
                result += x.result
        return result
