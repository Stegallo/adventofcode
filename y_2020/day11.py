from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(11)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def _iteration(self):
        new_seating = []
        for i in range(len(self.__input)):
            new_seating.append([])
            for j in range(len(self.__input[i])):

                # check 8 seats:
                u = max(0, i - 1)
                r = min(len(self.__input[i]) - 1, j + 1)
                d = min(len(self.__input) - 1, i + 1)
                l = max(0, j - 1)
                # clockwise
                c1 = self.__input[u][j]
                c2 = self.__input[u][r]
                c3 = self.__input[i][r]
                c4 = self.__input[d][r]
                c5 = self.__input[d][j]
                c6 = self.__input[d][l]
                c7 = self.__input[i][l]
                c8 = self.__input[u][l]
                adj = [
                    c1 if u != i else None,
                    c2 if u != i and r != j else None,
                    c3 if r != j else None,
                    c4 if d != i and r != j else None,
                    c5 if d != i else None,
                    c6 if d != i and l != j else None,
                    c7 if l != j else None,
                    c8 if u != i and l != j else None,
                ]
                adj_map = [1 if i == "#" else 0 for i in adj]
                temp = self.__input[i][j]
                if self.__input[i][j] == "L":
                    if sum(adj_map) == 0:
                        temp = "#"
                if self.__input[i][j] == "#":
                    # if 4 or more occupied:
                    if sum(adj_map) >= 4:
                        temp = "L"
                new_seating[i].append(temp)

        self.__input = []
        for i in new_seating:
            string = "".join(i)
            self.__input.append(string)
        print()

    def _calculate_1(self):
        before = str(self.__input)
        c = 0
        while True:
            c += 1
            before = str(self.__input)
            self._iteration()
            after = str(self.__input)
            if before == after:
                break
        x = 0
        for i in self.__input:
            for j in i:
                if j == "#":
                    x += 1
        return x

    def _second_iteration(self):
        new_seating = []
        for i in range(len(self.__input)):
            new_seating.append([])
            for j in range(len(self.__input[i])):

                # check 8 seats:
                u = i - 1
                r = j + 1
                d = i + 1
                l = j - 1

                c1 = self.__input[u][j] if u >= 0 else None
                u1 = u
                while c1 == ".":
                    if c1 not in ["L", "#"]:
                        u1 = u1 - 1
                        c1 = self.__input[u1][j] if u1 >= 0 else None

                c2 = (
                    self.__input[u][r]
                    if u >= 0 and r <= len(self.__input[i]) - 1
                    else None
                )
                u2 = u
                r2 = r
                while c2 == ".":
                    if c2 not in ["L", "#"]:
                        u2 = u2 - 1
                        r2 = r2 + 1
                        c2 = (
                            self.__input[u2][r2]
                            if u2 >= 0 and r2 <= len(self.__input[i]) - 1
                            else None
                        )

                c3 = self.__input[i][r] if r <= len(self.__input[i]) - 1 else None
                r3 = r
                while c3 == ".":
                    if c3 not in ["L", "#"]:
                        r3 = r3 + 1
                        c3 = (
                            self.__input[i][r3]
                            if r3 <= len(self.__input[i]) - 1
                            else None
                        )

                c4 = (
                    self.__input[d][r]
                    if d <= len(self.__input) - 1 and r <= len(self.__input[i]) - 1
                    else None
                )
                d4 = d
                r4 = r
                while c4 == ".":
                    if c4 not in ["L", "#"]:
                        r4 = r4 + 1
                        d4 = d4 + 1
                        c4 = (
                            self.__input[d4][r4]
                            if d4 <= len(self.__input) - 1
                            and r4 <= len(self.__input[i]) - 1
                            else None
                        )

                c5 = self.__input[d][j] if d <= len(self.__input) - 1 else None
                d5 = d
                while c5 == ".":
                    if c5 not in ["L", "#"]:
                        d5 = d5 + 1
                        c5 = (
                            self.__input[d5][j] if d5 <= len(self.__input) - 1 else None
                        )

                c6 = (
                    self.__input[d][l]
                    if d <= len(self.__input) - 1 and l >= 0
                    else None
                )
                d6 = d
                l6 = l
                while c6 == ".":
                    if c6 not in ["L", "#"]:
                        d6 = d6 + 1
                        l6 = l6 - 1
                        c6 = (
                            self.__input[d6][l6]
                            if d6 <= len(self.__input) - 1 and l6 >= 0
                            else None
                        )

                c7 = self.__input[i][l] if l >= 0 else None
                l7 = l
                while c7 == ".":
                    if c7 not in ["L", "#"]:
                        l7 = l7 - 1
                        c7 = self.__input[i][l7] if l7 >= 0 else None

                c8 = self.__input[u][l] if u >= 0 and l >= 0 else None
                u8 = u
                l8 = l
                while c8 == ".":
                    if c8 not in ["L", "#"]:
                        u8 = u8 - 1
                        l8 = l8 - 1
                        c8 = self.__input[u8][l8] if u8 >= 0 and l8 >= 0 else None

                adj = [
                    c1,
                    c2,
                    c3,
                    c4,
                    c5,
                    c6,
                    c7,
                    c8,
                ]
                adj_map = [1 if i == "#" else 0 for i in adj]

                temp = self.__input[i][j]
                if self.__input[i][j] == "L":
                    if sum(adj_map) == 0:
                        temp = "#"
                if self.__input[i][j] == "#":
                    if sum(adj_map) >= 5:
                        temp = "L"
                new_seating[i].append(temp)

        self.__input = []
        for i in new_seating:
            string = "".join(i)
            self.__input.append(string)
        for i in self.__input:
            print(i)

    def _calculate_2(self):
        before = str(self.__input)
        c = 0
        while True:
            c += 1
            before = str(self.__input)
            self._second_iteration()
            after = str(self.__input)
            if before == after:
                break
        x = 0
        for i in self.__input:
            for j in i:
                if j == "#":
                    x += 1
        return x
