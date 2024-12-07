from typing import Optional

from pydantic.dataclasses import dataclass
from collections import defaultdict
from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original


@dataclass
class Rule:
    original: str
    processed: Optional[list[str]] = None

    def __post_init__(self) -> None:
        self.processed = self.original.split("|")


@dataclass
class Update:
    original: str
    processed: Optional[list[str]] = None

    def __post_init__(self) -> None:
        self.processed = self.original.split(",")


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data_1 = [Rule(i) for i in self._input_data[0]]
        self.__input_data_2 = [Update(i) for i in self._input_data[1]]

    def _calculate_1(self):
        result = 0
        foll = defaultdict(list)
        prec = defaultdict(list)
        for x in self.__input_data_1:
            foll[x.processed[0]].append(x.processed[1])
            prec[x.processed[1]].append(x.processed[0])

        self.valids = []
        for x in self.__input_data_2:
            valid = True
            for c, i in enumerate(x.processed):
                for d, j in enumerate(x.processed[c + 1 :]):
                    if j not in foll[i]:
                        valid = False
            if valid:
                result += int(x.processed[len(x.processed) // 2])
                self.valids.append(x.processed)

        return result

    def _calculate_2(self):
        result = 0
        foll = defaultdict(list)
        orfoll = defaultdict(list)

        for x in self.__input_data_1:
            foll[x.processed[0]].append(x.processed[1])
            orfoll[x.processed[0]].append(x.processed[1])

        for x in self.__input_data_2:
            valid = True
            for c, i in enumerate(x.processed):
                for d, j in enumerate(x.processed[c + 1 :]):
                    # print(i,j)
                    if j not in orfoll[i]:
                        valid = False
            if valid:
                pass
            else:
                proposed = list(x.processed)
                valid_p = False
                while not valid_p:
                    ordered = True
                    for i in range(len(proposed) - 1):
                        j = i + 1
                        if proposed[j] not in foll[proposed[i]]:
                            ordered = False
                            proposed[j], proposed[i] = proposed[i], proposed[j]
                    if ordered:
                        valid_p = True
                        break

                result += int(proposed[len(proposed) // 2])

        return result
