import re
from typing import NamedTuple

from .common import AoCDay
from .utils import collapse_strings, dict_from_string

ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


class ValidationRule(NamedTuple):
    regex: str
    validation_func: str


def hgt_validation_func(content):
    return (content[1] == "cm" and 150 <= int(content[0]) <= 193) or (
        content[1] == "in" and 59 <= int(content[0]) <= 76
    )


FIELDS = {
    "byr": ValidationRule("([\d]{4})$", lambda x: 1920 <= int(x) <= 2002),
    "iyr": ValidationRule("([\d]{4})$", lambda x: 2010 <= int(x) <= 2020),
    "eyr": ValidationRule("([\d]{4})$", lambda x: 2020 <= int(x) <= 2030),
    "hgt": ValidationRule("([\d]+)([\D]*)$", hgt_validation_func),
    "hcl": ValidationRule("(#[\d|a-f]{6})$", lambda x: True if x else False),
    "ecl": ValidationRule("(.*)", lambda x: x in ECL),
    "pid": ValidationRule("(^[\d|\w]{9}$)", lambda x: True if x else False)
    # "cid"
}


class Day(AoCDay):
    def __init__(self):
        super().__init__(4)

    def _preprocess_input(self):
        p_list = []
        for p_string in collapse_strings(self._input_data):
            p_dict = {}
            for element in p_string.split(" "):
                p_dict = {**p_dict, **dict_from_string(element)}
            p_list.append(p_dict)
        self.__passport_list = p_list

    def _calculate_1(self):
        passports = self.__passport_list
        return sum(
            self.__validate(passport, skip_elements_validation=True)
            for passport in passports
        )

    def _calculate_2(self):
        passports = self.__passport_list
        return sum(self.__validate(passport) for passport in passports)

    @staticmethod
    def __validate_element(element: str, value: str) -> bool:
        if not (parse := re.findall(FIELDS[element].regex, value)):
            return False
        return FIELDS[element].validation_func(parse[0])

    @staticmethod
    def __validate(passport: dict, skip_elements_validation: bool = False) -> bool:
        return all(
            f in passport
            and (skip_elements_validation or Day.__validate_element(f, passport[f]))
            for f in FIELDS
        )
