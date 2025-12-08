from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid, Point, Cursor, Direction


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        # print(f"{len(self._input_data)=}")
        # print(f"{len(self._input_data[0])=}")
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()
        # self.__input_data = [Row(i) for i in self._input_data[0]]
        # self.__input_data = [Row(i) for j in self._input_data for i in j]
        # for x in self.__input_data:
        #     print(f"{x}")

    def _calculate_1(self):
        result = 0
        # print(len(self.grid.values['S']))
        # print(len(self.grid.values['^']))
        s = self.grid.values['S'][0]
        next_row = set([s])
        for i in range(self.grid.height):
            # print(i)
            beams = [i for i in next_row]
            if not beams:
                break
            # print(f"{i}, Beams to process: {len(beams)=}, {beams=}")
            next_row = set()
            for p in beams:
                b = Cursor(p, Direction.from_symbol('v'))
                # print(f"Processing {b}", self.grid.grid.get(b.ahead()))
                if self.grid.grid.get(b.ahead()) == '.':
                    next_row.add(b.ahead())
                    # self.grid.grid[b.ahead()] = '|'
                if self.grid.grid.get(b.ahead()) == '^':
                # else:
                #     # print(b.ahead().x)
                    result+=1
                    next_row.add(Point(b.ahead().x-1, b.ahead().y))
                    next_row.add(Point(b.ahead().x+1, b.ahead().y))
                    # self.grid.grid[Point(b.ahead().x-1, b.ahead().y+1)] = '|'
                    # self.grid.grid[Point(b.ahead().x+1, b.ahead().y+1)] = '|'
            # print(result)
            # self.grid.display()
        #     ...
        return result
        # 2925 too high

    def _calculate_2(self):
        result = 0
        return result
