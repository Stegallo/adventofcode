from .common import AoCDay
from collections import defaultdict


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = [i for i in self._input_data]
        print(f"len of input = {len(self.__input_data)}")

    def _calculate_1(self):
        x = self.__input_data[:]
        tabs = defaultdict(int)
        for y in x:
            # print(y.split(" -> "))
            start = y.split(" -> ")[0].split(",")
            end = y.split(" -> ")[1].split(",")
            # print(start)
            # print(end)
            if start[0] == end[0]:  # x
                print(y)
                print(start[1])
                print(end[1])
                l = sorted([int(start[1]), int(end[1])])
                print(l)
                for i in range(l[0], l[1] + 1):
                    tabs[(int(start[0]), i)] += 1
            if start[1] == end[1]:  # y
                print(y)
                print(start[0])
                print(end[0])
                l = sorted([int(start[0]), int(end[0])])
                print(l)
                for i in range(l[0], l[1] + 1):
                    tabs[(i, int(start[1]))] += 1
                # tabs[]
            # for z in y.split(" -> "):
            #     print(z)
        # print(tabs)
        # for i in tabs.values():
        #     print(i)
        result = sum(1 for i in tabs.values() if i >= 2)

        return result

    def _calculate_2(self):
        x = self.__input_data[:]
        tabs = defaultdict(int)
        for y in x:
            # print(y.split(" -> "))
            start = y.split(" -> ")[0].split(",")
            end = y.split(" -> ")[1].split(",")
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
                if int(start[0]) > int(end[0]):
                    # print("going left")
                    oriz = -1
                else:
                    # print("going right")
                    oriz = 1
                if int(start[1]) > int(end[1]):
                    # print("going down")
                    vert = -1
                else:
                    # print("going up")
                    vert = 1

                for i in range(abs(int(start[0]) - int(end[0])) + 1):
                    tabs[(int(start[0]) + i * oriz, int(start[1]) + i * vert)] += 1

        result = sum(1 for i in tabs.values() if i >= 2)

        return result
