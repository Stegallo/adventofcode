from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.utilities import Grid
from math import inf
G = {}

#DIRECTIONS
DOWN = ( 0, 1)
UP   = ( 0,-1)
LEFT = (-1, 0)
RIGH = ( 1, 0)

MAP = {'D': DOWN, 'U': UP, 'L': LEFT, 'R': RIGH}
@dataclass
class Row:
    dir: str
    steps: int
    color: str

@dataclass
class Point:
    x: int
    y: int

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(*i.split(' ')) for i in self._input_data[0]]

    def _calculate_1(self):
        start = Point(0,0)
        points = [start]
        curr = start
        perim = 0
        for c, x in enumerate(self.__input_data):
            dir = [(x.steps)*i for i in MAP[x.dir]]
            perim += x.steps
            curr = Point(curr.x+dir[0],curr.y+dir[1])
            points.append(curr)
        shoelace = 0
        for c, i in enumerate(points):
            if c==0:
                continue
            sour = points[c-1]
            dest = points[c]
            v = sour.x*dest.y-sour.y*dest.x
            shoelace+=v

        return abs(shoelace)//2+perim//2+1

    def _calculate_2(self):
        return 0
