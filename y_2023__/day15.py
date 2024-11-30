from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from collections import defaultdict


@dataclass
class Row:
    original: str
    label: Optional[str] = None
    operation: Optional[str] = None

    def __post_init__(self) -> None:
        # breakpoint(/)
        self.label = self.original.split("=")[0].split("-")[0]
        self.operation = self.original.replace(self.label, "")[0]

    def compute_hash(self) -> int:
        current = 0
        for i in self.original:
            current += ord(i)
            current = current * 17
            current = current % 256
            # print(current)
        return current

    def compute_hash_on_label(self) -> int:
        current = 0
        for i in self.label:  # type: ignore
            current += ord(i)
            current = current * 17
            current = current % 256
            # print(current)
        return current


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = [Row(i) for i in self._input_data[0][0].split(",")]

    def _calculate_1(self):
        result = 0
        return result
        for x in self.__input_data:
            # print(f"{x}, {x.compute_hash()}")
            result += x.compute_hash()
        return result

    def _calculate_2(self):
        boxes = defaultdict(list)
        for x in self.__input_data:
            hash = x.compute_hash_on_label()
            print(f"{x}, {hash}")
            if x.operation == "=":
                lab = boxes[hash]
                found = False
                for i in lab:
                    if x.label in i:
                        found = True
                        break
                if not found:
                    boxes[hash].append(x.original)
                if found:
                    boxes[hash] = [
                        i if x.label not in i else x.original for i in boxes[hash]
                    ]
            if x.operation == "-":
                boxes[hash] = [i for i in boxes[hash] if x.label not in i]

        result = 0
        for k, v in boxes.items():
            res_1 = k + 1
            for c, i in enumerate(v):
                # print(k, v, c+1, int(i.split('=')[1]))
                print(res_1 * (c + 1) * int(i.split("=")[1]))
                result += res_1 * (c + 1) * int(i.split("=")[1])
        return result
