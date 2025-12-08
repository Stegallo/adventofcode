from functools import lru_cache

from common.aoc import AoCDay
from common.grid import Cursor, Direction, Grid, Point


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)

    def _calculate_1(self):
        result = 0
        s = self.grid.values["S"][0]
        next_row = set([s])
        for _ in range(self.grid.height):
            beams = [i for i in next_row]
            if not beams:
                break

            next_row = set()
            for p in beams:
                b = Cursor(p, Direction.from_symbol("v"))
                if self.grid.grid.get(b.ahead()) == ".":
                    next_row.add(b.ahead())
                if self.grid.grid.get(b.ahead()) == "^":
                    result += 1
                    next_row.add(Point(b.ahead().x - 1, b.ahead().y))
                    next_row.add(Point(b.ahead().x + 1, b.ahead().y))
        return result

    @lru_cache()
    def possible_routes(self, c_str: str) -> int:
        c = Cursor.deserialize(c_str)
        if c.ahead().y >= self.grid.height:
            return 1

        if self.grid.grid.get(c.ahead()) == "^":
            return self.possible_routes(
                Cursor(
                    Point(c.ahead().x - 1, c.ahead().y), Direction.from_symbol("v")
                ).serialize()
            ) + self.possible_routes(
                Cursor(
                    Point(c.ahead().x + 1, c.ahead().y), Direction.from_symbol("v")
                ).serialize()
            )
        else:
            return self.possible_routes(
                Cursor(c.ahead(), Direction.from_symbol("v")).serialize()
            )

    def _calculate_2(self):
        s = self.grid.values["S"][0]
        p = Cursor(s, Direction.from_symbol("v"))
        return self.possible_routes(p.serialize())
