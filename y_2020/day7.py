from .common import AoCDay
from typing import NamedTuple


class BagRule(NamedTuple):
    rules: list
    cache: dict
    extension: dict


class Day(AoCDay):
    def __init__(self):
        super().__init__(7)

    def _preprocess_input(self):
        x = {}
        for i in [i.split(" ") for i in self._input_data[:]]:
            bag_color = i[0] + "#" + i[1]
            x[bag_color] = BagRule([], {}, {})
            c = 4
            while True:
                try:
                    needed_count = 0 if i[c - 2] + "#" + i[c - 1] == "no#other" else int(i[c - 3])
                except Exception:
                    ...
                if i[c] in ["bag.", "bags."]:
                    x[bag_color].rules.append({i[c - 2] + "#" + i[c - 1]: needed_count})
                    break
                if i[c] in ["bag,", "bags,"]:
                    x[bag_color].rules.append({i[c - 2] + "#" + i[c - 1]: needed_count})

                c += 1
        self.__rules = x
        self.__rules["no#other"] = BagRule([], {}, {})

    def _calculate_1(self):
        for k, bagrules in self.__rules.items():
            self.enhance1(bagrules)
        return sum(
            1
            for k, bagrule in self.__rules.items()
            if "shiny#gold" in bagrule.extension
        )

    def _calculate_2(self):
        c = 0
        for k, bagrules in self.__rules.items():

            self.enhance2(bagrules)

        for k, bagrule in self.__rules.items():
            if k == "shiny#gold":
                for i in bagrule.cache:
                    c += bagrule.cache[i]

        return c

    def enhance1(self, bagrules):
        for rule in bagrules.rules:
            if rule == "no#other":
                bagrules.cache["no#other"] = 0
                return bagrules.extension

            for k, v in rule.items():
                bagrules.cache[k] = v
                bagrules.extension[k] = v
            for i in rule:
                x = self.enhance1(self.__rules[i])
                if x:
                    c = 0
                    for k, v in x.items():
                        bagrules.extension[k] = v
                        c += v
                    if c > 0:
                        bagrules.cache[f"{i}-dependent"] = bagrules.cache[i] * c
        return bagrules.extension

    def enhance2(self, bagrules):
        for rule in bagrules.rules:
            if rule == "no#other":
                bagrules.cache["no#other"] = 0
                return bagrules.cache

            for k, v in rule.items():
                bagrules.cache[k] = v
                bagrules.extension[k] = v
            for i in rule:
                x = self.enhance2(self.__rules[i])
                if x:
                    c = 0
                    for k, v in x.items():
                        bagrules.extension[k] = v
                        c += v
                    if c > 0:
                        bagrules.cache[f"{i}-dependent"] = bagrules.cache[i] * c
        return bagrules.cache
