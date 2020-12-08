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
        self.__accumulator = 0
        self.__instruction_count = defaultdict(int)

    def _calculate_1(self):
        self.__accumulator = 0
        self.__instruction_count.clear()
        instruction_pointer = 0
        while True:
            if self.__instruction_count[instruction_pointer] > 0:
                break
            self.__instruction_count[instruction_pointer] += 1

            current_instruction = self.__instructions[instruction_pointer]
            if current_instruction.operation == "acc":
                self.__accumulator += current_instruction.argument
                instruction_pointer += 1
            if current_instruction.operation == "jmp":
                instruction_pointer += current_instruction.argument
            if current_instruction.operation == "nop":
                instruction_pointer += 1
        return self.__accumulator

    def _calculate_2(self):
        # global ACC
        # ACC = 0
        # global INSTR
        # INSTR = defaultdict(int)
        # z = [(i.split(" ")[0], i.split(" ")[1]) for i in self._input_data]
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

            self.__accumulator = 0
            self.__instruction_count.clear()

            infinite_loop = False
            instruction_pointer = 0
            while instruction_pointer < len(local_instructions):
                val = local_instructions[instruction_pointer]

                if self.__instruction_count[instruction_pointer] > 0:
                    infinite_loop = True
                    break
                self.__instruction_count[instruction_pointer] += 1

                current_instruction = local_instructions[instruction_pointer]
                if current_instruction.operation == "acc":
                    self.__accumulator += current_instruction.argument
                    instruction_pointer += 1
                if current_instruction.operation == "jmp":
                    instruction_pointer += current_instruction.argument
                if current_instruction.operation == "nop":
                    instruction_pointer += 1
            if infinite_loop == False:
                return self.__accumulator
