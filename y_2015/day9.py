import re
from collections import defaultdict
from itertools import permutations
from typing import Dict

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Route:
    start: str
    end: str
    distance: int


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [
            Route(*list(re.search(r"(.*) to (.*) = (\d*)", x).groups()))
            for x in self._input_data[0]
        ]
        self.__cities = set()
        for i in self.__input_data:
            self.__cities.add(i.start)
            self.__cities.add(i.end)

    def _calculate_1(self) -> int:
        n_cities = len(self.__cities)
        distances: Dict[str, Dict[str, int]] = defaultdict(dict)
        for x in self.__input_data:
            distances[x.start][x.end] = x.distance
            distances[x.end][x.start] = x.distance
        min_dist = 100_000
        for i in permutations(self.__cities):
            dist = sum(distances[i[c]][i[c + 1]] for c in range(n_cities - 1))
            if dist < min_dist:
                min_dist = dist
        return min_dist

    def _calculate_2(self) -> int:
        n_cities = len(self.__cities)
        distances: Dict[str, Dict[str, int]] = defaultdict(dict)
        for x in self.__input_data:
            distances[x.start][x.end] = x.distance
            distances[x.end][x.start] = x.distance
        max_dist = -1
        for i in permutations(self.__cities):
            dist = sum(distances[i[c]][i[c + 1]] for c in range(n_cities - 1))
            if dist > max_dist:
                max_dist = dist
        return max_dist
