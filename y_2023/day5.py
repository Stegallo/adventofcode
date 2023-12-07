from common.aoc import AoCDay
from pprint import pprint
from collections import deque
from pydantic.dataclasses import dataclass

def mapp(input, mapping):
    # print(mapping)
    output = input
    for m in mapping:
        if int(input) >= m[0] and int(input) <= m[1]:
            output = int(input) - m[0] + m[2]
    return output #
    # return mapping.get(int(input), int(input))

# def collapse_rages(rang):
#     breakpoint()
#     fixed
#     while not fixed:
#

def mapp_range(input, mapping):
    # print(f"at start: {input}, {mapping}")
    # sorted_i = sorted(input, key=lambda x: x.start)
    # print(f"sorted_i: {sorted_i}")
    # for i in range(len(sorted_i)-1):
    #     if sorted_i[i].end>=sorted_i[i+1].start:
    #         input=collapse_rages(sorted_i)
    #         break

    # new_input = [i for i in input]
    # breakpoint()
    for i in mapping:
        new_input = []
        for j in input:
            # print(f"{i[0]=},{i[1]=}")
            new_input.extend(j.split(i[0],i[1]))
        input = [i for i in new_input]
        # print(f"  in progress: {input}, {mapping}")
    # print(f"at end  : {input}, {mapping}")

    print_inp = list(input)
    output = []
    for inp in input:
        processed = False
        for m in mapping:
            # print(f"{m=}")
            # if m[0]==77:
            #     breakpoint()

            if inp.start >= m[0] and inp.end <= m[1]:
                output.append(SeedRange(inp.start- m[0] + m[2], inp.end- m[0] + m[2]))
                processed=True
            # else:
            #     output.append(inp)
            # breakpoint()
        if not processed:
            output.append(inp)
        # input = list(output)
    # print(f"{print_inp=}, {output=}")
    return output

@dataclass
class SeedRange:
    start:int
    end:int
    size:int = 0

    def __post_init__(self) -> None:
        self.size = self.end-self.start+1

    # @property
    # def size(self):
    #     return self.end-self.start

    def split(self, s, e):
        result = []
        # breakpoint()
        if self.end < s:
            return [self]
        if self.start > e:
            return [self]
        if self.start < s and self.end > e:
            result.append(SeedRange(self.start, s-1))
            result.append(SeedRange(s, e))
            result.append(SeedRange(e+1, self.end))
        if not self.start < s and self.end > e:
            result.append(SeedRange(self.start, e))
            result.append(SeedRange(e+1, self.end))
        if self.start < s and not self.end > e:
            result.append(SeedRange(self.start, s-1))
            result.append(SeedRange(s, self.end))
        if not result:
            return [self]
        return result

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = self._input_data

    def _calculate_1(self):
        return 0
        seeds = self.__input_data[0][0].split(': ')[1].split(' ')
        map = []
        for c, x in enumerate(self.__input_data[1:]):
            map.append([])
            # map.append({})
            for y in x[1:]:
                d, s, r = [int(i) for i in y.split(' ')]
                map[c].append((s, s+r-1, d))
                # for i in range(r):
                #     map[c][s+i] = d+i
                # print(map)
        print(seeds)
        # pprint(map)
        for x in map:
            # seeds = [x.get(int(s), s) for s in seeds]
            seeds = [mapp(s, x) for s in seeds]
            print(seeds)
        return min(seeds)

    def _calculate_2(self):
        seeds = self.__input_data[0][0].split(': ')[1].split(' ')
        map = []
        for c, x in enumerate(self.__input_data[1:]):
            map.append([])
            # map.append({})
            for y in x[1:]:
                d, s, r = [int(i) for i in y.split(' ')]
                map[c].append((s, s+r-1, d))
                # for i in range(r):
                #     map[c][s+i] = d+i
                # print(map)
        print(seeds)


        seeds_new = []
        for c, k in enumerate(seeds):
            # print(c, k, seeds)
            if c % 2 != 0:
                # print(c, k, seeds)
                # for i in range(int(k)):
                #     seeds_new.append(int(seeds[c-1])+i)
                # print(int(seeds[c-1]), int(seeds[c-1])+int(k))
                seeds_new.append(SeedRange(int(seeds[c-1]), int(seeds[c-1])+int(k)-1))
            # for i in range(int(d)):
            #     seeds_new.append(int(c)+i)
        # print(f"{seeds_new}")
        # breakpoint()
        # return 0
        # pprint(map)
        result = 1_000_000_000
        for x in map:
        #     # seeds = [x.get(int(s), s) for s in seeds]
            # seeds_new = [mapp_range(s, x) for s in seeds_new]
            seeds_new = mapp_range(seeds_new, x)
            # print(seeds_new, sum(i.size for i in seeds_new))
            # return
        for i  in seeds_new:
            if i.start < result:
                result=i.start
                # print(i.start)
        return result # min(seeds_new)
