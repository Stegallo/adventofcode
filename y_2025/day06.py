from math import prod
from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid, Point


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = " ".join(self.original.split()).split(" ")


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for j in self._input_data for i in j]
        self.grid = Grid.from_input(self._input_data)

    def _calculate_1(self):
        result = 0
        for i in range(len(self.__input_data[-1].processed)):
            op = self.__input_data[-1].processed[i]

            if op == "+":
                result += sum(int(x.processed[i]) for x in self.__input_data[:-1])

            elif op == "*":
                result += prod(int(x.processed[i]) for x in self.__input_data[:-1])

        return result

    def _calculate_2(self):
        result = 0

        block_op = None
        for i in range(self.grid.length):
            line = [
                self.grid.grid.get(Point(i, j), ".")
                for j in range(self.grid.height - 1)
            ]
            op = self.grid.grid.get(Point(i, self.grid.height - 1), ".")
            if op != " ":
                block_op = op
                if op == "+":
                    rez = 0
                elif op == "*":
                    rez = 1

            if "".join(line).strip() != "":
                if block_op == "+":
                    rez += int("".join(line))
                elif block_op == "*":
                    rez *= int("".join(line))
            else:
                result += rez

        return result + rez
