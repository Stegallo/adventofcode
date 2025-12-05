from common.aoc import AoCDay
from common.grid import Grid


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

    def _calculate_1(self):
        result = 0
        for k, v in self.grid.items():
            if v == "@" and (
                sum(1 if self.grid.grid.get(y) == "@" else 0 for y in k.crown()) <= 3
            ):
                result += 1

        return result

    def _calculate_2(self):
        result = 0
        while True:
            removed = False
            for k, v in self.grid.items():
                if (
                    v == "@"
                    and sum(1 if self.grid.grid.get(y) == "@" else 0 for y in k.crown())
                    <= 3
                ):
                    result += 1
                    removed = True
                    self.grid.grid[k] = "x"
            if not removed:
                break
        return result
