from typing import Any, Dict, List, Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.utilities import bitand, bitnot, bitor, lshift, rshift

OPERATORS: Dict[str, Any] = {
    "NOT": bitnot,
    "AND": bitand,
    "OR": bitor,
    "LSHIFT": lshift,
    "RSHIFT": rshift,
}


@dataclass
class Operator:
    source: str
    inputs: List[str]


@dataclass
class Element:
    source: str
    operator: Optional[Operator] = None
    cached_result: Optional[int] = None

    def __post_init__(self) -> None:
        for i in list(OPERATORS.keys()):
            if i in self.source:
                self.operator = Operator(
                    i,
                    [x for x in self.source.replace(" ", "").split(i) if x],
                )

    def __compute_result(self, wires) -> int:
        if self.operator:
            inputs = [
                int(i) if i.isnumeric() else wires[i].resolve(wires)
                for i in self.operator.inputs
            ]
            return OPERATORS[self.operator.source](*inputs)
        if self.source.isnumeric():
            return int(self.source)
        return wires[self.source].resolve(wires)

    def resolve(self, wires) -> int:
        if not self.cached_result:
            self.cached_result = self.__compute_result(wires)
        return self.cached_result


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
        wires = {x.target: Element(x.source) for x in self.__input_data}

        return wires["a"].resolve(wires)

    def _calculate_2(self):
        wires = {
            x.target: Element("46065") if x.target == "b" else Element(x.source)
            for x in self.__input_data
        }

        return wires["a"].resolve(wires)
