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
    res = []
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
        return len(stones)

    r = 0
    for j in stones:
        x = inner(j)

        rex = calc_len("#".join(x), i - 1)

        r += rex

    return r


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        state = []
        for j in self.__input_data:
            for x in j.processed:
                state.append(x)

        T = 25
        return calc_len("#".join(state), T + 1)

    def _calculate_2(self):
        state = []
        for j in self.__input_data:
            for x in j.processed:
                state.append(x)

        T = 75
        return calc_len("#".join(state), T + 1)
