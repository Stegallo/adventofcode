from common.aoc import AoCDay
from common.grid import Grid, Cursor, Direction, Point

DIRS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
RIGHT = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


class Day(AoCDay):
    _visited_in_1: set[Point] = set()

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
        direction = Direction(
            *DIRS[grid[self.starting_point]],
            grid[self.starting_point],
        )
        curs = Cursor(position, direction)
        grid[position] = "X"
        self._visited_in_1.add(position)
        while True:
            adhead = curs.ahead()
            try:
                if grid[adhead] == "#":  # obstacle:
                    curs.turn_right()
                else:
                    curs.move_forward()
                    grid[curs.pos] = "X"
                    self._visited_in_1.add(curs.pos)
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
        direction = Direction(
            *DIRS[grid[self.starting_point]],
            grid[self.starting_point],
        )
        curs = Cursor(position, direction)
        visited = {}
        while True:
            visited[(curs.pos, curs.dir)] = True
            adhead = curs.ahead()
            try:
                if grid[adhead] == "#":  # obstacle:
                    curs.turn_right()
                else:
                    curs.move_forward()
                if (curs.pos, curs.dir) in visited:
                    return True
            except KeyError:
                break
        return False
