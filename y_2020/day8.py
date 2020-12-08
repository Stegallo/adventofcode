from .common import AoCDay
from collections import defaultdict
from typing import NamedTuple

#
# OPERATIONS= {
#
# "acc":
# "jmp":
# "nop":


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
        # self.__accumulator = 0
        # self.__instruction_count = defaultdict(int)

    def _execute(self, local_instructions=None):
        if not local_instructions:
            local_instructions = self.__instructions
        accumulator = 0
        instruction_count = defaultdict(int)

        infinite_loop = False
        instruction_pointer = 0
        while instruction_pointer < len(local_instructions):
            if instruction_count[instruction_pointer] > 0:
                infinite_loop = True
                break
            instruction_count[instruction_pointer] += 1

            current_instruction = local_instructions[instruction_pointer]
            if current_instruction.operation == "acc":
                accumulator += current_instruction.argument
                instruction_pointer += 1
            elif current_instruction.operation == "jmp":
                instruction_pointer += current_instruction.argument
            elif current_instruction.operation == "nop":
                instruction_pointer += 1
        if not infinite_loop:
            return accumulator, infinite_loop
        return accumulator, infinite_loop

    def _calculate_1(self):
        x = self._execute()
        return x[0]

    def _calculate_2(self):
        for attempt in range(len(self.__instructions)):
            local_instructions = list(self.__instructions)
            if local_instructions[attempt].operation == "nop":
                local_instructions[attempt] = Instruction(
                    "jmp", local_instructions[attempt].argument
                )
            elif local_instructions[attempt].operation == "jmp":
                local_instructions[attempt] = Instruction(
                    "nop", local_instructions[attempt].argument
                )

            x = self._execute(local_instructions)
            if not x[1]:
                return x[0]
