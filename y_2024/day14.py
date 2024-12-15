from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid, Point


@dataclass
class Row:
    original: str
    p: Optional[Point] = None
    v: Optional[Point] = None

    def __post_init__(self) -> None:
        p = self.original.split(" ")[0].replace("p=", "").split(",")
        v = self.original.split(" ")[1].replace("v=", "").split(",")

        self.p = Point(*[int(i) for i in p])
        self.v = Point(*[int(i) for i in v])


@dataclass
class Robot:
    pos: Point
    v: Point

    def move(self, witdh, lenght):
        self.pos = Point(
            (int(self.pos.x) + int(self.v.x)) % witdh,
            (int(self.pos.y) + int(self.v.y)) % lenght,
        )


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for j in self._input_data for i in j]
        self.__input_data = [Robot(i.p, i.v) for i in self.__input_data]

    def _calculate_1(self):
        witdh = 101 if not self._test else 11
        lenght = 103 if not self._test else 7
        for x in self.__input_data:
            for _ in range(100):
                x.move(witdh, lenght)

        q1 = range(0, witdh // 2), range(0, lenght // 2)
        q2 = range(witdh // 2 + 1, witdh), range(0, lenght // 2)
        q3 = range(0, witdh // 2), range(lenght // 2 + 1, lenght)
        q4 = range(witdh // 2 + 1, witdh), range(lenght // 2 + 1, lenght)

        p1 = 0
        for x in self.__input_data:
            for i in q1[0]:
                for j in q1[1]:
                    if x.pos.x == i and x.pos.y == j:
                        p1 += 1
        p2 = 0
        for x in self.__input_data:
            for i in q2[0]:
                for j in q2[1]:
                    if x.pos.x == i and x.pos.y == j:
                        p2 += 1
        p3 = 0
        for x in self.__input_data:
            for i in q3[0]:
                for j in q3[1]:
                    if x.pos.x == i and x.pos.y == j:
                        p3 += 1
        p4 = 0
        for x in self.__input_data:
            for i in q4[0]:
                for j in q4[1]:
                    if x.pos.x == i and x.pos.y == j:
                        p4 += 1

        g = Grid.from_h_l(lenght, witdh)
        g.display_param({r.pos: "*" for r in self.__input_data})
        return p1 * p2 * p3 * p4

    def _calculate_2(self):
        witdh = 101 if not self._test else 11
        lenght = 103 if not self._test else 7

        for i in range(6587):
            for x in self.__input_data:
                x.move(witdh, lenght)
            g = Grid.from_h_l(lenght, witdh)
        g.display_param({r.pos: "*" for r in self.__input_data})
        print(f">>> {i+1}")
        return 0
