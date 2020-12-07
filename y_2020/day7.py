import re

from .common import AoCDay
from typing import NamedTuple


class BagRule(NamedTuple):
    rules: list
    cache: dict


class Day(AoCDay):
    def __init__(self):
        super().__init__(7)

    def _preprocess_input(self):
        x = {}
        # for i in [i.split(" ") for i in self._input_data[:1]]:
        for i in [i.split(" ") for i in self._input_data[:]]:
            print(i)
            bag_color = i[0] + "#" + i[1]
            x[bag_color] = BagRule([], {})
            c = 4
            while True:
                if i[c] == "bag." or i[c] == "bags.":
                    x[bag_color].rules.append(i[c - 2] + "#" + i[c - 1])
                    break
                if i[c] in ["bag,", "bags,"]:
                    # print("in bag comma")
                    x[bag_color].rules.append(i[c - 2] + "#" + i[c - 1])

                c += 1
        # for j in i:
        #     print(j)
        # print(i[4:])
        # print(i[7:])
        # self.__input = [i for i in self._input_data]
        self.__rules = x
        # print(f"{len(self.__rules)=}")
        # for r in self.__rules:
        #     print(f"{r=}")
        #     print(f"{self.__rules[r]=}")
        self.__rules["no#other"] = BagRule([], {})

    def _calculate_1(self):
        # return 0
        c = 0
        for k, bagrules in self.__rules.items():
            # print(k)
            # print(f"{bagrules=}")

            self.enhance(bagrules)

            # if self.can_contain(k, "shiny#gold"):
            # if self.can_contain(k, "posh#fucsia"):
            # c += 1
            # break
        for k, bagrule in self.__rules.items():
            print(f"{k}: {bagrule.cache=}")
            if "shiny#gold" in bagrule.cache:
                c += 1
        # print(self.__rules)
        # info(self._input_data)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        # self.__input
        return c

    def _calculate_2(self):
        # self.__input
        return 0

    def can_contain(self, rule, key):
        # print("can contain")
        # print(rule)
        # print(self.rules)

        if rule == "no#other":
            return True
        # print(self.rules[rule])
        for r in self.rules[rule]:
            # print(r)
            if self.can_contain(r, key):
                return True
        return False
        # if self.can_contain(rule, key):
        # return True
        # for i in self.rules:
        #     # print(i)
        #     if i:
        #         # print(i[0][0])
        #         if i[0][0] == key:
        #             print(f"{i=}")
        return False

    def enhance(self, bagrules):
        # print(f"{bagrules=}")

        for rule in bagrules.rules:
            # print(f"{rule=}")
            if rule == "no#other":
                # print("rule no#other")
                bagrules.cache["no#other"] = "no#other"
                return bagrules.cache

            #
            # if bagrules.cache == {}:
            #     print("empty cache")
            bagrules.cache[rule] = rule
            # print(rule)
            x = self.enhance(self.__rules[rule])
            # print(f"{x=}")
            if x:
                for k, v in x.items():
                    bagrules.cache[k] = v
        return bagrules.cache
        ...


def info(x):
    print(f"{type(x)=}, {len(x)=}")
    hf = len(x) // 2 + 1
    try:
        print(f"{x[+0]=}")
        print(f"{x[hf]=}")
        print(f"{x[-1]=}")
    except:
        ...

    # regex = "([\d]+)-([\d]+) ([\D]): ([\D]*)$"
    # fa = re.findall(regex, x[0])[0]
    # # print(*fa, sep="\n")
