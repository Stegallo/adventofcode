from pydantic.dataclasses import dataclass
from typing import List, Set
from common.aoc import AoCDay


@dataclass()
class Position:
    x: int
    y: int

    @property
    def hash(self) -> str:
        return f"x={self.x};y={self.y}"


OPERATIONS = {
    ">": Position(1, 0),
    "<": Position(-1, 0),
    "^": Position(0, 1),
    "v": Position(0, -1),
}


class Santa:
    current_position = Position(0, 0)

    def __init__(self, grid) -> None:
        self.grid: Set = grid

    def deliver_present(self, command) -> None:
        self.current_position = Position(
            self.current_position.x + OPERATIONS[command].x,
            self.current_position.y + OPERATIONS[command].y,
        )
        self.grid.add(self.current_position.hash)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self) -> None:
        self.__sequence = self._input_data[0][0]

    def initialize(self) -> None:
        self.grid: Set = {Position(0, 0).hash}

    def dispatch(self, actors: List[str]) -> int:
        santas = [Santa(self.grid) for _ in actors]
        active_santa = 0
        for command in self.__sequence:
            santas[active_santa].deliver_present(command)
            active_santa = (active_santa + 1) % len(santas)

        return len(self.grid)

    def _calculate_1(self) -> int:
        self.initialize()
        return self.dispatch(["Santa"])

    def _calculate_2(self) -> int:
        self.initialize()
        return self.dispatch(["Santa", "RoboSanta"])
