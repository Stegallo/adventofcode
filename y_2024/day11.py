from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
import functools


@dataclass
class Row:
    original: str
    processed: Optional[list[str]] = None

    def __post_init__(self) -> None:
        self.processed = self.original.split(" ")


@functools.lru_cache(maxsize=128000000, typed=False)
def inner(i):
    # print(type(i))
    res = []
    # return res
    if i == "0":
        res.append("1")
        return res

    if len(i) % 2 == 0:
        res.append(str(int(i[: len(i) // 2])))
        res.append(str(int(i[len(i) // 2 :])))
        return res

    res.append(str(int(i) * 2024))
    return res


@functools.lru_cache(maxsize=128000000, typed=False)
def calc_len(stones, i):
    stones = stones.split("#")
    if i == 1:
        # print(stones)
        return len(stones)

    r = 0
    for j in stones:
        # print(f"stone: {j}")
        x = inner(j)
        # print(f"flipped: {x}")
        rex = calc_len("#".join(x), i - 1)
        # print(f"{rex=}")
        # continue
        r += rex

    return r


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
        # for x in self.__input_data[:3]:
        #     print(f"{x}")
        # print('.')
        # print('.')
        # for x in self.__input_data[-3:]:
        #     print(f"{x}")
        #     ...

    def _calculate_1(self):
        # 0 1 10 99 999

        result = 0
        return 0
        state = []
        for j in self.__input_data:
            for x in j.processed:
                # print(x)
                state.append(x)
        # print(state)
        for _ in range(75):
            # for i in range(6):
            new_state = []
            for i in state:
                print(i)

            # print(new_state)
            state = list(new_state)
        result = len(state)
        return result

    def _calculate_2(self):
        result = 0
        state = []
        for j in self.__input_data:
            for x in j.processed:
                # print(x)
                state.append(x)
        # print(state)
        repeated = {}
        T = 75
        return calc_len("#".join(state), T + 1)
        l = len(state)  # noqa: E741
        for progr in range(75):
            # for progr in range(25):
            # for progr in range(6):
            l = 0  # noqa: E741
            new = set()
            new_state = []
            for i in state:
                # print(i)
                new_state.extend(inner(i))
                if i not in repeated:
                    # new.add(i)
                    rez = inner(i)
                    # print(rez,len(rez))
                    repeated[i] = len(rez)
                # print(l)
                l += repeated[i]  # noqa: E741
            # print(new_state)
            state = list(new_state)
            print(progr)
            print(f"{len(new)=}, {len(repeated)=}, {l=}")

        result = len(state)
        return result
