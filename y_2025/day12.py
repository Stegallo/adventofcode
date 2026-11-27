from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


# @dataclass
# class Row:
#     original: str
#     processed: Optional[str] = None

#     def __post_init__(self) -> None:
#         self.processed = ""  # self.original


@dataclass
class Gift:
    original: list
    index: Optional[int] = None
    shape: Optional[list[str]] = None

    def __post_init__(self) -> None:
        self.index = int(self.original[0][:-1])
        self.shape = [i for i in self.original[1:]]

    def size(self):
        r = 0
        for i in self.shape:
            for j in i:
                r += 1 if j == "#" else 0
            # print(i)
        return r


@dataclass
class Region:
    original: str
    x: Optional[int] = None
    y: Optional[int] = None
    boxes: Optional[list[int]] = None

    def __post_init__(self) -> None:
        # print()
        coord = self.original.split(":")[0].split("x")
        self.x = int(coord[0])
        self.y = int(coord[1])
        self.boxes = [int(i) for i in self.original.split(":")[1].split()]

    def area(self):
        return self.x * self.y


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
        # self.__input_data = [Row(i) for j in self._input_data for i in j]
        # for x in self.__input_data:
        #     print(f"{x}")
        # for i in self._input_data[:-1]:
        #     # print(int(i[0][:-1]))
        #     # print(i[1:])
        #     print(i)
        #     print(Gift(i))
        # print(f"{[Region(i) for i in  self._input_data[-1]]=}")
        self.gifts = [Gift(i) for i in self._input_data[:-1]]
        self.regions = [Region(i) for i in self._input_data[-1]]

    def _calculate_1(self):
        result = 0
        d = {}
        for x in self.gifts:
            # print(x, x.size())
            d[x.index] = x

        k = 0
        for x in self.regions:
            o = 0
            for c, i in enumerate(x.boxes):
                # print(c, i, d[c].size())
                o += i * d[c].size()
            if o > x.area():
                continue
            print(x, x.area(), o, {o > x.area()})
            k += 1
        print(k)

        return result

    def _calculate_2(self):
        result = 0
        return result
