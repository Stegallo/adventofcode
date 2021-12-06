from .common import AoCDay
from collections import defaultdict


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = list(self._input_data)

    def _calculate_1(self):
        tabs = defaultdict(int)
        for move in self.__input_data:
            start = move.split(" -> ")[0].split(",")
            end = move.split(" -> ")[1].split(",")
            if start[0] == end[0]:  # x
                l = sorted([int(start[1]), int(end[1])])
                for i in range(l[0], l[1] + 1):
                    tabs[(int(start[0]), i)] += 1
            if start[1] == end[1]:  # y
                l = sorted([int(start[0]), int(end[0])])
                for i in range(l[0], l[1] + 1):
                    tabs[(i, int(start[1]))] += 1

        return sum(i >= 2 for i in tabs.values())

    def _calculate_2(self):
        tabs = defaultdict(int)
        for move in self.__input_data:
            start = move.split(" -> ")[0].split(",")
            end = move.split(" -> ")[1].split(",")
            if start[0] == end[0]:  # x
                l = sorted([int(start[1]), int(end[1])])
                for i in range(l[0], l[1] + 1):
                    tabs[(int(start[0]), i)] += 1
            elif start[1] == end[1]:  # y
                l = sorted([int(start[0]), int(end[0])])
                for i in range(l[0], l[1] + 1):
                    tabs[(i, int(start[1]))] += 1
            elif abs(int(start[0]) - int(end[0])) == abs(int(start[1]) - int(end[1])):
                # print("diagonalley")
                oriz = -1 if int(start[0]) > int(end[0]) else 1
                vert = -1 if int(start[1]) > int(end[1]) else 1
                for i in range(abs(int(start[0]) - int(end[0])) + 1):
                    tabs[(int(start[0]) + i * oriz, int(start[1]) + i * vert)] += 1

        return sum(i >= 2 for i in tabs.values())
