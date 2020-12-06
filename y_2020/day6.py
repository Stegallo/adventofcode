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

    def _preprocess_input(self):
        self.__user_groups = [
            UserGroup(
                Counter(group_string.replace(" ", "")), group_string.count(" ") + 1
            )
            for group_string in collapse_strings(self._input_data)
        ]

    def _calculate_1(self):
        return sum(len(group.answers) for group in self.__user_groups)

    def _calculate_2(self):
        return sum(
            v == group.size
            for group in self.__user_groups
            for k, v in group.answers.items()
        )
