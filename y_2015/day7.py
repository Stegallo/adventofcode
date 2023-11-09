import re
from pprint import pprint
from typing import List, Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


def bitand(x, y):
    return x & y


def bitor(x, y):
    return x | y


def lshift(x, y):
    return x << y


def rshift(x, y):
    return x >> y


def bitnot(x):
    return x ^ 65535


BIN_OPERATORS = {"AND": bitand, "OR": bitor, "LSHIFT": lshift, "RSHIFT": rshift}
UN_OPERATORS = {"NOT": bitnot}


class Ingress:
    @staticmethod
    def extract_opcode(source: str) -> Optional[str]:
        r = re.search(r"(NOT|AND|OR|LSHIFT|RSHIFT)", source)
        if r:
            return r.groups()[0]
        return None

    @staticmethod
    def extract_inputs(source: str, opcode: Optional[str]) -> List[str]:
        if not opcode:
            return [source]
        if opcode == "NOT":
            return [source.replace("NOT ", "")]
        return source.replace(opcode, "").split("  ")

    def __init__(self, source) -> None:
        self.opcode: Optional[str] = self.extract_opcode(source)
        self.inputs: List[str] = self.extract_inputs(source, self.opcode)
        self.result: Optional[int] = None
        if self.inputs[0].isnumeric():
            self.result = int(self.inputs[0])

    def __repr__(self):
        return (
            f"Ingress(opcode={self.opcode}, inputs={self.inputs}, result={self.result})"
        )

    def __eq__(self, other):
        if isinstance(other, Ingress):
            return self.opcode == other.opcode and self.inputs == other.inputs
        return False

    @property
    def value(self):
        return self.result

    def resolve(self, wires):
        # print(self)
        if not self.opcode:
            if self.inputs[0].isnumeric():
                self.result = int(self.inputs[0])
                return self
            return wires[self.inputs[0]].resolve(wires)
        if self.opcode in UN_OPERATORS:
            if self.inputs[0].isnumeric():
                op1 = int(self.inputs[0])
            else:
                op1 = wires[self.inputs[0]].resolve(wires).value
            return Ingress(str(UN_OPERATORS[self.opcode](op1)))
        if self.opcode in BIN_OPERATORS:
            if self.inputs[0].isnumeric():
                op1 = int(self.inputs[0])
            else:
                op1 = wires[self.inputs[0]].resolve(wires).value
            if self.inputs[1].isnumeric():
                op2 = int(self.inputs[1])
            else:
                op2 = wires[self.inputs[1]].resolve(wires).value
            return Ingress(str(BIN_OPERATORS[self.opcode](op1, op2)))
        return 1 / 0


@dataclass
class Instruction:
    source: str
    target: str
    ingress: Optional[Ingress] = None

    def __post_init__(self):
        # transforms source in an Ingress object
        self.ingress = Ingress(self.source)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [
            Instruction(
                *list(re.search(r"(.*) -> (\D*)", i).groups()),
            )
            for i in self._input_data[0]
        ]

    def _calculate_1(self):
        wires = {}
        for x in self.__input_data:
            wires[x.target] = x.ingress

        pprint(wires)
        # for x in self.__input_data:
        #     print(x.target)
        #     wires[x.target] = wires[x.target].resolve(wires)
        # pprint(wires)
        wires["a"].resolve(wires).value
        return 0  # wires["a"].resolve(wires).value

    def _calculate_2(self):
        return 0
        wires = {}
        for x in self.__input_data:
            if x.target == "b":
                wires[x.target] = Ingress("46065")
            else:
                wires[x.target] = x.ingress
        #
        return wires["a"].resolve(wires).value
