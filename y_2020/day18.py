import re

from .common import AoCDay
from .utils import prod

# GLOBAL_POINTER = 0


def custom_add(a, b):
    return a + b


def custom_mul(a, b):
    return a * b


OPS = {"+": custom_add, "*": custom_mul}


class Day(AoCDay):
    def __init__(self):
        super().__init__(18)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def calc1(self, lst):
        # global GLOBAL_POINTER
        # print(lst)
        # print()
        result = 0
        op = None
        op_n = 0
        a = 0
        b = 0
        x = []
        ignore = 0
        # breakpoint()
        for c, j in enumerate(lst):
            # print(f"{j=} in {''.join(lst)}, {ignore=}; {x=}")
            if ignore:
                if j == ")":
                    ignore -= 1
                if j == "(":
                    ignore += 1
                continue
            if j == ")":
                return a
            # continue
            if j in OPS:
                # print(OPS)
                op = j
            else:
                if op_n == 0:
                    if j == "(":
                        ignore += 1
                        # breakpoint()
                        a = self.calc1(lst[c + 1 :])
                    else:
                        a = int(j)
                    x.append(a)
                    op_n = 1
                else:
                    if j == "(":
                        ignore += 1
                        # breakpoint()
                        b = self.calc1(lst[c + 1 :])
                    else:
                        b = int(j)
                    if op == "+" or True:
                        # a = x[-1]
                        # print(f"{a=}, {b=}")
                        a = OPS[op](a, b)
                        # x[-1] = a
                    else:
                        x.append(b)
                        # breakpoint()
                # print(f"{x=}")

        return a

    def calc2(self, lst):
        # global GLOBAL_POINTER
        # print(lst)
        # print()
        result = 0
        op = None
        op_n = 0
        a = 0
        b = 0
        x = []
        ignore = 0
        # breakpoint()
        for c, j in enumerate(lst):
            # print(f"{j=} in {''.join(lst)}, {ignore=}; {x=}")
            if ignore:
                if j == ")":
                    ignore -= 1
                if j == "(":
                    ignore += 1
                continue
            if j == ")":
                return prod(x)
            # continue
            if j in OPS:
                # print(OPS)
                op = j
            else:
                if op_n == 0:
                    if j == "(":
                        ignore += 1
                        # breakpoint()
                        a = self.calc2(lst[c + 1 :])
                    else:
                        a = int(j)
                    x.append(a)
                    op_n = 1
                else:
                    if j == "(":
                        ignore += 1
                        # breakpoint()
                        b = self.calc2(lst[c + 1 :])
                    else:
                        b = int(j)
                    if op == "+":
                        a = x[-1]
                        # print(f"{a=}, {b=}")
                        a = OPS[op](a, b)
                        x[-1] = a
                    else:
                        x.append(b)
                        # breakpoint()
                # print(f"{x=}")

        return prod(x)

    def _calculate_1(self):
        # print(self.__input)
        result = 0
        for i in self.__input:
            express = [k for k in list(i) if k != " "]
            # print(f"{express=}")
            result += self.calc1(express)

        return result

    def _calculate_2(self):
        # print(self.__input)
        result = 0
        for i in self.__input:
            express = [k for k in list(i) if k != " "]
            # print(f"{express=}")
            result += self.calc2(express)

        return result
