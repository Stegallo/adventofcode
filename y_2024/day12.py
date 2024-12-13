from typing import Optional

from pydantic.dataclasses import dataclass
from collections import defaultdict
from common.aoc import AoCDay
from common.grid import Grid, Cursor, Direction, DIRS


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original


ASSINGED_REGION = {}


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _area(self):
        return

    def _perim(self):
        return

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

    def next_char(self, c):
        return chr(ord(c) + 1)

    def navigate(self, x):
        # print(f"{ASSINGED_REGION=}")
        # if x in ASSINGED_REGION:
        #     return
        for i in DIRS:
            cur = Cursor(x, Direction.from_symbol(i))
            # print(f"{i=}, {cur}")
            if (
                self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x)
                and cur.ahead() not in ASSINGED_REGION
            ):
                ASSINGED_REGION[cur.ahead()] = ASSINGED_REGION[x]
                self.navigate(cur.ahead())

    def _calculate_1(self):
        return 0
        visited = set()
        result = 0

        regions = defaultdict(list)
        # for x in self.grid.values:
        reg_n = 0
        for x in self.grid.grid.keys():
            if x in ASSINGED_REGION:
                # alreay vicino a qualcuno
                # print(f"{x=}, {self.grid.grid.get(x)}, {ASSINGED_REGION[x]=}")
                ...
                # continue
            else:
                # reg_n = self.next_char(reg_n)
                reg_n += 1
                ASSINGED_REGION[x] = reg_n
                visited.add(self.grid.grid.get(x))
                # print(f"{x=}, {self.grid.grid.get(x)}, {ASSINGED_REGION[x]=}")
            # print(assinged_region.values())
            # if x not in assinged_region.values():
            #     print('assinging region')
            #     reg_n+=1
            #     regions[reg_n].append(x)
            #     continue
            # reg_n+=1
            # print(x, reg_n)
            # print(x, self.grid.values[x], len(self.grid.values[x]))
            self.navigate(x)
            # for i in DIRS:
            #     # print(f"{i}")
            #     cur = Cursor(x, Direction.from_symbol(i))
            #     # print(f"{i}, {cur.ahead()}, {self.grid.grid.get(cur.ahead())}")
            #     # if self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x) and cur.ahead() not in assinged_region:
            #     if self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x):
            #         # print(f'>>>{cur.ahead()} is in same region of {self.grid.grid.get(x)}')
            #         assinged_region[cur.ahead()] = assinged_region[x]

            # print(f"{cur.ahead()=}")

        # print("assinged_region")
        # print(f"{len(ASSINGED_REGION)=}")
        # print(f"{set(ASSINGED_REGION.values())=}")
        # for k,v in assinged_region.items():
        #     print(k, self.grid.grid.get(k), v)
        # regions[self.grid.grid[x]].append(x)
        # print("regions")
        # for k,v in regions.items():
        #     print(k, len(v))
        region_grid = Grid.from_grid(
            {k: str(ASSINGED_REGION[k]) for k, v in self.grid.grid.items()},
            self.grid.height,
            self.grid.length,
        )
        region_grid.display()
        # for k,v  in region_grid.values.items():
        #     print(k,len(v))

        perims = defaultdict(list)
        for k, v in region_grid.items():
            # print(k,v)
            for i in DIRS:
                cur = Cursor(k, Direction.from_symbol(i))
                # print(f"{i=}, {cur}, {cur.ahead()} {self.grid.grid.get(cur.ahead(),'*')}, {self.grid.grid.get(k)=}")
                if self.grid.grid.get(cur.ahead(), "*") != self.grid.grid.get(k):
                    perims[v].append("*")
                # if self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x) and cur.ahead() not in ASSINGED_REGION:
                #     ASSINGED_REGION[cur.ahead()] = ASSINGED_REGION[x]
                #     self.navigate(cur.ahead())
            # perims[k].append(Point(-1,-1))
            # break
        for k, v in perims.items():
            print(k, len(v))

        result = 0
        for k, v in region_grid.values.items():
            result += len(v) * len(perims[k])

        return result

    def _calculate_2(self):
        # return 0
        visited = set()
        result = 0

        regions = defaultdict(list)
        # for x in self.grid.values:
        reg_n = 0
        for x in self.grid.grid.keys():
            if x in ASSINGED_REGION:
                # alreay vicino a qualcuno
                # print(f"{x=}, {self.grid.grid.get(x)}, {ASSINGED_REGION[x]=}")
                ...
                # continue
            else:
                # reg_n = self.next_char(reg_n)
                reg_n += 1
                ASSINGED_REGION[x] = reg_n
                visited.add(self.grid.grid.get(x))
                # print(f"{x=}, {self.grid.grid.get(x)}, {ASSINGED_REGION[x]=}")
            # print(assinged_region.values())
            # if x not in assinged_region.values():
            #     print('assinging region')
            #     reg_n+=1
            #     regions[reg_n].append(x)
            #     continue
            # reg_n+=1
            # print(x, reg_n)
            # print(x, self.grid.values[x], len(self.grid.values[x]))
            self.navigate(x)
            # for i in DIRS:
            #     # print(f"{i}")
            #     cur = Cursor(x, Direction.from_symbol(i))
            #     # print(f"{i}, {cur.ahead()}, {self.grid.grid.get(cur.ahead())}")
            #     # if self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x) and cur.ahead() not in assinged_region:
            #     if self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x):
            #         # print(f'>>>{cur.ahead()} is in same region of {self.grid.grid.get(x)}')
            #         assinged_region[cur.ahead()] = assinged_region[x]

            # print(f"{cur.ahead()=}")

        # print("assinged_region")
        # print(f"{len(ASSINGED_REGION)=}")
        # print(f"{set(ASSINGED_REGION.values())=}")
        # for k,v in assinged_region.items():
        #     print(k, self.grid.grid.get(k), v)
        # regions[self.grid.grid[x]].append(x)
        # print("regions")
        # for k,v in regions.items():
        #     print(k, len(v))
        region_grid = Grid.from_grid(
            {k: str(ASSINGED_REGION[k]) for k, v in self.grid.grid.items()},
            self.grid.height,
            self.grid.length,
        )
        # region_grid.display()
        # for k,v  in region_grid.values.items():
        #     print(k,len(v))

        perims = defaultdict(list)
        sup_perims = defaultdict(list)
        sides = {}
        corners = defaultdict(int)
        for k, v in region_grid.items():
            side = 0

            # if int(v) > 3:
            #     continue
            # print(k,v)
            temp = []
            temp2 = []
            for i in DIRS:
                cur = Cursor(k, Direction.from_symbol(i))
                # print(f"{i=}, {cur}, {cur.ahead()} {self.grid.grid.get(cur.ahead(),'*')}, {self.grid.grid.get(k)=}")
                if self.grid.grid.get(cur.ahead(), "*") != self.grid.grid.get(k):
                    temp.append((cur.ahead(), cur.dir))
                # if self.grid.grid.get(cur.ahead()) == self.grid.grid.get(x) and cur.ahead() not in ASSINGED_REGION:
                #     ASSINGED_REGION[cur.ahead()] = ASSINGED_REGION[x]
                #     self.navigate(cur.ahead())
            # perims[k].append(Point(-1,-1))

            # for j in DIRS_8:
            #     cur = Cursor(k, Direction.from_symbol8(j))
            #     if self.grid.grid.get(cur.ahead(), "*") != self.grid.grid.get(k):
            #         temp2.append(cur.ahead())
            # print(temp)
            # print(temp2)
            # print(set(temp2)-set(temp))
            # print()
            # breakpoint()
            # if len(temp)>1:
            #     corners[v] +=2
            # print(f'{v} this may be a corner {temp}')
            # corners[v] = side
            perims[v].extend(temp)
            # sup_perims[v].extend(set(temp2)-set(temp))
            # if c==3:
            # break
        # breakpoint()
        for k, v in perims.items():
            remaining_borders = v
            l = 0
            while remaining_borders:
                touched_borders = set()
                # print(k, len(v))
                start = remaining_borders[0][0]
                dir = remaining_borders[0][1]
                # print(start, dir.right())
                c = Cursor(start, dir.right())
                # print(c.ahead(), v)

                for i in range(1000):
                    # print(c, start, dir)
                    if c.pos == start and i > 1:
                        break
                    # print(f"{c.ahead()=} - {c.p_right()=} - {c.p_left()=}")
                    if c.ahead() in [i[0] for i in v]:
                        # print(f'{c.ahead()} contiguoys')
                        c.move_forward()
                        touched_borders.add(c.ahead())
                    elif c.p_right() in [i[0] for i in v]:
                        # print('turn right')
                        # print(c.p_right())
                        c.move_right()
                        l += 1
                        touched_borders.add(c.p_right())
                    elif c.p_left() in [i[0] for i in v]:
                        # print('turn left')
                        c.move_left()
                        l += 1
                        touched_borders.add(c.p_left())
                    else:
                        raise Exception()
                breakpoint()
                remaining_borders = [i for i in v if i[0] not in touched_borders]
            print(f"{l=}")

            # for i in v:
            #     print(i)
        # for k, v in perims.items():
        #
        #     # print(len(set(sup_perims[k])-set(perims[k])))
        #     # print(len(perims[k])-len(set(perims[k])))
        #     tot = len(set(sup_perims[k])-set(perims[k]))+len(perims[k])-len(set(perims[k]))
        #     print(k,len(v), tot)
        #         len(set(sup_perims['1'])-set(perims['1']))
        # 7
        # (Pdb) len(perims['1'])
        # 18
        # (Pdb) len(perims['1'])-len(set(perims['1'])
        # *** SyntaxError: '(' was never closed
        # (Pdb) len(perims['1'])-len(set(perims['1']))
        # 3
        # print(k, v, len(corners))
        # for k,v in corners.items():
        #     print(k, v, len(perims[k]))
        # for k, v in perims.items():
        #     # visited = set()
        #     print(v)
        #     sorted_perim = []
        #     pos_in_per = v[0]
        #     dir = Direction.from_symbol('^')
        #     pos_to_right = Point(pos_in_per.x+1, pos_in_per.y)
        #     pos_to_left = Point(pos_in_per.x-1, pos_in_per.y)
        #     pos_to_bottom = Point(pos_in_per.x, pos_in_per.y+1)
        #     pos_to_top = Point(pos_in_per.x, pos_in_per.y-1)
        #     if pos_to_bottom in region_grid.values[k] or pos_to_top in region_grid.values[k]:
        #         dir = Direction.from_symbol('>')
        #     # if pos_to_right in region_grid.values[k] or pos_to_left in region_grid.values[k]:
        #     # breakpoint()
        #     sorted_perim.append(pos_in_per)
        #     # if pos_in_per
        #     c = 0
        #     while True:
        #         c+=1
        #         cur = Cursor(pos_in_per, dir)
        #         p_right = cur.p_right()
        #         p_left = cur.p_left()
        #         print(*(cur,f"{cur.ahead()=}", f"{p_right=}", f"{p_left=}"), sep="\n")
        #         if cur.ahead() in v: # and cur.ahead() not in sorted_perim:
        #             # print(f"{cur.ahead()} not in {sorted_perim}, {cur.ahead() not in sorted_perim}")
        #             print(f"{cur.ahead()} in perims")
        #             sorted_perim.append(cur.ahead())
        #             pos_in_per = cur.ahead()
        #         if p_right in v: # and p_right not in sorted_perim:
        #             # print(f"{p_right} not in {sorted_perim}, {p_right not in sorted_perim}")
        #             print(f"{p_right} in perims")
        #             sorted_perim.append(p_right)
        #             pos_in_per = p_right
        #             dir = dir.right()
        #         if p_left in v: # and p_left not in sorted_perim:
        #             # print(f"{p_left} not in {sorted_perim}, {p_left not in sorted_perim}")
        #             print(f"{p_left} in perims")
        #             sorted_perim.append(p_left)
        #             pos_in_per = p_left
        #             dir = dir.left()
        #         if c==8:
        #             break
        #     # for i in v:
        #     #     cur = Cursor(i, Direction.from_symbol('^'))
        #     #     if cur.ahead() in v:
        #     #         print('no change')
        #     #     else:
        #     #         print('change')
        #     #
        #     #     print(i)
        #     #     print()
        #
        #     print(k, len(v), len(set(v)))
        #     print(sorted_perim)
        #     break

        result = 0
        for k, v in region_grid.values.items():
            result += len(v) * len(perims[k])

        return result
