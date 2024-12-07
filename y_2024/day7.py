from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


OPS = [add, mul]


@dataclass
class Row:
    original: str
    result: Optional[int] = None
    op_list: Optional[list[int]] = None

    def __post_init__(self) -> None:
        self.result = int(self.original.split(": ")[0])
        self.op_list = [int(i) for i in self.original.split(": ")[1].split(" ")]

    def do1(self, lst):
        if len(lst) == 1:
            if lst[0] == self.result:
                return True
            return False
        op1 = lst[0]
        op2 = lst[1]

        # A
        la = [op1 * op2]
        la.extend(lst[2:])

        a = self.do1(la)

        # B
        lb = [op1 + op2]
        lb.extend(lst[2:])

        b = self.do1(lb)

        if a or b:
            return True
        return False

    def do2(self, lst):
        if len(lst) == 1:
            if lst[0] == self.result:
                return True
            return False
        op1 = lst[0]
        op2 = lst[1]

        # A
        la = [op1 * op2]
        la.extend(lst[2:])

        a = self.do2(la)

        # B
        lb = [op1 + op2]
        lb.extend(lst[2:])

        b = self.do2(lb)

        # C
        lc = [int(str(op1) + str(op2))]
        # print("{lc}")
        lc.extend(lst[2:])

        c = self.do2(lc)

        if a or b or c:
            return True
        return False

    def solve1(self):
        return self.do1(self.op_list)

    def solve2(self):
        return self.do2(self.op_list)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        print(f"{self._input_data=}")
        print(f"{len(self._input_data)=}")
        print(f"{len(self._input_data[0])=}")
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        result = 0
        for x in self.__input_data:
            # print(x)
            # print(f"{x.result}, {x.op_list}, {len(x.op_list)}")
            if x.solve1():
                # print(x)
                result += x.result
        return result

    def _calculate_2(self):
        result = 0
        for x in self.__input_data:
            # print(x)
            # print(f"{x.result}, {x.op_list}, {len(x.op_list)}")
            if x.solve2():
                # print(x)
                result += x.result
        return result
