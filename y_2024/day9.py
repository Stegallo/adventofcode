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
        return 0
        r = []
        for c, x in enumerate(self.__input_data[0].original):
            # print(f"{c//2=},{c%2=},{c=}{x=}")
            m = c // 2 if c % 2 == 0 else "."
            # print(f"{m=}, {x=}")
            for i in range(int(x)):
                r.append(Elem(str(m)))
            # r.append(v)
            # print(f"{v=}")
            ...
        # print(r)
        # string = list(''.join(r))
        print("here")
        len_file = len([i for i in r if i.x != "."])
        # print(f"{string=}, {len_file=}")
        print(f"{len_file=}")
        print(f"here, {len_file=}")
        c = 0
        # d=0
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
            # print(f"{c//2=},{c%2=},{c=}{x=}")
            m = c // 2 if c % 2 == 0 else "."
            # print(f"{m=}, {x=}")
            for i in range(int(x)):
                r.append(Elem(str(m)))
            # r.append(v)
            # print(f"{v=}")
            ...
        # print(r)
        # string = list(''.join(r))
        print("here")
        len_file = len([i for i in r if i.x != "."])
        # print(f"{string=}, {len_file=}")
        print(f"{len_file=}")
        print(f"here, {len_file=}")
        # chunks
        chunks = []
        chunks2 = []
        c = []
        c2 = []
        x = r[-1]
        c.append(x)
        c2.append(len(r) - 1)
        for i in range(1, len(r)):
            # print(i)
            if r[-1 - i].x == x.x:
                # print(r[-1-i].x,x.x)
                c.append(r[len(r) - 1 - i])
                c2.append(len(r) - 1 - i)
            else:
                # print(r[-1-i].x,x.x)
                if c[0].x != ".":
                    chunks.append(c)
                    chunks2.append(c2[::-1])
                c = []
                c2 = []
                x = r[-1 - i]
                c.append(x)
                c2.append(len(r) - 1 - i)
        # print(chunks)

        # for c,i in enumerate(chunks):
        #     print(i,chunks2[c])
        # print('now')

        # free slots
        slots = []
        slo = deque()
        for i in range(len(r)):
            if r[i].x == ".":
                slo.append(i)
            else:
                if len(slo) > 0:
                    slots.append(slo)
                slo = deque()
        # for i in slots:
        # print(i)
        # return
        c = 0
        # d=0
        print(len(r), r[-60:])
        print("tada\n\n\n")
        for c, i in enumerate(chunks):
            #     # x = chunks[len(chunks)-1-i]
            # print(i, len(i))
            for j in range(len(slots)):
                # print(j,len(j))

                if len(i) <= len(slots[j]):
                    if slots[j][0] > chunks2[c][0]:
                        break
                    # print("swap")
                    # print(chunks2[c])

                    for m in chunks2[c]:
                        # print(m)
                        r[m] = Elem("#")
                        n = slots[j].popleft()
                        # print(r[n],i[0], len(i))
                        # if r[n].x!='.':
                        #     breakpoint()
                        r[n] = i[0]
                    break
        print(len(r), r[-60:])
        print("".join([i.x for i in r]))
        result = 0
        for c, i in enumerate(r):
            # print(i)
            if i.x not in ["#", "."]:
                result += c * int(i.x)
        # 8504654861152 too high
        return result
