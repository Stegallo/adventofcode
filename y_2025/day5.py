from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Range:
    original: str
    begin: Optional[int] = None
    end: Optional[int] = None

    def __post_init__(self) -> None:
        processed = [int(i) for i in self.original.split("-")]
        self.begin = processed[0]
        self.end = processed[1]


@dataclass
class Ingredient:
    original: str
    id: Optional[int] = None

    def __post_init__(self) -> None:
        self.id = int(self.original)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.ranges = [Range(i) for i in self._input_data[0]]
        self.ingredients = [Ingredient(i) for i in self._input_data[1]]

    def _calculate_1(self):
        result = 0
        for ingredient in self.ingredients:
            found = 0
            for r in self.ranges:
                if ingredient.id >= r.begin and ingredient.id <= r.end:
                    found = 1
                    break
            if found == 1:
                result += 1
        return result

    def _calculate_2(self):
        result = 0
        self.ranges.sort(key=lambda x: (x.begin, x.end))
        current_interval = self.ranges[0]

        for r in self.ranges[1:]:
            if r.begin <= current_interval.end + 1:
                current_interval.end = max(current_interval.end, r.end)
            else:
                result += current_interval.end - current_interval.begin + 1
                current_interval = r
        return result + (current_interval.end - current_interval.begin + 1)
