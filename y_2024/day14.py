from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid,Point


@dataclass
class Row:
    original: str
    p: Optional[Point] = None
    v: Optional[Point] = None

    def __post_init__(self) -> None:
        p = self.original.split(' ')[0].replace('p=','')
        v = self.original.split(' ')[1].replace('v=','')
        self.p = Point(*p.split(','))
        self.v = Point(*v.split(','))

@dataclass
class Robot:
    pos: Point
    v: Point

    def move(self, witdh, lenght):
        self.pos = Point((self.pos.x + self.v.x)%witdh, (self.pos.y+self.v.y)%lenght)

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        print(f"{self._input_data=}")
        print(f"{len(self._input_data)=}")
        print(f"{len(self._input_data[0])=}")
        # self.grid = Grid.from_input(self._input_data)
        # self.grid.display()
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data = [Row(i) for j in self._input_data for i in j]
        self.__input_data = [Robot(i.p, i.v) for i in self.__input_data]
        # for x in self.__input_data:
        #     print(f"{x}")

    def _calculate_1(self):
        result = 0
        witdh = 101
        # witdh = 11
        lenght = 103
        # lenght = 7
        for x in self.__input_data:
            # print(x)
            # if x.pos!=Point(2,4):
            #     continue

            for _ in range(100):
                # for _ in range(3):
                x.move(witdh, lenght)
                # print(f">>> {x}")

        # print()
        qb1 = witdh//2
        qb2 = lenght//2
        q1 = range(0, witdh//2), range(0, lenght//2)
        q2 = range(witdh//2+1,witdh), range(0, lenght//2)
        q3 = range(0, witdh//2), range(lenght//2+1,lenght)
        q4 = range(witdh//2+1,witdh), range(lenght//2+1,lenght)
        print(q1)
        print(q2)
        print(q3)
        print(q4)
        p1=0
        for x in self.__input_data:
            for i in q1[0]:
                for j in q1[1]:
                    if x.pos.x == i and x.pos.y == j:
                        # print(x)
                        p1+=1
        p2=0
        for x in self.__input_data:
            for i in q2[0]:
                for j in q2[1]:
                    if x.pos.x == i and x.pos.y == j:
                        # print(x)
                        p2+=1
        p3=0
        for x in self.__input_data:
            for i in q3[0]:
                for j in q3[1]:
                    if x.pos.x == i and x.pos.y == j:
                        # print(x)
                        p3+=1
        p4=0
        for x in self.__input_data:
            for i in q4[0]:
                for j in q4[1]:
                    if x.pos.x == i and x.pos.y == j:
                        # print(x)
                        p4+=1

        print(p1,p2,p3,p4)
        return p1*p2*p3*p4

    def _calculate_2(self):
        result = 0
        return result
