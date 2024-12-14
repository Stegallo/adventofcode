from typing import Optional

from pydantic.dataclasses import dataclass
from collections import deque
from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original


@dataclass
class Elem:
    x: str


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        print(f"{self._input_data=}")
        # print(f"{len(self._input_data)=}")
        # print(f"{len(self._input_data[0])=}")
        # self.grid = Grid.from_input(self._input_data)
        # self.grid.display()
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        result = 0
        r = []
        for c, x in enumerate(self.__input_data[0].original):
            m = c // 2 if c % 2 == 0 else "."

            for i in range(int(x)):
                r.append(Elem(str(m)))

        c = 0

        for i in range(len(r) - 1):
            x = r[len(r) - 1 - i].x
            try:
                while r[c].x != ".":
                    c += 1
                r[c].x = x
                r[len(r) - 1 - i] = Elem("#")
            except Exception:
                break
        result = 0
        for c, i in enumerate(r):
            if i.x != "#":
                result += c * int(i.x)

        return result

    def _calculate_2(self):
        result = 0
        r = []
        for c, x in enumerate(self.__input_data[0].original):
            m = c // 2 if c % 2 == 0 else "."

            for i in range(int(x)):
                r.append(Elem(str(m)))

        chunks = []
        chunks2 = []
        c = []
        c2 = []
        x = r[-1]
        c.append(x)
        c2.append(len(r) - 1)
        for i in range(1, len(r)):
            if r[-1 - i].x == x.x:
                c.append(r[len(r) - 1 - i])
                c2.append(len(r) - 1 - i)
            else:
                if c[0].x != ".":
                    chunks.append(c)
                    chunks2.append(c2[::-1])
                c = []
                c2 = []
                x = r[-1 - i]
                c.append(x)
                c2.append(len(r) - 1 - i)

        slots = []
        slo = deque()
        for i in range(len(r)):
            if r[i].x == ".":
                slo.append(i)
            else:
                if len(slo) > 0:
                    slots.append(slo)
                slo = deque()

        c = 0

        for c, i in enumerate(chunks):
            for j in range(len(slots)):
                if len(i) <= len(slots[j]):
                    if slots[j][0] > chunks2[c][0]:
                        break

                    for m in chunks2[c]:
                        r[m] = Elem("#")
                        n = slots[j].popleft()

                        r[n] = i[0]
                    break

        result = 0
        for c, i in enumerate(r):
            if i.x not in ["#", "."]:
                result += c * int(i.x)

        return result
