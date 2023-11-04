from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass()
class Position:
    x: int
    y: int

    @property
    def hash(self):
        return f"x={self.x};y={self.y}"


@dataclass
class Santa:
    sequence: str
    current_position = Position(0, 0)

    def set_grid(self, grid):
        self.grid = grid

    def deliver_presents(self):
        for i in self.sequence:
            if i == "<":
                self.current_position = Position(
                    self.current_position.x - 1, self.current_position.y
                )

            elif i == ">":
                self.current_position = Position(
                    self.current_position.x + 1, self.current_position.y
                )
            elif i == "^":
                self.current_position = Position(
                    self.current_position.x, self.current_position.y + 1
                )
            elif i == "v":
                self.current_position = Position(
                    self.current_position.x, self.current_position.y - 1
                )

            if self.current_position.hash not in self.grid:
                self.grid.add(self.current_position.hash)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__santa = Santa(self._input_data[0][0])
        self.__real_santa = Santa(
            "".join([i for c, i in enumerate(self._input_data[0][0]) if c % 2 == 0])
        )
        self.__robo_santa = Santa(
            "".join([i for c, i in enumerate(self._input_data[0][0]) if c % 2 != 0])
        )

    def _calculate_1(self):
        grid = {Position(0, 0).hash}
        self.__santa.set_grid(grid)
        self.__santa.deliver_presents()
        return len(self._Day__santa.grid)

    def _calculate_2(self):
        grid = {Position(0, 0).hash}
        self.__real_santa.set_grid(grid)
        self.__robo_santa.set_grid(grid)
        self.__real_santa.deliver_presents()
        self.__robo_santa.deliver_presents()
        return len(grid)
