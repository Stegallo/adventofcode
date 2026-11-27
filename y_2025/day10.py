from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from math import inf
import numpy as np
from scipy.optimize import linprog


@dataclass
class Row:
    original: str
    # processed: Optional[str] = None
    target: Optional[str] = None
    buttons: Optional[list] = None
    joltage: Optional[list[int]] = None

    def __post_init__(self) -> None:
        a = self.original.index("]")
        b = self.original.index("{")
        # self.processed = [self.original[:a+1],
        #                   self.original[a+2:b-1], self.original[b:]]
        self.target = self.original[1:a]
        # breakpoint()
        self.buttons = [
            tuple(int(j) for j in i[1:-1].split(","))
            for i in self.original[a + 2 : b - 1].split(" ")
        ]
        self.joltage = [int(i) for i in self.original[b + 1 : -1].split(",")]
        # self.joltage = self.original[b+1:-1]
        # breakpoint()
        # print(self.joltage)


@dataclass
class Light:
    states: list[str]

    def toggle(self, button):
        # print(f"{button=}")
        result = list(self.states)
        for el in button:
            # print(f"{el=}, {self.states[el]=}")
            result[el] = "#" if self.states[el] == "." else "."
            # print(''.join(result))
        return Light(result)

    def __hash__(self) -> int:
        return hash(tuple(self.states))


@dataclass
class Counter:
    states: list[int]

    def press(self, button, joltage):
        # print(f"{button=}")
        result = list(self.states)
        for el in button:
            # print(f"{el=}, {self.states[el]=}")
            if self.states[el] > joltage[el]:
                raise Exception()
            result[el] = self.states[el] + 1
            # print(''.join(result))
        return Counter(result)

    def __hash__(self) -> int:
        return hash(tuple(self.states))


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        # print(f"{len(self._input_data)=}")
        # print(f"{len(self._input_data[0])=}")
        # self.grid = Grid.from_input(self._input_data)
        # self.grid.display()
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data = [Row(i) for j in self._input_data for i in j]
        for x in self.__input_data:
            print(x.target, x.buttons, x.joltage)
            # print(f"{x.processed[0]=}")
            # print(f"{x.processed[1]=}")

    def _calculate_1(self):
        result = 0
        return result
        for x in self.__input_data:
            # print(len(x.target))
            # print('.' * len(x.target))
            # breakpoint()
            base = Light(list("." * len(x.target)))
            ...
            # print(base)
            visited = set()
            queue = [(base, [])]
            max_len = inf
            while queue:
                base, path = queue.pop(0)
                for i in x.buttons:
                    # print(base)
                    toggled = base.toggle(i)
                    if "".join(toggled.states) == x.target:
                        print(toggled, path, i)
                        if len(path) + 1 < max_len:
                            max_len = len(path) + 1
                        # raise
                    # print(f"{i=},\t\t {toggled=}")
                    if toggled not in visited:
                        queue.append((toggled, path + [i]))
                    visited.add(toggled)

            print(visited, max_len)
            result += max_len
            # break

        return result

    def _calculate_2(self):
        result = 0
        for x in self.__input_data:
            print(x.joltage)
            print(x.buttons)
            max_l = 0
            ss = []
            for i in x.buttons:
                # print(i)
                s = {}
                k = 0
                for j in range(10):
                    if j in i:
                        s[j] = 1
                        k = j
                    else:
                        s[j] = 0
                max_l = max(max_l, k)
                ss.append(list(s.values()))
            # print(max_l, [i[:max_l+1] for i in ss])
            matrix = np.array([i[: max_l + 1] for i in ss])
            print(matrix.T)
            solution = linprog(
                c=[1 for _ in range(len(x.buttons))],
                A_eq=matrix.T,
                b_eq=x.joltage,
                integrality=1,
            )
            # breakpoint()
            result += int(solution.fun)
            # inv = np.linalg.pinv(matrix.T)
            # rez = np.matmul(inv, x.joltage)
            # # print(f"{sum([abs(i - round(i)) for i in rez])}")
            # # if sum([abs(i - round(i)) for i in rez]) > 0.5:
            # rounded_rez = [round(i) for i in rez]
            # print(f"{rez=} {rounded_rez=}")
            # for i in rounded_rez:
            #     print(i)
            # # print(np.matmul(matrix.T, rez), x.joltage)
            # # print(np.matmul(matrix.T, [float(round(i, 0)) for i in rez]), x.joltage)
            # # if list(np.matmul(matrix.T, [round(i) for i in rez])) != x.joltage:
            # #         raise
            # print(int(sum(rounded_rez)))
            # result += int(sum(rounded_rez))
            # print(sum(np.matmul(inv, x.joltage)))
            # # base = Counter(list('0' * len(x.joltage)))
            # print(base)
            # visited = set()
            # queue = [(base, [])]
            # max_len = inf
            # while queue:
            #     base, path = queue.pop(0)
            #     print(base)
            #     for i in x.buttons:
            #         try:
            #             pressed = base.press(i, x.joltage)
            #         except:
            #             continue
            #         # print(','.join([str(i) for i in pressed.states]))
            #         # print(','.join([str(i) for i in x.joltage]))
            #         if ','.join([str(i) for i in pressed.states]) == \
            #                 ','.join([str(i) for i in x.joltage]):
            #             print(f"{i=},\t\t {pressed=}, {len(path)+1}")
            #             if len(path)+1 < max_len:
            #                 max_len = len(path)+1
            #             # raise
            #         if pressed not in visited:
            #             queue.append((pressed, path + [i]))
            #         visited.add(pressed)
            # # print(visited, max_len)
            # result += max_len
            # break
        # 18837 too high
        return result
