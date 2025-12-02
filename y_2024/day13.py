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

    def find_prize(self, cost=0, x=0, y=0, a=0, b=0, pr_mul=0):
        M = np.array(
            [[self.ba.x_incr, self.bb.x_incr], [self.ba.y_incr, self.bb.y_incr]],
        )
        Minv = np.linalg.inv(M)
        pr = np.array([self.pr.x + pr_mul, self.pr.y + pr_mul])
        x = np.matmul(Minv, pr)

        a, b = round(x[0]), round(x[1])

        if (
            a * self.ba.x_incr + b * self.bb.x_incr != self.pr.x + pr_mul
            or a * self.ba.y_incr + b * self.bb.y_incr != self.pr.y + pr_mul
        ):
            return 0

        return a * 3 + b


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
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

    def _calculate_1(self):
        result = 0

        for c, x in enumerate(self.machines):
            result += x.find_prize()

        return result

    def _calculate_2(self):
        result = 0

        for c, x in enumerate(self.machines):
            result += x.find_prize(pr_mul=10000000000000)

        return result
