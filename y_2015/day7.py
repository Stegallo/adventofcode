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

    result: int = 0
    result_valid: bool = False

    def __post_init__(self) -> None:
        if any(o in self.source for o in list(OPERATORS.keys())):
            for i in list(OPERATORS.keys()):
                if i in self.source:
                    self.operator = Operator(
                        i,
                        [x for x in self.source.replace(" ", "").split(i) if x],
                    )

    def resolve(self, wires) -> int:
        if self.result_valid:
            return self.result
        if not self.operator:
            if self.source.isnumeric():
                self.result = int(self.source)
                self.result_valid = True
            else:
                self.result = wires[self.source].resolve(wires)
                self.result_valid = True

        else:
            inputs = [
                int(i) if i.isnumeric() else wires[i].resolve(wires)
                for i in self.operator.inputs
            ]

            self.result = OPERATORS[self.operator.source](*inputs)
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
        wires = {x.target: Element(x.source) for x in self.__input_data}

        return wires["a"].resolve(wires)

    def _calculate_2(self):
        wires = {
            x.target: Element("46065") if x.target == "b" else Element(x.source)
            for x in self.__input_data
        }

        return wires["a"].resolve(wires)
