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

        self.__3dworld = []
        for z in range(-NUM_ITERATIONS, NUM_ITERATIONS + 1):
            if z == 0:
                self.__3dworld.append(zero_layer)
                continue
            self.__3dworld.append([["." for _ in i] for i in zero_layer])

        self.__4dworld = []
        for w in range(-NUM_ITERATIONS, NUM_ITERATIONS + 1):
            if w == 0:
                self.__4dworld.append(self.__3dworld)
                continue
            self.__4dworld.append(
                [[["." for _ in i] for i in j] for j in self.__3dworld]
            )

    def validate_borders3d(self, ck, cj, ci, x=0, y=0, z=0):
        return (
            (0 <= ci + z <= NUM_ITERATIONS * 2)
            and (0 <= cj + y <= (self.__height + NUM_ITERATIONS * 2) - 1)
            and (0 <= ck + x <= (self.__width + NUM_ITERATIONS * 2) - 1)
        )

    def check_box3d(self, ck, cj, ci, x, y, z):
        if not self.validate_borders3d(ck, cj, ci, x, y, z):
            return 0
        elem = self.__3dworld[ci + z][cj + y][ck + x]
        if elem == "#":
            return 1
        return 0

    def count_active_nb3d(self, ci, cj, ck):
        c = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if x == y == z == 0:
                        continue
                    c += self.check_box3d(ck, cj, ci, x, y, z)
        return c

    def validate_borders4d(self, ck, cj, ci, ch, x=0, y=0, z=0, w=0):
        return (
            (0 <= ch + w <= NUM_ITERATIONS * 2)
            and (0 <= ci + z <= NUM_ITERATIONS * 2)
            and (0 <= cj + y <= (self.__height + NUM_ITERATIONS * 2) - 1)
            and (0 <= ck + x <= (self.__width + NUM_ITERATIONS * 2) - 1)
        )

    def check_box4d(self, ck, cj, ci, ch, x, y, z, w):
        if not self.validate_borders4d(ck, cj, ci, ch, x, y, z, w):
            return 0
        elem = self.__4dworld[ch + w][ci + z][cj + y][ck + x]
        if elem == "#":
            return 1
        return 0

    def count_active_nb4d(self, ch, ci, cj, ck):
        c = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        if x == y == z == w == 0:
                            continue
                        c += self.check_box4d(ck, cj, ci, ch, x, y, z, w)
        return c

    def __iteration3d(self):
        new_world = copy.deepcopy(self.__3dworld)
        for ci, i in enumerate(self.__3dworld):
            for cj, j in enumerate(i):
                for ck, k in enumerate(j):
                    active_nb = self.count_active_nb3d(ci, cj, ck)
                    if k == "#" and active_nb not in [2, 3]:
                        new_world[ci][cj][ck] = "."
                    if k == "." and active_nb in [3]:
                        new_world[ci][cj][ck] = "#"
        self.__3dworld = new_world

    def __iteration4d(self):
        new_world = copy.deepcopy(self.__4dworld)
        for ch, h in enumerate(self.__4dworld):
            for ci, i in enumerate(h):
                for cj, j in enumerate(i):
                    for ck, k in enumerate(j):
                        active_nb = self.count_active_nb4d(ch, ci, cj, ck)
                        if k == "#" and active_nb not in [2, 3]:
                            new_world[ch][ci][cj][ck] = "."
                        if k == "." and active_nb in [3]:
                            new_world[ch][ci][cj][ck] = "#"
        self.__4dworld = new_world

    def _calculate_1(self):
        for i in range(NUM_ITERATIONS):
            self.__iteration3d()

        res = 0
        for i in self.__3dworld:
            for j in i:
                for k in j:
                    if k == "#":
                        res += 1
        return res

    def _calculate_2(self):
        for i in range(NUM_ITERATIONS):
            self.__iteration4d()

        res = 0
        for h in self.__4dworld:
            for i in h:
                for j in i:
                    for k in j:
                        if k == "#":
                            res += 1
        return res
