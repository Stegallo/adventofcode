from collections import defaultdict
from typing import NamedTuple

from .common import AoCDay


class Operation(NamedTuple):
    acc_action: callable
    move_action: callable


OPERATIONS = {
    "acc": Operation(lambda x: x, lambda x: 1),
    "jmp": Operation(lambda x: 0, lambda x: x),
    "nop": Operation(lambda x: 0, lambda x: 1),
}


class Instruction(NamedTuple):
    operation: str
    argument: int


class Day(AoCDay):
    def __init__(self):
        super().__init__(8)

    def _preprocess_input(self):
        self.__instructions = [
            Instruction(i.split(" ")[0], int((i.split(" "))[1]))
            for i in self._input_data
        ]

    def _execute(self, local_instructions=None):
        if not local_instructions:
            local_instructions = self.__instructions
        accumulator = 0
        instruction_count = defaultdict(int)

        infinite_loop = False
        instr_pointer = 0
        while instr_pointer < len(local_instructions):
            if instruction_count[instr_pointer] > 0:
                infinite_loop = True
                break
            instruction_count[instr_pointer] += 1

            curr_instruction = local_instructions[instr_pointer]
            accumulator += OPERATIONS[curr_instruction.operation].acc_action(
                curr_instruction.argument
            )
            instr_pointer += OPERATIONS[curr_instruction.operation].move_action(
                curr_instruction.argument
            )

        if not infinite_loop:
            return accumulator, infinite_loop
        return accumulator, infinite_loop

    def _calculate_1(self):
        execution_result = self._execute()
        return execution_result[0]

    def _calculate_2(self):
        for attempt in range(len(self.__instructions)):
            local_instructions = list(self.__instructions)
            local_instructions[attempt] = self.__swap(local_instructions[attempt])
            execution_result = self._execute(local_instructions)
            if not execution_result[1]:
                return execution_result[0]

    @staticmethod
    def __swap(instruction: Instruction):
        if instruction.operation == "nop":
            return Instruction("jmp", instruction.argument)
        if instruction.operation == "jmp":
            return Instruction("nop", instruction.argument)
        return instruction
