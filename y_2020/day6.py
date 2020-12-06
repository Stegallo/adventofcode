from collections import Counter
from typing import NamedTuple

from .common import AoCDay
from .utils import collapse_strings


class UserGroup(NamedTuple):
    answers: Counter
    size: int


class Day(AoCDay):
    def __init__(self):
        super().__init__(6)

    def _preprocess_input(self, input_data):
        return [
            UserGroup(Counter(i.replace(" ", "")), i.count(" ") + 1)
            for i in collapse_strings(input_data)
        ]

    def _calculate_1(self):
        return sum(len(i.answers) for i in self._input_data)

    def _calculate_2(self):
        return sum(v == i.size for i in self._input_data for k, v in i.answers.items())
