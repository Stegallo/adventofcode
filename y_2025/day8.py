from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from math import dist


@dataclass
class Row:
    original: str
    processed: Optional[tuple] = None

    def __post_init__(self) -> None:
        self.processed = tuple(int(i) for i in self.original.split(","))


# @dataclass
# class Circuit:
#     points: list[int]


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
        # for x in self.__input_data:
        #     print(f"{x}")

    def _calculate_1(self):
        result = 1
        for x in self.__input_data:
            ...
            # print(f"Processing circuit {x.processed}")
        distances = {}
        for i in range(len(self.__input_data[:-1])):
            for j in range(i + 1, len(self.__input_data)):
                ll = self.__input_data[i].processed
                mm = self.__input_data[j].processed
                # print(i, j, l, m, dist(l,m))
                distances[(ll, mm)] = dist(ll, mm) ** 2
        # print(distances)
        # sort dict by value
        sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
        # print("Sorted distances:")
        belonging = {}
        groups = {}
        c = 0
        for k, v in sorted_distances.items():
            ...
            print(f"{c} -- {k}: {v}")
            if c >= 1000:
                break
            if k[0] in belonging and k[1] in belonging:
                if belonging[k[0]] == belonging[k[1]]:
                    print("both belong, continue\n")
                    c += 1
                    # continue
                else:
                    # breakpoint()
                    print("merging groups")
                    groups[belonging[k[0]]].extend(groups[belonging[k[1]]])
                    temp = belonging[k[1]]
                    for item in groups[belonging[k[1]]]:
                        belonging[item] = belonging[k[0]]
                    print(f"Deleting group {k[1]} - {belonging[k[1]]}, {temp=}")
                    del groups[temp]
                    c += 1
                    # continue
                for i in groups.values():
                    print(i, len(i))
                continue
            if k[0] in belonging:
                print("expanding k0", k, f"{belonging[k[0]]=}")
                groups[belonging[k[0]]].append(k[1])
                belonging[k[1]] = belonging[k[0]]
            elif k[1] in belonging:
                print("expanding k1")
                groups[belonging[k[1]]].append(k[0])
                belonging[k[0]] = belonging[k[1]]
            else:
                print("new group")
                groups[k[0]] = list(k)
                belonging[k[0]] = k[0]
                belonging[k[1]] = k[0]
            for i in groups.values():
                print(i, len(i))
            c += 1
        # print(f"Current groups: {groups.values()}\n")
        for i in sorted([len(i) for i in groups.values()], reverse=True)[:3]:
            #     print(i, len(i))
            result *= i
        # print(f"{sorted([len(i) for i in groups.values()], reverse=True)[:3]=}")

        return result

    def _calculate_2(self):
        # result = 1
        for x in self.__input_data:
            ...
            # print(f"Processing circuit {x.processed}")
        distances = {}
        for i in range(len(self.__input_data[:-1])):
            for j in range(i + 1, len(self.__input_data)):
                ll = self.__input_data[i].processed
                mm = self.__input_data[j].processed
                # print(i, j, l, m, dist(l,m))
                distances[(ll, mm)] = dist(ll, mm) ** 2
        # print(distances)
        # sort dict by value
        sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
        # print("Sorted distances:")
        belonging = {}
        groups = {}
        c = 0
        for k, v in sorted_distances.items():
            ...
            print(f"{c} -- {k}: {v}")
            if c >= 10000:
                break
            if k[0] in belonging and k[1] in belonging:
                if belonging[k[0]] == belonging[k[1]]:
                    print("both belong, continue\n")
                    c += 1
                    # continue
                else:
                    # breakpoint()
                    print("merging groups")
                    groups[belonging[k[0]]].extend(groups[belonging[k[1]]])
                    temp = belonging[k[1]]
                    for item in groups[belonging[k[1]]]:
                        belonging[item] = belonging[k[0]]
                    print(f"Deleting group {k[1]} - {belonging[k[1]]}, {temp=}")
                    del groups[temp]
                    c += 1
                    # continue
                for i in groups.values():
                    print(i, len(i))
                continue
            if k[0] in belonging:
                print("expanding k0", k, f"{belonging[k[0]]=}")
                groups[belonging[k[0]]].append(k[1])
                belonging[k[1]] = belonging[k[0]]
            elif k[1] in belonging:
                print("expanding k1")
                groups[belonging[k[1]]].append(k[0])
                belonging[k[0]] = belonging[k[1]]
            else:
                print("new group")
                groups[k[0]] = list(k)
                belonging[k[0]] = k[0]
                belonging[k[1]] = k[0]
            for i in groups.values():
                print(i, len(i))
            c += 1
            if sorted([len(i) for i in groups.values()], reverse=True) and sorted(
                [len(i) for i in groups.values()],
                reverse=True,
            )[0] == len(self.__input_data):
                print(k[0], k[1], "ALL GROUPED")
                return k[0][0] * k[1][0]
                break

        # print(f"Current groups: {groups.values()}\n")
        # for i in sorted([len(i) for i in groups.values()], reverse=True)[:3]:
