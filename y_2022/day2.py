from .common import AoCDay

MAP = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}

d = {"X": 1, "Y": 2, "Z": 3}
d2 = {"R": 1, "P": 2, "S": 3}


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = [[i for i in chunk] for chunk in self._input_data][0]
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # self.__input_data = [[i for i in chunk] for chunk in self._input_data]

    def _calculate_1(self):
        x = self.__input_data
        # print(f"{x=}")
        incr = 0
        for i in x:
            r = i.split(" ")
            v = d[r[1]]
            # print(f"{v=}, {r=}")
            p = 0
            # breakpoint()
            if MAP[r[0]] == MAP[r[1]]:
                p = 3
            elif MAP[r[1]] == "R" and MAP[r[0]] == "S":
                p = 6
            elif MAP[r[1]] == "S" and MAP[r[0]] == "P":
                p = 6
            elif MAP[r[1]] == "P" and MAP[r[0]] == "R":
                p = 6
            else:
                p = 0
            partial = v + p
            # print(f"{p=}, {partial=}")
            # print(partial)
            incr += partial
        return incr  # max(sum(i) for i in self.__input_data)

    def _calculate_2(self):
        x = self.__input_data
        print(f"{x=}")
        incr = 0
        for i in x:
            r = i.split(" ")
            print(r)
            if r[1] == "Y":  # draw
                m = MAP[r[0]]
            elif r[1] == "X":  # lose
                if MAP[r[0]] == "R":
                    m = "S"
                elif MAP[r[0]] == "S":
                    m = "P"
                elif MAP[r[0]] == "P":
                    m = "R"
            else:  # win
                if MAP[r[0]] == "R":
                    m = "P"
                elif MAP[r[0]] == "S":
                    m = "R"
                elif MAP[r[0]] == "P":
                    m = "S"
            print(f"{r[1]=},{m=}")
            v = d2[m]
            p = 0
            # breakpoint()
            if MAP[r[0]] == m:
                p = 3
            elif m == "R" and MAP[r[0]] == "S":
                p = 6
            elif m == "S" and MAP[r[0]] == "P":
                p = 6
            elif m == "P" and MAP[r[0]] == "R":
                p = 6
            else:
                p = 0
            partial = v + p
            # print(f"{p=}, {partial=}")
            # print(partial)
            incr += partial
        return incr  # max(sum(i) for i in self.__input_data)
