from common.aoc import AoCDay

DIRS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
RIGHT = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


class Day(AoCDay):
    _visited_in_1: set[tuple[int]] = set()

    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [[i for i in chunk] for chunk in self._input_data]
        self.grid = {}
        for y in self.__input_data:
            for c, x in enumerate(y):
                for i, k in enumerate(x):
                    self.grid[(c, i)] = k
                    if k in DIRS:
                        self.starting_point = (c, i)

    def _calculate_1(self) -> int:
        grid = {k: v for k, v in self.grid.items()}
        position = self.starting_point
        direction = DIRS[self.grid[self.starting_point]]
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
            new_grid = {k: v for k, v in self.grid.items()}
            new_grid[i] = "#"
            result += self.run_in_circe(new_grid)
        return result

    def run_in_circe(self, grid) -> bool:
        grid = {k: v for k, v in grid.items()}
        position = self.starting_point
        direction = DIRS[self.grid[self.starting_point]]
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
