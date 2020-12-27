import re
from collections import defaultdict
from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(19)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]
        self.__rules = {}
        self.__messages = []
        self.get_rules()
        self.get_messages()

    def get_rules(self):
        for i in self.__input:
            if i == "":
                break
            r = i.split(": ")
            self.__rules[int(r[0])] = r[1].replace('"', "").split(" | ")

    def get_messages(self):
        found = False
        for i in self.__input:
            if i == "":
                found = True
                continue
            if found:
                self.__messages.append(i)

    def build_regex(self, rule=0):
        r = self.__rules[rule]
        if len(r) == 1 and r[0].isalpha():
            return r[0]
        options = []
        for alternative in r:
            option = ""
            for x in alternative.split(" "):
                if x == " ":
                    continue
                option += self.build_regex(int(x))
            options.append(option)
        return "(" + "|".join(options) + ")"

    def _calculate_1(self):
        rexp = re.compile("^" + self.build_regex() + "$")
        c = 0
        for k, i in enumerate(self.__messages):
            valid = 1 if rexp.match(i) else 0
            c += valid
        return c

    def _calculate_2(self):
        print(self.__rules)
        return 0
