from common.aoc import AoCDay
from common.grid import Grid


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

    def _get_antinodes(self, a, b, i, include) -> list:
        x: list = []
        dist = (b[0] - a[0]), (b[1] - a[1])
        start = 0 if include else 1
        for i in range(start, i):
            x.extend(
                (
                    (a[0] - i * dist[0], a[1] - i * dist[1]),
                    (b[0] + i * dist[0], b[1] + i * dist[1]),
                ),
            )
        return x

    def _common(self, i, include):
        antin = set()
        antennas = {k: v for k, v in self.grid.values.items() if k != "."}
        for j in antennas.values():
            for x in range(len(j)):
                for y in range(len(j)):
                    if j[x] == j[y]:
                        continue
                    ants = self._get_antinodes(j[x], j[y], i, include)
                    for m in ants:
                        antin.add(m)

        return sum(bool(i in antin) for i in self.grid.keys())

    def _calculate_1(self):
        return self._common(2, False)

    def _calculate_2(self):
        return self._common(100, True)
