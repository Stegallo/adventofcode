from typing import Optional

from pydantic.dataclasses import dataclass
from itertools import combinations

from common.aoc import AoCDay

REPETITIONS = 1000000 - 1


@dataclass
class Row:
    original: str
    processed: Optional[str] = None
    has_galaxy: Optional[bool] = False

    def __post_init__(self) -> None:
        self.processed = self.original
        self.has_galaxy = "#" in self.original


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = [Row(i) for i in self._input_data[0]]

    def short_path(self, i):
        # print(self.columns)
        # print(self.__input_data)
        # print(i)
        st, en = i
        # print(st[0], st[1], en[0], en[1])
        max_y = max(st[1], en[1])
        max_x = max(st[0], en[0])

        min_y = min(st[1], en[1])
        min_x = min(st[0], en[0])

        columns_to_cross = []
        for c, i in enumerate(self.columns):
            if not i:
                # print(f"{c=}, {i=}")
                columns_to_cross.append(c)
        rows_to_cross = []
        for d, j in enumerate(self.__input_data):
            if not j.has_galaxy:
                # print(f"{d=}, {j=}")
                rows_to_cross.append(d)
        # print(columns_to_cross)
        # print(rows_to_cross)

        cross_x = 0
        for i in columns_to_cross:
            if min_x < i and max_x > i:
                cross_x += 1
        cross_y = 0
        for i in rows_to_cross:
            if min_y < i and max_y > i:
                cross_y += 1

        return (
            (max_y - min_y)
            + cross_y * REPETITIONS
            + (max_x - min_x)
            + cross_x * REPETITIONS
        )

    def _calculate_1(self):
        grid = {}

        self.columns = []
        for x in range(len(self.__input_data[0].original)):
            has_g = False
            # print(x)
            for y in self.__input_data:
                if y.original[x] == "#":
                    has_g = True
            self.columns.append(has_g)
        # print(f"{columns=}")

        new_input = []
        for row in self.__input_data:
            r = []
            for c, v in enumerate(row.original):
                r.append(v)
                # if not columns[c]:
                #     for _ in range(REPETITIONS):
                #         r.append(v)
            new_input.append("".join(r))
            # print(f"{x=}")
            # if not row.has_galaxy:
            #     for _ in range(REPETITIONS):
            #         # print(f"{x=}")
            #         new_input.append(''.join(r))

        galaxies = {}
        for y, row in enumerate(new_input):
            # print(x)
            for x, v in enumerate(row):
                if v == "#":
                    galaxies[(x, y)] = v
        # print(galaxies)
        perm = list(combinations(galaxies, 2))
        result = 0
        for i in perm:
            sp = self.short_path(i)
            # print(f"short path for {i} = {sp}")
            # break
            result += sp
        return result

    def _calculate_2(self):
        return 0
