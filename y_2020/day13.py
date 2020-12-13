import re

from .common import AoCDay
from collections import defaultdict


class Day(AoCDay):
    def __init__(self):
        super().__init__(13)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def _calculate_1(self):
        # info(self._input_data)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        print(self.__input)
        arr = int(self.__input[0])
        buses = [int(i) for i in self.__input[1].split(",") if i != "x"]
        print(f"{buses=}")
        schedule = {}  # defaultdict(int)
        for i in buses:
            c = 0
            schedule[i] = []
            while True:
                c += 1
                schedule[i].append(i * c)
                if i * c > arr * 2:
                    break
        # print(f"{schedule=}")
        mins = {}
        for k, v in schedule.items():
            for i in v:
                if i >= arr:
                    mins[k] = i
                    break
        # print(f"{mins=}")
        min_x = min([m for m in mins.values()])
        min_x = arr * 10
        for k, v in mins.items():
            if v < min_x:
                min_x = v
                bus_id = k

        print(f"{min_x=}")
        return (min_x - arr) * bus_id

    def _calculate_2(self):
        buses = {
            c: (int(i) if i != "x" else None)
            for c, i in enumerate(self.__input[1].split(","))
        }
        print(f"{buses=}")

        time = 0
        deps = [
            (int(i) if i != "x" else None)
            for c, i in enumerate(self.__input[1].split(","))
        ]

        next_dep = [i for i in deps]
        increment = min([i for i in next_dep if i])
        print(f"{next_dep=}, {increment}")
        mark = 10 * 1000 * 1000
        while True:
            for i in range(len(deps)):
                # print(f"{next_dep[i]=}, {time=}")
                if deps[i]:
                    if (next_dep[i]) < time + 1:
                        next_dep[i] += deps[i]
            # next_dep = [1068781, 1068782, 0, 0, 1068785, 0, 1068787, 1068788]
            # time = 1068781
            solved = True

            for c, i in enumerate(next_dep):
                print(f"{time=},{next_dep=}, {next_dep[0] + c=}, {i=}")
                if next_dep[0] + c != i:
                    if i is not None:
                        solved = False
                        break
                    # time = 1068781
                # print(f"{c}, {i}")
                # print(f"{solved=}")

            # if solved or time > 1000:  # 1068790:
            # if solved or time > 1068790:
            if solved:  # or
                # if time > 90:
                # if True:
                break
            print(f"{time=},{next_dep=},{increment=}\n")
            if time > mark:
                print(f"{time=}, {mark=}")
                mark = mark + 10 * 1000 * 1000
            time += increment
        print(f"\n{next_dep=}, {time + increment=}")
        return next_dep[0]
