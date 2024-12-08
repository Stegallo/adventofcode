from common.aoc import AoCDay
from common.grid import Grid


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

    def _anti2(self, a, b, i, include) -> list:
        x = []
        start = 0 if include else 1
        for i in range(start, i):
            x.append((a[0] - i * (b[0] - a[0]), a[1] - i * (b[1] - a[1])))
            x.append((b[0] + i * (b[0] - a[0]), b[1] + i * (b[1] - a[1])))
        return x

    def _common(self, i, include):
        antin = {}
        antennas = {k: v for k, v in self.grid.values.items() if k != "."}
        for j in antennas.values():
            for x in range(len(j)):
                for y in range(len(j)):
                    if j[x] == j[y]:
                        continue
                    ants = self._anti2(j[x], j[y], i, include)
                    for m in ants:
                        antin[m] = "O"

        result = sum(bool(antin.get(i)) for i in self.grid.keys())
        return result

    def _calculate_1(self):
        return self._common(2, False)

    def _calculate_2(self):
        return self._common(100, True)
