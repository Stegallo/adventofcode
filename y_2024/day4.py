from common.aoc import AoCDay
from common.grid import Grid, DIRS_8, Cursor, Direction


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

    def _calculate_1(self):
        result = 0
        for value in self.grid.values:
            if value != "X":
                continue
            for pos in self.grid.values[value]:
                for dir in DIRS_8:
                    cur = Cursor(pos, Direction.from_symbol8(dir))
                    if self.grid.grid.get(cur.ahead()) == "M":
                        cur1 = Cursor(cur.ahead(), Direction.from_symbol8(dir))
                        if self.grid.grid.get(cur1.ahead()) == "A":
                            cur2 = Cursor(cur1.ahead(), Direction.from_symbol8(dir))
                            if self.grid.grid.get(cur2.ahead()) == "S":
                                result += 1

        return result

    def _calculate_2(self):
        result = 0
        dirs_x = {k: v for k, v in DIRS_8.items() if k in ["1", "7", "L", "J"]}
        # print(dirs_x)
        for value in self.grid.values:
            if value != "X":
                continue
            for pos in self.grid.values[value]:
                ones = {}
                for dir in dirs_x:
                    cur = Cursor(pos, Direction.from_symbol8(dir))
                    ones[cur.dir.icon] = self.grid.grid.get(cur.ahead())
                print(ones)
                if (
                    ones["1"] == "M"
                    and ones["L"] == "S"
                    and ones["7"] == "M"
                    and ones["J"] == "S"
                ):
                    result += 1
                if (
                    ones["1"] == "S"
                    and ones["L"] == "M"
                    and ones["7"] == "S"
                    and ones["J"] == "M"
                ):
                    result += 1

                if (
                    ones["1"] == "M"
                    and ones["L"] == "S"
                    and ones["7"] == "S"
                    and ones["J"] == "M"
                ):
                    result += 1
                if (
                    ones["1"] == "S"
                    and ones["L"] == "M"
                    and ones["7"] == "M"
                    and ones["J"] == "S"
                ):
                    result += 1
        result = 0
        return result
        for y in self.__input_data:
            for c, x in enumerate(y):
                for i, k in enumerate(x):
                    if k != "A":
                        continue
                    lu = (c - 1, i - 1)
                    ru = (c - 1, i + 1)
                    ld = (c + 1, i - 1)
                    rd = (c + 1, i + 1)

                    if (
                        self.grid.get(lu) == "M"
                        and self.grid.get(rd) == "S"
                        and self.grid.get(ru) == "M"
                        and self.grid.get(ld) == "S"
                    ):
                        result += 1

                    if (
                        self.grid.get(lu) == "S"
                        and self.grid.get(rd) == "M"
                        and self.grid.get(ru) == "S"
                        and self.grid.get(ld) == "M"
                    ):
                        result += 1

                    if (
                        self.grid.get(lu) == "M"
                        and self.grid.get(rd) == "S"
                        and self.grid.get(ru) == "S"
                        and self.grid.get(ld) == "M"
                    ):
                        result += 1

                    if (
                        self.grid.get(lu) == "S"
                        and self.grid.get(rd) == "M"
                        and self.grid.get(ru) == "M"
                        and self.grid.get(ld) == "S"
                    ):
                        result += 1
        return result
