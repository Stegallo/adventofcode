from collections import defaultdict
from typing import NamedTuple

from .common import AoCDay
from .utils import collapse_strings


class UserGroup(NamedTuple):
    answers: defaultdict
    size: int


class Day(AoCDay):
    def __init__(self):
        super().__init__(6)

    def _preprocess_input(self, input_data):
        result = []
        for i in collapse_strings(input_data):
            d = defaultdict(int)
            for j in i.replace(" ", ""):
                d[j] += 1
            result.append(UserGroup(d, i.count(" ") + 1))
        return result

    def _calculate_1(self):
        return sum(len(i.answers) for i in self._input_data)

    def _calculate_2(self):
        return sum(v == i.size for i in self._input_data for k, v in i.answers.items())
