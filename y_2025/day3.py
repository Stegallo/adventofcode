from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = [int(i) for i in self.original]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for j in self._input_data for i in j]

    def _calculate_1(self):
        result = 0
        for x in self.__input_data:
            highest = 0
            for c, y in enumerate(x.processed):
                if c == len(x.processed) - 1:
                    continue
                for d, z in enumerate(x.processed):
                    if d <= c:
                        continue
                    t = int(str(y) + str(z))
                    if t > highest:
                        highest = t
            result += highest
        return result

    def _calculate_2(self):
        result = 0
        for x in self.__input_data:
            on = x.processed[-12:]
            for i in range(len(x.processed) - 12 - 1, -1, -1):
                bat = x.processed[i]
                for c, v in enumerate(on):
                    if bat >= v:
                        on[c], bat = bat, on[c]
                    else:
                        break
            result += int("".join([str(i) for i in on]))
        return result
