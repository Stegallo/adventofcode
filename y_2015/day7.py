from pydantic.dataclasses import dataclass
from common.aoc import AoCDay
from typing import Optional, List, Dict, Any


def bitand(x, y) -> int:
    return x & y


def bitor(x, y) -> int:
    return x | y


def lshift(x, y) -> int:
    return x << y


def rshift(x, y) -> int:
    return x >> y


def bitnot(x) -> int:
    return x ^ 65535


BIN_OPERATORS = {"AND": bitand, "OR": bitor, "LSHIFT": lshift, "RSHIFT": rshift}
UN_OPERATORS = {"NOT": bitnot}
OPERATORS: Dict[str, Any] = {
    "NOT": bitnot,
    "AND": bitand,
    "OR": bitor,
    "LSHIFT": lshift,
    "RSHIFT": rshift,
}


@dataclass
class Element:
    source: str
    is_operator: bool = False
    operator: Optional[str] = None
    inputs: Optional[List[str]] = None
    result: int = 0
    result_valid: bool = False

    def __post_init__(self) -> None:
        self.is_operator = any([o in self.source for o in list(OPERATORS.keys())])
        for i in list(OPERATORS.keys()):
            if i in self.source:
                self.operator = i
        if self.is_operator:
            self.inputs = [
                x for x in self.source.replace(" ", "").split(self.operator) if x
            ]

    def resolve(self, wires) -> int:
        if self.result_valid:
            return self.result
        if not self.is_operator:
            if self.source.isnumeric():
                self.result = int(self.source)
                self.result_valid = True
            else:
                self.result = wires[self.source].resolve(wires)
                self.result_valid = True

        else:
            inputs = [x for x in self.source.replace(" ", "").split(self.operator) if x]

            inputs = [
                int(i) if i.isnumeric() else wires[i].resolve(wires) for i in inputs
            ]

            self.result = OPERATORS[str(self.operator)](*inputs)
            self.result_valid = True
        return self.result


@dataclass
class Instruction:
    source: str
    target: str


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [
            Instruction(*list(i.split(" -> "))) for i in self._input_data[0]
        ]

    def _calculate_1(self):
        wires = {}
        for x in self.__input_data:
            wires[x.target] = Element(x.source)

        return wires["a"].resolve(wires)

    def _calculate_2(self):
        wires = {}
        for x in self.__input_data:
            if x.target == "b":
                wires[x.target] = Element("46065")
            else:
                wires[x.target] = Element(x.source)

        return wires["a"].resolve(wires)
