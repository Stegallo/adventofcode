from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = [int(i) for i in self.original.split()]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        print(f"{self._input_data=}")
        self.__input_data = [Row(i) for i in self._input_data[0]]

    def _calculate_1(self):
        r = 0
        for x in self.__input_data:
            y = x.processed
            si = True
            sd = True
            for c, i in enumerate(y):
                if c == 0:
                    continue
                if y[c] - y[c - 1] not in (1, 2, 3):
                    si = False
                if y[c - 1] - y[c] not in (1, 2, 3):
                    sd = False
            if si or sd:
                r += 1
        return r

    def _calculate_2(self):
        r = 0
        for x in self.__input_data:
            y = x.processed
            si = True
            sd = True
            for c, i in enumerate(y):
                if c == 0:
                    continue
                if y[c] - y[c - 1] not in (1, 2, 3):
                    si = False
                if y[c - 1] - y[c] not in (1, 2, 3):
                    sd = False
            if si or sd:
                r += 1
            else:
                found = False
                for rem in range(len(y)):
                    if found:
                        break
                    new_y = y[:rem] + y[rem + 1 :]
                    ssi = True
                    ssd = True
                    for c, i in enumerate(new_y):
                        if c == 0:
                            continue
                        if new_y[c] - new_y[c - 1] not in (1, 2, 3):
                            ssi = False
                        if new_y[c - 1] - new_y[c] not in (1, 2, 3):
                            ssd = False
                    if ssi or ssd:
                        r += 1
                        found = True
        return r
