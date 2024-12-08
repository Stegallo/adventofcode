from typing import Optional, Callable

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def conc(a: int, b: int) -> int:
    return int(str(a) + str(b))


@dataclass
class Row:
    original: str
    result: Optional[int] = None
    op_list: Optional[list[int]] = None

    def __post_init__(self) -> None:
        self.result = int(self.original.split(": ")[0])
        self.op_list = [int(i) for i in self.original.split(": ")[1].split(" ")]

    def do(self, lst: list[int], ops: list[Callable]) -> bool:
        if len(lst) == 1:
            return lst[0] == self.result

        return any([self.do([op(*lst[:2])] + lst[2:], ops) for op in ops])


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        return sum(x.result for x in self.__input_data if x.do(x.op_list, [add, mul]))

    def _calculate_2(self):
        return sum(
            x.result for x in self.__input_data if x.do(x.op_list, [add, mul, conc])
        )
