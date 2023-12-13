<<<<<<< HEAD
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
=======
from typing import Optional, List

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay

from math import inf


@dataclass
class Rule:
    destination: int
    source: int
    length: int


@dataclass
class Category:
    name: str
    order: int
    rules: Optional[List[Rule]] = None

    def set_rules(self, rules: List[Rule]) -> None:
        self.rules = rules


@dataclass
class SeedRange:
    start: int
    end: int
    size: int = 0

    def __post_init__(self) -> None:
        self.size = self.end - self.start + 1

    def split(self, s: int, e: int) -> List:
        if self.end < s or self.start > e:
            return [self]
        if self.start < s and self.end > e:
            return [
                SeedRange(self.start, s - 1),
                SeedRange(s, e),
                SeedRange(e + 1, self.end),
            ]
        if self.start >= s and self.end > e:
            return [SeedRange(self.start, e), SeedRange(e + 1, self.end)]
        if self.start < s and self.end <= e:
            return [SeedRange(self.start, s - 1), SeedRange(s, self.end)]
        return [self]


def apply_rules(seed: int, category: Category) -> int:
    output = seed
    for rule in category.rules:  # type: ignore
        if seed >= rule.source and seed <= rule.source + rule.length - 1:
            output = seed - rule.source + rule.destination
    return output


def apply_rules_to_range(input: List[SeedRange], category: Category) -> List[SeedRange]:
    for rule in category.rules:  # type: ignore
        split_input = []
        for seed_range in input:
            split_input.extend(
                seed_range.split(rule.source, rule.source + rule.length - 1),
            )
        input = list(split_input)

    output = []
    for seed_range in input:
        processed = False
        for rule in category.rules:  # type: ignore
            if (
                seed_range.start >= rule.source
                and seed_range.end <= rule.source + rule.length - 1
            ):
                output.append(
                    SeedRange(
                        seed_range.start - rule.source + rule.destination,
                        seed_range.end - rule.source + rule.destination,
                    ),
                )
                processed = True

        if not processed:
            output.append(seed_range)

    return output

>>>>>>> master

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
<<<<<<< HEAD
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
=======
        self.seeds = [int(i) for i in self._input_data[0][0].split(": ")[1].split(" ")]

        self.categories = []
        for c, rules in enumerate(self._input_data[1:]):
            cat = Category(rules[0], c)
            cat.set_rules([Rule(*rule.split(" ")) for rule in rules[1:]])
            self.categories.append(cat)

        # transforms list of seeds into ranges of seeds
        self.seeds_as_range = [
            SeedRange(
                int(self.seeds[c - 1]),
                int(self.seeds[c - 1]) + int(k) - 1,
            )
            for c, k in enumerate(self.seeds)
            if c % 2 != 0
        ]

    def _calculate_1(self):
        seeds = self.seeds
        for i in self.categories:
            seeds = [apply_rules(s, i) for s in seeds]
        return min(seeds)

    def _calculate_2(self):
        seeds_as_range = self.seeds_as_range
        for x in self.categories:
            seeds_as_range = apply_rules_to_range(seeds_as_range, x)

        result = inf
        for i in seeds_as_range:
            if i.start < result:
                result = i.start

        return result
>>>>>>> master
