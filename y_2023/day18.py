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

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = [Row(*i.split(' ')) for i in self._input_data[0]]

    def _calculate_1(self):
        max_c = -inf
        max_r = -inf
        min_c = inf
        min_r = inf
        start = (0,0)
        curr = start
        for x in self.__input_data:
            dir = MAP[x.dir]
            # print(f"{x}, {dir}")
            for i in range(x.steps):
                curr = (curr[0]+dir[0], curr[1]+dir[1])
                if curr[0]+dir[0] > max_c:
                    max_c = curr[0]+dir[0]
                if curr[1]+dir[1] > max_r:
                    max_r = curr[1]+dir[1]
                if curr[0]+dir[0] < min_c:
                    min_c = curr[0]+dir[0]
                if curr[1]+dir[1] < min_r:
                    min_r = curr[1]+dir[1]
                # print(f"{curr}")
                G[curr] = '#' # x.color
        # print(f"{G=}, {len(G)}, {min_c=}, {min_r=}, {max_c=}, {max_r=}")
        contour = Grid.from_grid(G, frame=1)
        contour.viz()
        grid = []
        for i in range(max_r-min_r+1):
            break
            1/0
            row = []
            insid=False
            on_bord=False
            prev_on_bord = on_bord
            for j in range(max_c-min_c+1):
                pos=(min_c+j,min_r+i)
                if G.get(pos):
                    on_bord = True
                if not G.get(pos):
                    on_bord = False

                if prev_on_bord and not on_bord:
                        insid = not insid
                if pos[0]==max_c:
                    insid = False
                if pos[1]==max_r:
                    insid = False
                # if G.get((j,i)) and not insid:
                #     insid = True
                # if not G.get((j,i)) and on_bord:
                #     insid = False
                # if orig_on_bord != on_bord:
                #     insid = not insid
                # print(f"{pos} {prev_on_bord=}\t{on_bord=} {insid=}, {max_c=}, {pos[0]=}")
                # if not G.get((j,i)) and insid:
                #     insid = True
                # if G.get((j,i)) and insid:
                #     insid = True
                if G.get(pos) or insid:
                    row.append( '#' )
                if not G.get(pos) and not insid:
                    row.append( '.' )
                prev_on_bord = on_bord
            grid.append(''.join(row))
            # print(''.join(row))

        for j in contour.dia1:
            print(j)
            # print()
            # continue
            row = []
            insid=False
            on_bord=False
            # prev_on_bord = on_bord
            for i in j:
                if i == '#':
                    insid = not insid
                #     on_bord = True
                # else:
                #     on_bord = False

                # if prev_on_bord and not on_bord:
                #     insid = not insid
                if i == '#' or insid:
                    row.append( '#' )
                if i != '#' and not insid:
                    row.append( '.' )
                # prev_on_bord = on_bord
            print((''.join(row)))
            grid.append(''.join(row))
            print()
        # g = contour
        # g = Grid(grid)
        # g.viz()
        # g.grid = {k:v if v=='#' else '.' for k,v in g.grid.items()}
        # g.grid = {k:v for k,v in g.grid.items() if v=='#' }
        print(f"{grid=}")
        result = 0
        for r in grid:
            print(r)
            print([i for i in r if i=='#'])
            result+=len([i for i in r if i=='#'])

        # for j in g.rows:
        #     print(j)
        #     for i in j:
        #         # print(i)
        #         pass
        # 57330 low
        # 57590 low
        # 57590
        return result #len(g.grid)

    def _calculate_2(self):
        return 0
