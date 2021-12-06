from dataclasses import dataclass
from typing import List
from .common import AoCDay

COMMANDS_1 = {
    "forward": lambda amount, position: Position(
        position.horizontal_position + amount, position.depth
    ),
    "down": lambda amount, position: Position(
        position.horizontal_position, position.depth + amount
    ),
    "up": lambda amount, position: Position(
        position.horizontal_position, position.depth - amount
    ),
}

COMMANDS_2 = {
    "forward": lambda amount, position: Position(
        position.horizontal_position + amount,
        position.depth + position.aim * amount,
        position.aim,
    ),
    "down": lambda amount, position: Position(
        position.horizontal_position, position.depth, position.aim + amount
    ),
    "up": lambda amount, position: Position(
        position.horizontal_position, position.depth, position.aim - amount
    ),
}


@dataclass
class Position:
    horizontal_position: int
    depth: int
    aim: int = 0


@dataclass
class Command:
    move: int
    amount: int

    @staticmethod
    def from_instruction(instruction: List):
        return Command(instruction[0], int(instruction[1]))


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data

    def _calculate_1(self):
        instructions = self.__input_data
        position = Position(0, 0)
        for instruction in instructions:
            command = Command.from_instruction(instruction.split(" "))
            position = COMMANDS_1[command.move](command.amount, position)

        return position.horizontal_position * position.depth

    def _calculate_2(self):
        instructions = self.__input_data
        position = Position(0, 0, 0)
        for instruction in instructions:
            command = Command.from_instruction(instruction.split(" "))
            position = COMMANDS_2[command.move](command.amount, position)

        return position.horizontal_position * position.depth
