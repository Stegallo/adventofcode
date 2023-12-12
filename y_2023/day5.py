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


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
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
