from common.aoc import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [[i for i in chunk] for chunk in self._input_data]
        self.grid = {}
        for y in self.__input_data:
            for c, x in enumerate(y):
                for i, k in enumerate(x):
                    self.grid[(c, i)] = k

    def _calculate_1(self):
        result = 0
        for y in self.__input_data:
            for c, x in enumerate(y):
                for i, k in enumerate(x):
                    if k != "X":
                        continue
                    left = (c, i - 1)
                    r = (c, i + 1)
                    u = (c - 1, i)
                    d = (c + 1, i)
                    lu = (c - 1, i - 1)
                    ru = (c - 1, i + 1)
                    ld = (c + 1, i - 1)
                    rd = (c + 1, i + 1)
                    if self.grid.get(left) == "M":
                        if self.grid.get((c, i - 2)) == "A":
                            if self.grid.get((c, i - 3)) == "S":
                                result += 1
                    if self.grid.get(r) == "M":
                        if self.grid.get((c, i + 2)) == "A":
                            if self.grid.get((c, i + 3)) == "S":
                                result += 1
                    if self.grid.get(u) == "M":
                        if self.grid.get((c - 2, i)) == "A":
                            if self.grid.get((c - 3, i)) == "S":
                                result += 1
                    if self.grid.get(d) == "M":
                        if self.grid.get((c + 2, i)) == "A":
                            if self.grid.get((c + 3, i)) == "S":
                                result += 1
                    if self.grid.get(lu) == "M":
                        if self.grid.get((c - 2, i - 2)) == "A":
                            if self.grid.get((c - 3, i - 3)) == "S":
                                result += 1
                    if self.grid.get(ru) == "M":
                        if self.grid.get((c - 2, i + 2)) == "A":
                            if self.grid.get((c - 3, i + 3)) == "S":
                                result += 1
                    if self.grid.get(ld) == "M":
                        if self.grid.get((c + 2, i - 2)) == "A":
                            if self.grid.get((c + 3, i - 3)) == "S":
                                result += 1
                    if self.grid.get(rd) == "M":
                        if self.grid.get((c + 2, i + 2)) == "A":
                            if self.grid.get((c + 3, i + 3)) == "S":
                                result += 1
        return result

    def _calculate_2(self):
        result = 0
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
