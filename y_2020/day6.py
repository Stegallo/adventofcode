import re
from .common import AoCDay
from .utils import collapse_strings, dict_from_string
from collections import defaultdict


class Day(AoCDay):
    def __init__(self):
        super().__init__(6)

    def _preprocess_input(self, input_data):
        p_list = []
        for p_string in collapse_strings(input_data):
            p_list.append(p_string)
        return p_list

    def _calculate_1(self):
        c = 0
        for i in self._input_data:
            d = defaultdict(int)
            for j in i:
                if j != " ":
                    d[j] += 1
            c += len(d)

        return c

    def _calculate_2(self):
        c = 0
        for i in self._input_data:
            users = i.count(" ") + 1
            d = defaultdict(int)
            for j in i:
                if j != " ":
                    d[j] += 1
            for k in d:
                if d[k] == users:
                    c += 1

        return c
