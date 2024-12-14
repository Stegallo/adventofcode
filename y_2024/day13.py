from typing import Optional
import numpy as np
from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    processed: Optional[list[str]] = None

    def __post_init__(self) -> None:
        self.processed = self.original.split(": ")


@dataclass
class Button:
    name: str
    x_incr: int
    y_incr: int


@dataclass
class Prize:
    x: int
    y: int


@dataclass
class Machine:
    ba: Button
    bb: Button
    pr: Prize

    def find_prize(self, cost=0, x=0, y=0, a=0, b=0):
        M = np.array(
            [[self.ba.x_incr, self.bb.x_incr], [self.ba.y_incr, self.bb.y_incr]],
        )
        Minv = np.linalg.inv(M)
        pr = np.array([self.pr.x + 10000000000000, self.pr.y + 10000000000000])
        x = np.matmul(Minv, pr)
        print(x[0], x[1])
        a, b = round(x[0]), round(x[1])
        print(a, b)
        # print(a*self.ba.x_incr+b*self.bb.x_incr)
        # print(a*self.ba.y_incr+b*self.bb.y_incr)
        #

        if (
            a * self.ba.x_incr + b * self.bb.x_incr != self.pr.x + 10000000000000
            or a * self.ba.y_incr + b * self.bb.y_incr != self.pr.y + 10000000000000
        ):
            return 0
        print(a, b)
        # if a>100 or b > 100:
        #
        #     return 0
        print()
        return a * 3 + b
        # breakpoint()
        # print(cost, x ,y, self.pr.x, self.pr.y, a, b)
        # breakpoint()
        # if x == self.pr.x and y == self.pr.y:
        #     return cost
        #
        # if x > self.pr.x or y > self.pr.y:
        #     return None
        # #
        # press_a = self.find_prize(cost+3,x+self.ba.x_incr,y+self.ba.y_incr, a+1, b)
        # press_b = self.find_prize(cost+1,x+self.bb.x_incr,y+self.bb.y_incr, a, b+1)
        # if press_a or press_b:
        #     return press_a or press_b
        # #
        # return None
        # print(self.pr.x/self.ba.x_incr)
        # print(self.pr.y/self.ba.y_incr)
        # print(self.pr.x/self.bb.x_incr)
        # print(self.pr.y/self.bb.y_incr)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        print(f"{len(self._input_data)=}")
        print(f"{len(self._input_data[0])=}")
        # self.grid = Grid.from_input(self._input_data)
        # self.grid.display()
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.machines = []
        for j in self._input_data:
            local_machine = []
            for c, i in enumerate(j):
                r = Row(i)
                if c == 0:
                    a = Button(
                        r.processed[0].replace("Button ", ""),
                        int(r.processed[1].split(", ")[0].replace("X", "")),
                        int(r.processed[1].split(", ")[1].replace("Y", "")),
                    )
                    # breakpoint()
                if c == 1:
                    b = Button(
                        r.processed[0].replace("Button ", ""),
                        int(r.processed[1].split(", ")[0].replace("X", "")),
                        int(r.processed[1].split(", ")[1].replace("Y", "")),
                    )
                if c == 2:
                    p = Prize(
                        r.processed[1].split(", ")[0].replace("X=", ""),
                        r.processed[1].split(", ")[1].replace("Y=", ""),
                    )
            local_machine = Machine(a, b, p)
            self.machines.append(local_machine)
        # self.__input_data = [Row(i) for j in self._input_data for i in j]
        # for x in self.machines:
        #     # for y in x:
        #     print(f"{x}")
        #     print()

    def _calculate_1(self):  # 15731 low
        result = 0
        # return result
        for c, x in enumerate(self.machines):
            # a,b = x.find_prize()
            # resulta += a
            # resultb += b
            print(f"{c=}, {x.find_prize()}")
            result += x.find_prize()
            # break
            # print(f"{x}")
        # print(resulta)
        # print(resultb)
        return result

    def _calculate_2(self):
        result = 0
        return result
