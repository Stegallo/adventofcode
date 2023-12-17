from math import lcm
from typing import Dict, List

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Node:
    left: str
    right: str

    def next(self, action):
        config = {
            "L": self.left,
            "R": self.right,
        }
        return config[action]


@dataclass
class Input:
    instructions: str
    network: Dict[str, Node]

    @staticmethod
    def from_source(source: List):
        instructions, network = source
        return Input(
            instructions[0],
            dict(
                [
                    (lambda x, y: (x, Node(*y.split(", "))))(
                        *i.replace("(", "").replace(")", "").split(" = "),
                    )
                    for i in network
                ],
            ),
        )


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)
        self.index = None

    def _preprocess_input(self) -> None:
        self.__input_data = Input.from_source(self._input_data)

    def next(self):
        self.index = (self.index + 1) % (len(self.__input_data.instructions))
        return self.__input_data.instructions[self.index]

    def _calculate_1(self) -> int:  # 11309
        self.index = -1
        result = 0
        current = "AAA"

        while current != "ZZZ":
            action = self.next()
            current = self.__input_data.network[current].next(action)
            result += 1

        return result

    def _calculate_2(self) -> int:  # 13740108158591
        self.index = -1
        currents = [i for i in self.__input_data.network if i[-1] == "A"]
        results = []
        for current in currents:
            c = 0
            while current[-1] != "Z":
                action = self.next()
                current = self.__input_data.network[current].next(action)
                c += 1
            results.append(c)

        return lcm(*results)
