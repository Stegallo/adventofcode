from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay

VISITED = {}

@dataclass
class Row:
    original: str
    row: int
    has_s: Optional[bool] = False
    s_column: Optional[int] = 0

    def __post_init__(self) -> None:
        if 'S' in self.original:
            self.has_s = True
            self.s_column = self.original.index('S')

@dataclass
class Pos:
    x:int
    y:int

    @property
    def border(self):
        return [
            (self.x + y - 1, self.y + x - 1)
            for x in range(3)
            for y in range(3)
            if x!=1 or y!=1
        ]

    @property
    def up(self):
        return (self.x, self.y - 1)

    @property
    def down(self):
        return (self.x, self.y + 1)

    @property
    def left(self):
            return (self.x -1, self.y)

    @property
    def right(self):
            return (self.x +1, self.y)


def navigate(current_pos, pipes, start=False):
    # current_pos = Pos(*list(locs.keys())[0])
    heads = []
    up=False
    down=False
    left=False
    right=False
    # if heads and heads[0] == heads[1]:
    #     return []
    # print(f"{current_pos=}")
    # print(f"{current_pos.border=}")
    if current_pos.up in pipes:
        if (pipes[current_pos.x,current_pos.y] not in ('F', '7')) and pipes[current_pos.up] in ('|', 'F', '7') and current_pos.up not in VISITED and (pipes[current_pos.x,current_pos.y] != pipes[current_pos.up] or pipes[current_pos.up] == '|') and (not pipes[current_pos.x,current_pos.y] == '-'):
            # print(pipes[current_pos.up])
            heads.append((current_pos.up, pipes[current_pos.up]))
            VISITED[current_pos.up] = pipes[current_pos.up]
            up=True

    if current_pos.down in pipes:
        if (pipes[current_pos.x,current_pos.y] not in ('L', 'J')) and pipes[current_pos.down] in ('|', 'L', 'J') and current_pos.down not in VISITED and (pipes[current_pos.x,current_pos.y] != pipes[current_pos.down] or pipes[current_pos.down] == '|') and (not pipes[current_pos.x,current_pos.y] == '-'):
            # print(pipes[current_pos.down])
            heads.append((current_pos.down, pipes[current_pos.down]))
            VISITED[current_pos.down] = pipes[current_pos.down]
            down=True

    if current_pos.left in pipes:
        if (pipes[current_pos.x,current_pos.y] not in ('L', 'F')) and pipes[current_pos.left] in ('-', 'F', 'L')  and current_pos.left not in VISITED and (pipes[current_pos.x,current_pos.y] != pipes[current_pos.left] or pipes[current_pos.left] == '-') and (not pipes[current_pos.x,current_pos.y] == '|'):
            # print(pipes[current_pos.left])
            heads.append((current_pos.left, pipes[current_pos.left]))
            VISITED[current_pos.left] = pipes[current_pos.left]
            left=True

    if current_pos.right in pipes:
        if (pipes[current_pos.x,current_pos.y] not in ('7', 'J')) and pipes[current_pos.right] in ('-', '7', 'J')  and current_pos.right not in VISITED and (pipes[current_pos.x,current_pos.y] != pipes[current_pos.right] or pipes[current_pos.right] == '-') and (not pipes[current_pos.x,current_pos.y] == '|'):
            # print(pipes[current_pos.right])
            heads.append((current_pos.right, pipes[current_pos.right]))
            VISITED[current_pos.right] = pipes[current_pos.right]
            right=True
    # print(heads)
    if start:
        if up and down:
            VISITED[(current_pos.x,current_pos.y)]='|'
        if left and right:
            VISITED[(current_pos.x,current_pos.y)]='-'
        if up and right:
            VISITED[(current_pos.x,current_pos.y)]='L'
        if up and left:
            VISITED[(current_pos.x,current_pos.y)]='J'
        if down and right:
            VISITED[(current_pos.x,current_pos.y)]='F'
        if down and left:
            VISITED[(current_pos.x,current_pos.y)]='7'

    return heads

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = [Row(i, c) for c, i in enumerate(self._input_data[0])]

    def _calculate_1(self) -> int: # 6649
        locs = {}
        pipes = {}
        for x in self.__input_data:
            # print(f"{x}")
            if x.has_s:
                locs[(x.s_column, x.row)] = 'S'
        for x in self.__input_data:
            for c, y in enumerate(x.original):
                if y != '.':
                    pipes[(c, x.row)] = y
        # print(locs)
        # print(f"{pipes=}")
        current_pos = Pos(*list(locs.keys())[0])
        VISITED[list(locs.keys())[0]]='S'
        heads = []
        x = navigate(current_pos, pipes, True)
        # x = navigate(current_pos, pipes)
        print(x)
        x1 = navigate(Pos(*x[0][0]), pipes)
        x2 = navigate(Pos(*x[1][0]), pipes)
        # print(f"{x1=}")
        # print(f"{x2=}")
        c=1
        while x1 != x2:
            c+=1
            if not x1 or not x2:
                break
            # if x1 == [((117, 41), 'J')]:
            #     breakpoint()
            # F
            # JJ
            # CURRENT = set()
            # if x1 == [((118, 40), '-')]:
            #     breakpoint()
            x1 = navigate(Pos(*x1[0][0]), pipes)
            x2 = navigate(Pos(*x2[0][0]), pipes)
            # print(f"{x1=}")
            # print(f"{x2=}")
            # if x1 == x2:
            #     break
            # print(f"{VISITED=}")
            # print(f"{CURRENT=}")
            # if not x:


            # current_pos = Pos(*list(locs.keys())[0])
            # heads = []
            # print(current_pos)
            # print(f"{current_pos.border=}")
            # if current_pos.up in pipes:
            #     if pipes[current_pos.up] in ('|', 'F', '7'):
            #         print(pipes[current_pos.up])
            #         heads.append((current_pos.up, pipes[current_pos.up]))
            # if current_pos.down in pipes:
            #     if pipes[current_pos.down] in ('|', 'L', 'J'):
            #         print(pipes[current_pos.down])
            #         heads.append((current_pos.down, pipes[current_pos.down]))
            # if current_pos.left in pipes:
            #     if pipes[current_pos.left] in ('-', 'F', 'L'):
            #         print(pipes[current_pos.left])
            #         heads.append((current_pos.left, pipes[current_pos.left]))
            # if current_pos.right in pipes:
            #     if pipes[current_pos.right] in ('-', '7', 'J'):
            #         print(pipes[current_pos.right])
            #         heads.append((current_pos.right, pipes[current_pos.right]))
            # print(heads)
            # for i in current_pos.border:
            #     if i in pipes :
            #         if current_pos
            #         print(i, pipes[i])

            # break
        return c

    def _calculate_2(self):
        pipes = {}
        for x in self.__input_data:
            for c, y in enumerate(x.original):
                # if y != '.':
                    pipes[(c, x.row)] = y
        # print(VISITED)
        xs = []
        ys = []
        for i in VISITED:
            p = Pos(*i)
            xs.append(p.x)
            ys.append(p.y)
        min_x =min(xs)-1
        min_y =min(ys)-1
        max_x =max(xs)+2
        max_y =max(ys)+2
        # print(min_x, min_y, max_x, max_y)
        inside_ = []
        rows=[]
        for i in range(max_y-min_y):
            row = []
            row1 = []
            in_loop = False
            open_border_f = False
            open_border_l = False
            for j in range(max_x-min_x):
                # row.append(VISITED.get((min_x+j, min_y+i), '#'))
                pipe = VISITED.get((min_x+j, min_y+i))
                element = pipes.get((min_x+j, min_y+i))
                row.append(pipe or '#')
                row1.append(element or '#')
                # if pipe in ('|', 'F', '7', 'L', 'J'):
                if pipe == '|':
                    in_loop = not in_loop
                elif pipe == '-':
                # elif pipe in ('-', 'F', '7', 'L', 'J'):
                    continue
                elif pipe == 'F':
                    open_border_f = True
                elif pipe == 'L':
                    open_border_l = True
                elif pipe == 'J':
                    if open_border_f:
                        in_loop = not in_loop
                        open_border_f=False
                    if open_border_l:
                        open_border_l=False
                elif pipe ==  '7':
                    if open_border_l:
                        in_loop = not in_loop
                        open_border_l = False
                    if open_border_f:
                        open_border_f = False

                else:
                    # print(f"{(min_x+j, min_y+i)=}, {element=}, {in_loop=}")
                    if element and in_loop:
                        inside_.append(element)
                # if pipe == 'S':
                #         breakpoint()
            rows.append(''.join(row))
            # print(f"pipes   : {row}")
            # print(f"original: {row1}")
        print(f"{inside_=}")
        return len(inside_)
