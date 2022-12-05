from copy import deepcopy
from typing import Dict, List

from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__parse_stack()

    def __parse_stack(self) -> None:
        start = self._input_data[0]
        self.__stack: Dict[int, List[str]] = {}
        self.__max_rack = 0
        for i in start[-1].strip().split("   "):
            if not i:
                break
            self.__stack[int(i)] = []
            self.__max_rack += 1
        for i in range(len(start) - 2, -1, -1):
            for j in range(self.__max_rack):
                if container := start[i][j * 4 : (j + 1) * 4].strip():
                    self.__stack[j + 1].append(container)

    def __produce_output(self, stack) -> str:
        r = [
            stack[i + 1].pop().replace("[", "").replace("]", "")
            for i in range(self.__max_rack)
        ]

        return "".join(r)

    def _calculate_1(self):
        moves = self._input_data[1]
        local_stack = deepcopy(self.__stack)
        for i in moves:
            (_, quantity, _, source, _, destination) = i.split(" ")

            for _ in range(int(quantity)):
                local_stack[int(destination)].append(local_stack[int(source)].pop())
        return self.__produce_output(local_stack)

    def _calculate_2(self):
        moves = self._input_data[1]
        local_stack = deepcopy(self.__stack)
        for i in moves:
            (_, quantity, _, source, _, destination) = i.split(" ")

            t = []
            for _ in range(int(quantity)):
                t.insert(0, local_stack[int(source)].pop())
            local_stack[int(destination)].extend(t)

        return self.__produce_output(local_stack)
