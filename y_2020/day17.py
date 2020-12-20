import re
import copy
from .common import AoCDay


NUM_ITERATIONS = 6


class Day(AoCDay):
    def __init__(self):
        super().__init__(17)

    def _preprocess_input(self):
        self.__width = 0
        for i in self._input_data:
            self.__width = len(self._input_data[0])
            break
        self.__height = len(self._input_data)
        zero_layer = []
        for y in range(-NUM_ITERATIONS, self.__height + NUM_ITERATIONS):
            if 0 <= y <= self.__height - 1:
                # print(f"{y=}, {self._input_data[y]=}")
                zero_layer.append(
                    list(
                        "." * NUM_ITERATIONS
                        + self._input_data[y]
                        + "." * NUM_ITERATIONS
                    )
                )
                continue
            zero_layer.append(list("." * (self.__width + NUM_ITERATIONS * 2)))

        self.__world = []
        # for w in range(-NUM_ITERATIONS, NUM_ITERATIONS + 1):
        #     if
        for z in range(-NUM_ITERATIONS, NUM_ITERATIONS + 1):
            if z == 0:
                self.__world.append(zero_layer)
                continue
            self.__world.append([["." for _ in i] for i in zero_layer])

        self.__4dworld = []
        for w in range(-NUM_ITERATIONS, NUM_ITERATIONS + 1):
            if w == 0:
                self.__4dworld.append(self.__world)
                continue
            self.__4dworld.append([[["." for _ in i] for i in j] for j in self.__world])

    def validate_borders(self, ck, cj, ci, ch, x=0, y=0, z=0, w=0):
        # if cj + z == 6 and cj + y == 5 and ck + x == 2:
        #     print(f"hello: {ci + x=},{cj +y=},{ck +z=}")
        #     breakpoint()
        return (
            (0 <= ch + w <= NUM_ITERATIONS * 2)
            and (0 <= ci + z <= NUM_ITERATIONS * 2)
            and (0 <= cj + y <= (self.__height + NUM_ITERATIONS * 2) - 1)
            and (0 <= ck + x <= (self.__width + NUM_ITERATIONS * 2) - 1)
        )

    def check_box(self, ck, cj, ci, ch, x, y, z, w):
        # if 6 <= ci + z <= 6:
        # print(f"{ci + z=}, {self.__world[ci + z]=}")
        # print(f"{cj + y=}, {self.__world[ci + z][cj + y]=}")
        # print(f"before border{cj=}; {ci + z=}, {cj+y=}, {ck+x=}")

        # if self.__world[ci][cj][ck] == "#":
        # print(f"hello: {x=},{y=},{z=}")
        if not self.validate_borders(ck, cj, ci, ch, x, y, z, w):
            #     if 6 <= ci + z <= 6:
            #         print("not valid border")
            return 0
        # breakpoint()
        # if 6 <= ci + z <= 6:
        #     # print(f"{ci + z=}, {self.__world[ci + z]=}")
        #     # print(f"{cj + y=}, {self.__world[ci + z][cj + y]=}")
        #     print(f"after border{cj=}")
        elem = self.__4dworld[ch + w][ci + z][cj + y][ck + x]
        # print(elem)
        if elem == "#":
            # breakpoint()
            return 1
        return 0
        # if problem1_or_occupied(problem, elem):
        #     return elem
        # elif problem2_and_empty(problem, elem):
        #     while validate_borders(data, i, j, length, ns, oe):
        #         if check_not_empty(data[i - SIGN_NS[ns]][j - SIGN_OE[oe]]):
        #             return data[i - SIGN_NS[ns]][j - SIGN_OE[oe]]
        #         i -= SIGN_NS[ns]
        #         j -= SIGN_OE[oe]
        # else:
        #     return "L"

    def count_active_nb(self, ch, ci, cj, ck):
        # if self.__world[ci][cj][ck] == "#":
        #     # breakpoint()
        #     print(ci, cj, ck)
        c = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        # print(i, j, k)
                        # if ci == 7:  # and self.__world[ci][cj][ck] == "#":
                        #     print(f"{ci=}, {z=}")
                        #     breakpoint()
                        if x == y == z == w == 0:
                            continue
                        c += self.check_box(ck, cj, ci, ch, x, y, z, w)
        return c
        # print(f"{c=}")
        # self.check_box(ci, cj, ck)

    def __iteration(self):
        # print(self.__cube)
        # print(f"{len(self.__world)=}")
        new_world = copy.deepcopy(self.__4dworld)
        for ch, h in enumerate(self.__4dworld):
            for ci, i in enumerate(h):
                # print(f"{ci=}")
                for cj, j in enumerate(i):
                    # print(f"{cj=}")
                    for ck, k in enumerate(j):
                        # print(f"{ck=}")
                        # continue
                        active_nb = self.count_active_nb(ch, ci, cj, ck)
                        if k == "#" and not active_nb in [2, 3]:
                            # print(f"{ci}, {cj}, {ck}: {k}")
                            # print(active_nb)
                            new_world[ch][ci][cj][ck] = "."
                        if k == "." and active_nb in [3]:
                            # print(f"{ci}, {cj}, {ck}: {k}")
                            # print(active_nb)
                            new_world[ch][ci][cj][ck] = "#"
        self.__4dworld = new_world
        # print(new_world)
        # print(v)
        # find neighbors and state
        # evaluate change

        ...

    def _calculate_1(self):
        return 0
        # info(self._input_data)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        # self.__input
        for i in range(NUM_ITERATIONS):
            self.__iteration()

        res = 0
        for i in self.__world:
            # print(f"{ci=}")
            for j in i:
                # print(f"{cj=}")
                for k in j:
                    # print(f"{ck=}")
                    # continue
                    # active_nb = self.count_active_nb(ci, cj, ck)
                    if k == "#":
                        res += 1
        return res

    def _calculate_2(self):
        for i in range(NUM_ITERATIONS):
            self.__iteration()

        res = 0
        for h in self.__4dworld:
            for i in h:
                for j in i:
                    for k in j:
                        if k == "#":
                            res += 1
        return res
