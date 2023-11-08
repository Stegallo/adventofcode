import re
from typing import Dict, Optional, Self

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Command:
    circuit: str
    result: Optional[int] = None

    @property
    def operator(self) -> Optional[str]:
        r = re.search(r"(NOT|AND|OR|LSHIFT|RSHIFT)", self.circuit)
        if r:
            return r.groups()[0]
        return None

    @property
    def inputs(self):
        if not self.operator:
            return [self.circuit]
        if self.operator == "NOT":
            return self.circuit.split(" ")[1:2]
        if self.operator in ("AND", "OR"):
            return self.circuit.replace("AND", "#").replace("OR", "#").split(" # ")
        if "SHIFT" in self.operator:
            return self.circuit.replace(" R", " ").replace(" L", " ").split(" SHIFT ")
        return []

    def operate(self, wires: Dict[str, Self]):
        if self.result:
            return self.result
        if not self.operator:
            if self.inputs[0].isnumeric():
                op1 = self.inputs[0]
            else:
                op1 = wires[self.inputs[0]].operate(wires)
            self.result = op1
        if self.operator == "NOT":
            if self.inputs[0].isnumeric():
                op1 = self.inputs[0]
            else:
                op1 = wires[self.inputs[0]].operate(wires)
            self.result = op1 ^ 65535
        if self.operator == "AND":
            if self.inputs[0].isnumeric():
                op1 = self.inputs[0]
            else:
                op1 = wires[self.inputs[0]].operate(wires)
            if self.inputs[1].isnumeric():
                op2 = self.inputs[1]
            else:
                op2 = wires[self.inputs[1]].operate(wires)
            self.result = int(op1) & int(op2)
        if self.operator == "OR":
            if self.inputs[0].isnumeric():
                op1 = self.inputs[0]
            else:
                op1 = wires[self.inputs[0]].operate(wires)
            if self.inputs[1].isnumeric():
                op2 = self.inputs[1]
            else:
                op2 = wires[self.inputs[1]].operate(wires)
            self.result = int(op1) | int(op2)
        if self.operator == "LSHIFT":
            if self.inputs[0].isnumeric():
                op1 = self.inputs[0]
            else:
                op1 = wires[self.inputs[0]].operate(wires)
            if self.inputs[1].isnumeric():
                op2 = self.inputs[1]
            else:
                op2 = wires[self.inputs[1]].operate(wires)
            self.result = int(op1) << int(op2)
        if self.operator == "RSHIFT":
            if self.inputs[0].isnumeric():
                op1 = self.inputs[0]
            else:
                op1 = wires[self.inputs[0]].operate(wires)
            if self.inputs[1].isnumeric():
                op2 = self.inputs[1]
            else:
                op2 = wires[self.inputs[1]].operate(wires)
            self.result = int(op1) >> int(op2)

        return self.result


@dataclass
class Instruction:
    command_str: str
    destination: str

    @property
    def command(self):
        return Command(self.command_str)


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
            wires[x.destination] = x.command

        return wires["a"].operate(wires)

    def _calculate_2(self):
        wires = {}
        for x in self.__input_data:
            if x.destination == "b":
                wires[x.destination] = Command("46065")
            else:
                wires[x.destination] = x.command

        return wires["a"].operate(wires)
