from typing import List, Any

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class History:
    vals: List[int]

    @property
    def next(self) -> Any:
        return History(
            [
                int(self.vals[i + 1]) - int(self.vals[i])
                for i in range(len(self.vals) - 1)
            ],
        )

    def next_value(self) -> int:
        if set(self.vals) == {0}:
            return 0
        self.vals.append(self.vals[-1] + self.next.next_value())
        return self.vals[-1]

    def prev_value(self) -> int:
        if set(self.vals) == {0}:
            return 0
        self.vals.insert(0, self.vals[0] - self.next.prev_value())
        return self.vals[0]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [History(i.split(" ")) for i in self._input_data[0]]

    def _calculate_1(self) -> int:  # 2043183816
        return sum(x.next_value() for x in self.__input_data)

    def _calculate_2(self) -> int:  # 1118
        return sum(x.prev_value() for x in self.__input_data)
