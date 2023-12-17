from typing import Optional, Tuple, List, Set

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay

from common.utilities import Grid
from collections import deque, defaultdict
from math import inf
# VISITED = set()

#DIRECTIONS
DOWN = ( 0, 1)
UP   = ( 0,-1)
LEFT = (-1, 0)
RIGH = ( 1, 0)

POT = defaultdict(lambda: inf)
@dataclass
class Cruc:
    grid: Grid

    def move(self, curr_pos = (0,0), dir = (1,0), visited = None, prev_dir = None, steps_dir = 0) -> None:
        # global VISITED
        # if curr_pos in VISITED:
        #     return inf
        # VISITED.add(curr_pos)
        if curr_pos in visited:
            return inf
        visited.add(curr_pos)

        # x = self.grid.grid[curr_pos]
        dest = (self.grid.col_num-1, self.grid.row_num-1)
        # dest = (2,1)
        # print(f"{dest=}")

        loss = 0

        # prev_dir = dir
        # c=0
        # # while True:
        # if True:
            # c+=1
        if not prev_dir:
            steps_dir=0
        if dir == prev_dir:
            steps_dir+=1
        try:
            value = int(self.grid.grid[curr_pos])
        except:
            return inf
        print(f"{curr_pos=},{value=},{dir=}, {steps_dir=}")
        if curr_pos == dest:
            return 0

        move_loss = 0
        possible_moves = []

        if dir == (1,0): # >
            possible_moves.extend([(0,1), (0,-1)])
        if dir == (-1,0): # <
            possible_moves.extend([(0,1), (0,-1)])
        if dir == (0,1): # v
            possible_moves.extend([(1,0), (-1,0)])
        if dir == (0,-1): # ^
            possible_moves.extend([(1,0), (-1,0)])
        if steps_dir<3:
            possible_moves.append(dir)
        # else:
            # print("can't continue straight")
        results = []
        print(f"{possible_moves=}")
        for i in possible_moves:
            print(f"move = {i}")
            nex_cruc = Cruc(self.grid)

            # print(f"move {(curr_pos[0]+i[0], curr_pos[1]+i[1]), i, dir, steps_dir}")
            try:
                future_val = int(self.grid.grid[(curr_pos[0]+i[0], curr_pos[1]+i[1])])
            except:
                print('esco perche non future_val')
                future_val = inf
                # break
            print(f"{curr_pos=}, {i=}, {move_loss}")
            move_loss = nex_cruc.move((curr_pos[0]+i[0], curr_pos[1]+i[1]), i, visited, dir, steps_dir)
            results.append(move_loss+future_val)

            if move_loss == 0:
                break

        print(f"{curr_pos=},{value=},{results=} result = {min(results) if results else inf}")

        # move_loss = nex_cruc.move(curr_pos, dir, dir, steps_dir)
        # print(f"{possible_moves=}")
        # print(f"{move_loss=}")
        return min(results) if results else inf

@dataclass
class Cru:
    grid: Grid
    pos: Tuple[int,int]
    dir: Tuple[int,int]
    steps_dir: int

    def __hash__(self) -> int:
        return hash((self.pos, self.dir))  # type: ignore

    @property
    def neib(self) -> Set:
        possible_moves = []
        out_of_bound = set()
        for i in (DOWN, UP, LEFT, RIGH):
            try:
                self.grid.grid[self.pos[0]+i[0], self.pos[1]+i[1]]
            except KeyError as e:
                out_of_bound.add(i)

        if self.dir == (1,0): # >
            possible_moves.extend([DOWN, UP])
        if self.dir == (-1,0): # <
            possible_moves.extend([DOWN, UP])
        if self.dir == (0,1): # v
            possible_moves.extend([RIGH, LEFT])
        if self.dir == (0,-1): # ^
            possible_moves.extend([RIGH, LEFT])
        if self.steps_dir<2:
            possible_moves.append(self.dir)
        # breakpoint()
        possible_moves = set(possible_moves)-out_of_bound
        # new_steps_dir = steps_dir+1 if self.dir == i else 0
        return {
            Cru(self.grid, (self.pos[0]+i[0], self.pos[1]+i[1]), i, self.steps_dir+1 if self.dir == i else 0)
            for i in possible_moves}

    @property
    def neib_cost(self):
        res = set()
        # print(f"{self.neib=}")
        # breakpoint()
        for i in self.neib:
            # print(f"{i=}")
            loss = int(self.grid.grid[self.pos[0]+i.dir[0], self.pos[1]+i.dir[1]])
            res.add((i, loss))
        return res

    def move(self):
        ...
class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        self.__input_data = Grid(self._input_data[0])

    def _calculate_1(self):
        x = self.__input_data
        # print(f"{x.grid}")
        cru = Cru(x, (0,0), (1,0), 0)
        res=0
        # print(f"{cru=}")
        POT[(cru.pos, cru.dir, cru.steps_dir)] = 0
        fringe = deque([cru])
        while fringe:
            c = fringe.popleft()
            # print(f"{c.pos=}")
            # breakpoint()
            for i in c.neib_cost:
                # print(f"{i[0].pos=}")
                if POT[c.pos, c.dir, c.steps_dir]+i[1] < POT[i[0].pos, i[0].dir, i[0].steps_dir]:
                    POT[i[0].pos, i[0].dir, i[0].steps_dir]=POT[c.pos, c.dir, c.steps_dir]+i[1]
                    fringe.append(i[0])
            # break
        # res = cruc.move((12,7), (0,1))
        # res = cruc.move((0,0), (0,1))
        # viz = set()
        # res = cruc.move((0,0), (1,0), viz)
        print(f"{len(POT.keys())=}, {fringe=}")
        dest = (x.col_num-1, x.row_num-1)
        results = [v for k,v in POT.items() if k[0] == dest]
        print(results)
        for i in sorted(POT):
            print(i, POT[i])
            # break
        return min(results)

    def _calculate_2(self):
        return 0
