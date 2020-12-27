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
        # print(f"{self.messages=}")
        # add terminator
        self.__rules["0"] = self.__rules["0"] + ' "c"'
        # self.invalid_msgs = {}
        self.cache = defaultdict(dict)

    def get_rules(self):
        for i in self.__input:
            if i == "":
                break
            r = i.split(": ")
            self.__rules[(r[0])] = r[1]

    def get_messages(self):
        found = False
        for i in self.__input:
            if i == "":
                found = True
                continue
            if found:
                self.__messages.append(i)

    def match_singe_rule(self, msg, rule):
        return False
        print(f"{msg=}, {rule=}")
        if len(msg) < len(rule):
            print("msg shorter")
            return False
        if len(msg) == len(rule) == 0:
            print("all zero")
            return True
        if len(rule) == 0:
            print("len rule is zero")
            return False
        for c, i in enumerate(msg):
            prefix = msg[: c + 1]
            first_rule = rule[0]
            print(f"{prefix=}, {first_rule=}")
            valid = self.is_valid(prefix, first_rule)
            if valid:
                print(f"{prefix=}, {first_rule=}, {valid=}, {rule=}, {len(rule)=}")
                if self.match_singe_rule(msg[c + 1 :], rule[1:]):
                    return True
        return False

    def _is_valid(self, msg, rule="0"):
        return False
        print(f"{msg=}, {self.invalid_msgs=}")
        if msg in self.invalid_msgs:
            if rule in self.invalid_msgs[msg]:
                return False
        for alternative in (
            self.rules[rule].replace(" ", "").replace('"', "").split("|")
        ):
            print(f"{msg=}; {alternative=}")
            # continue
            if msg in alternative:
                return True
            if alternative in ("a", "b"):
                if msg in self.invalid_msgs:
                    self.invalid_msgs[msg].append(rule)
                else:
                    self.invalid_msgs[msg] = []
                return False
            if self.match_singe_rule(msg, alternative):
                print(f"{msg=} is valid! for {rule=}, {alternative=}")
                return True
        if msg in self.invalid_msgs:
            self.invalid_msgs[msg].append(rule)
        else:
            self.invalid_msgs[msg] = []
        return False

    def is_valid(self, msg, rule_list=["0"]):
        # breakpoint()
        # print(f"\n{rule_list=} ... {msg=}  ... ")
        if len(rule_list) == 1:
            if rule_list[0].isalpha():
                return msg == rule_list[0]
            # breakpoint()
            single_alternative = self.__rules[rule_list[0]].replace('"', "").split(" ")

            # print(f"{single_alternative=}")
            if self.cache.get(msg, {}).get("#".join(single_alternative)) is True:
                # print("is valid")
                valid = True
            elif self.cache.get(msg, {}).get("#".join(single_alternative)) is False:
                # print("is not valid")
                valid = False
            else:
                valid = self.is_valid(msg, single_alternative)
                # self.cache[msg]["#".join(single_alternative)] = valid
                # print(f"is {valid}")
            return valid
        alternative_valid = False
        # print("reaching here!!!")
        # print(f'{"#".join(rule_list)=}')
        # print(f'{rule_list=}; {"#".join(rule_list).split("|")=}')
        for alternative_x in "#".join(rule_list).split("|"):
            alternative = alternative_x
            if alternative_x[0] == "#":
                alternative = alternative_x[1:]
            if alternative_x[-1] == "#":
                alternative = alternative_x[:-1]
            # alternative = alternative_x.replace("#", "")
            # print(f"{alternative=}")
            # print(f"{self.cache=}")
            # print(f"{msg}; {self.cache.get(msg, {}).get(alternative)=}")
            if self.cache.get(msg, {}).get(alternative) is True:
                alternative_valid = True
                break
            if self.cache.get(msg, {}).get(alternative) is False:
                continue
            # print(f"{alternative=}")
            # print(f"{alternative=}, {msg=}")
            original_msg = msg
            if len(alternative.split("#")) > len(msg):
                continue
            # print(f"{alternative=}, {msg}")
            valid = True
            for rule_key in alternative.split("#"):
                # print(f"{rule_key=}, {msg=}")
                # breakpoint()
                inner_valid = False
                for i in range(len(msg)):
                    if self.is_valid(msg[: i + 1], [rule_key]):
                        # print(f"{valid=}")
                        inner_valid = True
                        msg = msg[i + 1 :]
                        break
                        # print(f"{valid=}")
                if not inner_valid:
                    valid = False
                    break
            if valid:
                alternative_valid = True
                # self.cache[original_msg][alternative] = True
                break
            # self.cache[original_msg][alternative] = False

        return alternative_valid

    def _calculate_1(self):
        # print(f"{(self.__rules)=}")
        c = 0
        # x = {}
        # breakpoint()
        for k, i in enumerate(self.__messages):
            # print(i)
            valid = self.is_valid(i + "c")
            # print(f"{i} is {valid} {k=}")
            # print(k)
            c += valid
            # x[i] = (valid, len(i))
        # print(x)
        return c

    def _calculate_2(self):
        ...
        return 0
