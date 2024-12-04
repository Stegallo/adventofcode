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
        return (lambda x,y: Mul(int(x),int(y))) (*string.replace(')','').replace('mul(', '').split(','))

    @property
    def prod(self):
        return self.op1*self.op2


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for i in self._input_data[0]]

    def _calculate_1(self):
        result = 0
        p = re.compile(r'mul\(\d{1,3}\,\d{1,3}\)')
        for j in self.__input_data:
            for i in p.findall(j.original):
                result+= Mul.from_str(i).prod
        return result

    def _calculate_2(self):
        result = 0
        p = re.compile(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)")
        do = True
        for j in self.__input_data:
            for i in p.findall(j.original):
                if i == 'do()':
                    do = True
                elif i == 'don\'t()':
                    do = False
                    continue
                elif 'mul' in i and do:
                    result+= Mul.from_str(i).prod
        return result
