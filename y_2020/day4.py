import re
from typing import NamedTuple

ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


class ValidationRule(NamedTuple):
    regex: str
    validation_func: str


def hgt_validation_func(content):
    if content[1] == "cm":
        return int(content[0]) >= 150 and int(content[0]) <= 193
    if content[1] == "in":
        return int(content[0]) >= 59 and int(content[0]) <= 76
    return False


FIELDS = {
    "byr": ValidationRule(
        "([\d][\d][\d][\d])$", lambda x: int(x) >= 1920 and int(x) <= 2002
    ),
    "iyr": ValidationRule(
        "([\d][\d][\d][\d])$", lambda x: int(x) >= 2010 and int(x) <= 2020
    ),
    "eyr": ValidationRule(
        "([\d][\d][\d][\d])$", lambda x: int(x) >= 2020 and int(x) <= 2030
    ),
    "hgt": ValidationRule("([\d]+)([\D]*)$", hgt_validation_func),
    "hcl": ValidationRule("(#[\d|a-f]{6})$", lambda x: True if x else False),
    "ecl": ValidationRule("(.*)", lambda x: x in ECL),
    "pid": ValidationRule("(^[\d|\w]{9}$)", lambda x: True if x else False)
    # "cid"
}


def collapse_strings(x: list):
    p_list = [[]]
    for i in x:
        p = p_list[-1]
        if len(i) != 0:
            p.append(i)
        else:
            p_list.append([])
    return [" ".join(i) for i in p_list]


def dict_from_string(x: str) -> dict:
    el_list = x.split(":")
    return {el_list[0]: el_list[1]}


def get_passports(x: list) -> list:
    p_strings = collapse_strings(x)
    p_list = []
    for p_string in p_strings:
        p_dict = {}
        elements = p_string.split(" ")
        for element in elements:
            p_dict = {**p_dict, **dict_from_string(element)}
        p_list.append(p_dict)
    return p_list


def validate_element(element: str, value: str) -> bool:
    if not (parse := re.findall(FIELDS[element].regex, value)):
        return False
    return FIELDS[element].validation_func(parse[0])


def validate(passport: dict, skip_elements_validation: bool = False) -> bool:
    return all(
        f in passport and (skip_elements_validation or validate_element(f, passport[f]))
        for f in FIELDS
    )


def calculate_1(x: list) -> None:
    passports = get_passports(x)
    return sum(
        validate(passport, skip_elements_validation=True) for passport in passports
    )


def calculate_2(x: list) -> None:
    passports = get_passports(x)
    return sum(validate(passport) for passport in passports)
