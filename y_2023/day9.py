from typing import List, Any

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Row:
    history: List[int]

    @property
    def next(self) -> Any:
        return Row(
            [
                int(self.history[i + 1]) - int(self.history[i])
                for i in range(len(self.history) - 1)
            ],
        )

    def next_value(self) -> int:
        if set(self.history) == {0}:
            return 0
        self.history.append(self.history[-1] + self.next.next_value())
        return self.history[-1]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i.split(" ")) for i in self._input_data[0]]

    def _calculate_1(self) -> int:  # 2043183816
        return sum(x.next_value() for x in self.__input_data)

    def _calculate_2(self) -> int:  # 1118
        return 0
