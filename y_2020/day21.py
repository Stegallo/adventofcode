import re
from .common import AoCDay
from collections import defaultdict
from copy import deepcopy


class Day(AoCDay):
    def __init__(self):
        super().__init__(21)

    def _preprocess_input(self):
        result = []
        for i in self._input_data:
            x = re.findall("(.*) \(contains (.*)\)", i)[0]
            result.append([x[0].split(" "), x[1].split(", ")])

        self.__recipes = result
        self.__possible_allers = defaultdict(set)
        self.__recipes_with = defaultdict(list)

        for c, i in enumerate(self.__recipes):
            allergens = set(i[1])
            for aller in allergens:
                self.__recipes_with[aller].append(c)
            for ingr in i[0]:
                self.__possible_allers[ingr] |= allergens

        self.__safe = self.safe_ingredients()

    def safe_ingredients(self):
        safe = []

        for ingr, possible in (self.__possible_allers).items():
            # possible = self.__possible_allers[ingr]
            impossible = set()
            # breakpoint()

            for aller in possible:
                for i in self.__recipes_with[aller]:
                    if ingr not in self.__recipes[i][0]:
                        impossible.add(aller)
                        break

            # Difference between sets: remove all the items of `impossible` from `possible`
            possible -= impossible

            # If no possible allergens are left, the ingredient does not contain allergens
            if not possible:
                safe.append(ingr)

        return safe

    # safe = safe_ingredients(recipes, possible_allers, recipes_with)

    def _calculate_1(self):
        print(f"{self.__possible_allers=}")
        return sum(ingr in r[0] for r in self.__recipes for ingr in self.__safe)

    def simplify(self):
        assigned = {}

        while self.__possible_allers:
            for ingr, possible in self.__possible_allers.items():
                if len(possible) == 1:
                    break

            aller = possible.pop()
            assigned[aller] = ingr
            del self.__possible_allers[ingr]

            for ingr, possible in self.__possible_allers.items():
                if aller in possible:
                    possible.remove(aller)

        return assigned

    def _calculate_2(self):
        print(f"{self.__possible_allers=}")
        print(f"{self.__safe=}")
        for ingr in self.__safe:
            del self.__possible_allers[ingr]

        assigned = self.simplify()
        print(f"{sorted(assigned)=}")
        print(f"{assigned=}")
        lst = ",".join(map(assigned.get, sorted(assigned)))
        return lst
