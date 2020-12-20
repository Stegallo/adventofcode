import re

from .common import AoCDay

p = 0


class Day(AoCDay):
    def __init__(self):
        super().__init__(19)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def validate(self, rule=0):

        # print()
        # print(f"{self.message=}, {rule=}, {self.p=}, {self.rules[rule].split(' | ')=}")
        # print(self.rules)
        # print(self.rules[rule].split(" "))
        # breakpoint()
        outer_valid = False
        temp_p = self.p
        for j in self.rules[rule].split(" | "):
            valid = True
            self.p = temp_p
            for i in j.split(" "):
                # breakpoint()
                # print(f"{int(i)=}")
                # print(f"{self.rules[int(i)]=}")
                int_i = None
                str_i = None
                try:
                    int_i = int(i)
                except ValueError as e:
                    ...
                if int_i:
                    # print("rule is other rule")
                    if not self.validate(int_i):
                        valid = False
                    # print(f"{p=},{valid=}")
                    # self.p += 1
                else:
                    # print("rule is char")
                    # raise e
                    # breakpoint()
                    str_i = i.replace('"', "")
                    # print(f"{self.p=},{str_i=},{self.message[self.p]=}")
                    if self.message[self.p] != str_i:
                        valid = False
                    # else:
                    #     valid = False
                    self.p += 1
            # print(
            #     f"{self.rules[rule]}, {self.p=}, self.message[self.p]=, {valid=}, {len(self.message)=}"
            # )
            if valid:
                outer_valid = True
        if rule == 0 and len(self.message) > self.p:
            return False
        return outer_valid

    def _calculate_1(self):
        # info(self._input_data)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        self.rules = {}
        end_rules = False
        c = 0
        for i in self.__input:
            if not end_rules:
                # print(f"{i=}")
                if i == "":
                    end_rules = True
                    continue
                r = i.split(": ")
                # print(f"{r=}")
                self.rules[int(r[0])] = r[1]
                # print(f"{rules=}")
            if end_rules:
                # print(f"{i=}")
                self.message = i
                self.p = 0
                c += self.validate()
                # break
        return c

    def _calculate_2(self):
        self.__input
        return 0


def info(x):
    print(f"{len(x)=}")
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
