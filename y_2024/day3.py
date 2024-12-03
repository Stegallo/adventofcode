from typing import Optional
import re
from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    # processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original

@dataclass
class Mul:
    op1: int
    op2: int

    @staticmethod
    def from_str(string):
        x,y =string.replace(')','').replace('mul(', '').split(',')
        return Mul(int(x), int(y))

    @property
    def mult(self):
        return self.op1*self.op2


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for i in self._input_data[0]]

    def _calculate_1(self):
        r = 0
        p = re.compile(r'mul\(\d\d?\d?\,\d\d?\d?\)')
        for j in self.__input_data:
            for i in p.findall(j.original):
                r+= Mul.from_str(i).mult
        return r

    def _calculate_2(self):
        r = 0
        p = re.compile(r"mul\(\d\d?\d?\,\d\d?\d?\)|do\(\)|don't\(\)")
        do = True
        for j in self.__input_data:
            for i in p.findall(j.original):
                if i == 'do()':
                    do = True
                    continue
                if i == 'don\'t()':
                    do = False
                    continue
                if 'mul' in i and do:
                    r+= Mul.from_str(i).mult
        return r
