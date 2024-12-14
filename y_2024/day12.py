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
        self.grid = Grid.from_input(self._input_data)
        self.grid.display()

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
        # for k, v in perims.items():
        #     print(k, len(v))

        result = 0
        for k, v in region_grid.values.items():
            result += len(v) * len(perims[k])

        return result

    def _calculate_2(self):
        # return 0
        visited = set()
        result = 0

        regions = defaultdict(list)
        reg_n = 0
        for x in self.grid.grid.keys():
            if x in ASSINGED_REGION:
                ...
            else:
                reg_n += 1
                ASSINGED_REGION[x] = reg_n
                visited.add(self.grid.grid.get(x))

            self.navigate(x)

        region_grid = Grid.from_grid(
            {k: str(ASSINGED_REGION[k]) for k, v in self.grid.grid.items()},
            self.grid.height,
            self.grid.length,
        )

        perims = defaultdict(list)

        sides = {}
        for k, v in region_grid.items():
            temp = []
            for i in DIRS:
                cur = Cursor(k, Direction.from_symbol(i))
                if self.grid.grid.get(cur.ahead(), "*") != self.grid.grid.get(k):
                    temp.append(cur)
            perims[v].extend(temp)


        sides = {}
        for k, v in perims.items():
            # print(k, len(v))
            reduced_v = []
            for i in v:
                if i.dir.y==0:
                    reduced_v.append(i)
            # print(k, len(reduced_v), reduced_v)
            # continue
            # vicino_di_qlcn = set()
            # shrink = {}
            vicini_potenziali = defaultdict(list)
            vicini_potenziali_bound = {}
            for i in reduced_v:
                # print(f"{len(shrink)=}")
                print(f"{i=}")
                # if i in vicino_di_qlcn:
                #     print(f"{i} e' gia vicino")
                #     continue
                # shrink[i] = (i.pos.y, i.pos.y)
                for j in reduced_v:
                    if i == j:
                        continue
                    # if j in vicino_di_qlcn:
                    #     continue
                    if i.dir != j.dir:
                        continue
                    if i.pos.x != j.pos.x:
                        continue
                    vicini_potenziali[i].append(j)
                    vicini_potenziali_bound[i] = i.pos.y
                #     # if abs(i.pos.y - j.pos.y) != 1:
                #     #     continue
                    # if shrink[i][0]-1 != j.pos.y and shrink[i][1]+1 != j.pos.y:
                    #     breakpoint()
                #         continue
                #     # for k in vicini[i]:
                #     #     if abs(k.pos.y - j.pos.y) != 1:
                #     #         continue
                #     vicino_di_qlcn.add(j)
                #     # vicini[i].append(j)
                #     print(f"{i=},{j=}")
            # print(f"{len(vicini_potenziali)=}")
            # print(f"{vicini_potenziali_bound=}")
            for kk,vvv in vicini_potenziali.items():
                print(kk, len(vvv), vicini_potenziali_bound[kk])
                vv = sorted(vvv, key=lambda x: x.pos.y)
                for j in vv:
                    print(f">>> {j}")
            #         # print(f"{vicini_potenziali_bound[k]=} {j.pos.y=}")
                    if vicini_potenziali_bound[kk]+1 == j.pos.y:
                        vicini_potenziali_bound[kk] = j.pos.y
            # print(f"{vicini_potenziali_bound=}")
            # print(f"{len(vicini_potenziali_bound)=}")
            # set_vicini_potenziali_bound = set((k.pos.x,v) for k,v in vicini_potenziali_bound.items())
            tmp = set((k.pos.x,v,k.dir.icon) for k,v in vicini_potenziali_bound.items())
            print(f"{vicini_potenziali_bound=}")
            print(f"{tmp=}")
            print(f"{len(reduced_v)=}, {len(vicini_potenziali_bound)=}, {len(tmp)=}")

                # for l,u in vicini_potenziali.items():
                #     if k
            # print(len(shrink))
            # sides[k] = 2*(len(reduced_v)-len(set_vicini_potenziali_bound))
            # break

        print(sides)
        result = 0
        for k, v in region_grid.values.items():
            result += len(v) * sides[k]

        return result
