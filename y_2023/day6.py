from common.aoc import AoCDay
from typing import List, Optional
from pydantic.dataclasses import dataclass


@dataclass
class Placeholder:
    name: str
    orig_sequence: str
    sequence: Optional[List[int]] = None
    sequence_kernig: Optional[int] = None

    def __post_init__(self) -> None:
        self.sequence = [int(i) for i in self.orig_sequence.split()]
        self.sequence_kernig = int(self.orig_sequence.replace(" ", ""))

    @property
    def size(self):
        return len(self.sequence)


class Time(Placeholder):
    ...


class Distance(Placeholder):
    ...


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def _calculate_1(self) -> int:  # 227850
        time = Time(*self.__input_data[0].split(":"))
        distance = Distance(*self.__input_data[1].split(":"))

        result = 1
        for i in range(time.size):
            local_res = 0
            for j in range(time.sequence[i] + 1):  # type: ignore
                if j * (time.sequence[i] - j) > distance.sequence[i]:  # type: ignore
                    local_res += 1

            result *= local_res
        return result

    def _calculate_2(self) -> int:  # 42948149
        time = Time(*self.__input_data[0].split(":"))
        distance = Distance(*self.__input_data[1].split(":"))

        result = 1
        local_res = 0
        for j in range(time.sequence_kernig + 1):  # type: ignore
            if j * (time.sequence_kernig - j) > distance.sequence_kernig:  # type: ignore # noqa: E501
                local_res += 1

        result *= local_res
        return result
