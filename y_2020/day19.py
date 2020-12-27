import re

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
        options = ["".join(self.build_regex(int(j)) for j in i.split(" ")) for i in r]
        return "(" + "|".join(options) + ")"

    def _calculate_1(self):
        rexp = re.compile("^" + self.build_regex() + "$")
        return sum(1 if rexp.match(i) else 0 for i in self.__messages)

    def _calculate_2(self):
        R = 6
        self.__rules[8] = [" ".join(["42"] * k) for k in range(1, R)]
        self.__rules[11] = [" ".join(["42"] * k + ["31"] * k) for k in range(1, R)]
        rexp = re.compile("^" + self.build_regex() + "$")
        return sum(1 if rexp.match(i) else 0 for i in self.__messages)
