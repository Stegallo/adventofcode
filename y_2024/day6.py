from common.aoc import AoCDay
from common.grid import Grid

DIRS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
RIGHT = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


class Day(AoCDay):
    _visited_in_1: set[tuple[int]] = set()

    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()
        for i in DIRS:
            if i in self.grid.values:
                self.starting_point = self.grid.values[i][0]
                break

    def _calculate_1(self) -> int:
        grid = dict(self.grid.items())
        position = self.starting_point
        direction = DIRS[grid[self.starting_point]]
        grid[position] = "X"
        self._visited_in_1.add(position)
        while True:
            adhead = (position[0] + direction[0], position[1] + direction[1])
            try:
                if grid[adhead] == "#":  # obstacle:
                    direction = RIGHT[direction]
                else:
                    position = adhead
                    grid[position] = "X"
                    self._visited_in_1.add(position)
            except KeyError:
                break
        return sum(1 for i in grid.values() if i == "X")

    def _calculate_2(self) -> int:
        result = 0
        for i in self._visited_in_1 - {self.starting_point}:
            grid = dict(self.grid.items())
            grid[i] = "#"
            result += self.run_in_circle(grid)
        return result

    def run_in_circle(self, grid) -> bool:
        grid = dict(grid.items())
        position = self.starting_point
        direction = DIRS[grid[self.starting_point]]
        visited = {}
        while True:
            visited[(position, direction)] = True
            adhead = (position[0] + direction[0], position[1] + direction[1])
            try:
                if grid[adhead] == "#":  # obstacle:
                    direction = RIGHT[direction]
                else:
                    position = adhead
                if (position, direction) in visited:
                    return True
            except KeyError:
                break
        return False
