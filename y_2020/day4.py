import re

ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
FIELDS = {
    "byr": "([\d][\d][\d][\d])$",
    "iyr": "([\d][\d][\d][\d])$",
    "eyr": "([\d][\d][\d][\d])$",
    "hgt": "([\d]+)([\D]*)$",
    "hcl": "(#[\d|a-f]{6})$",
    "ecl": "(.*)",
    "pid": "(^[\d|\w]{9}$)",
    # "cid"
}


def collapse_strings(x):
    pl = [[]]
    for i in x:
        p = p = pl[-1]
        if len(i) != 0:
            p.append(i)
        else:
            pl.append([])
    return [" ".join(i) for i in pl]


def dict_from_string(x):
    el_list = x.split(":")
    return {el_list[0]: el_list[1]}


def get_passports(x):
    passport_strings = collapse_strings(x)
    passport_list = []
    for passport_string in passport_strings:
        passport_dict = {}
        elements = passport_string.split(" ")
        for element in elements:
            passport_dict = {**passport_dict, **dict_from_string(element)}
        passport_list.append(passport_dict)
    return passport_list


def validate_element(element, value):
    if not (parse := re.findall(FIELDS[element], value)):
        return False
    content = parse[0]
    if element == "byr":
        return int(content) >= 1920 and int(content) <= 2002
    if element == "iyr":
        return int(content) >= 2010 and int(content) <= 2020
    if element == "eyr":
        return int(content) >= 2020 and int(content) <= 2030
    if element == "hgt":
        if content[1] == "cm":
            return int(content[0]) >= 150 and int(content[0]) <= 193
        if content[1] == "in":
            return int(content[0]) >= 59 and int(content[0]) <= 76
    if element == "hcl":
        if content:
            return True
    if element == "ecl":
        return content in ECL
    if element == "pid":
        if content:
            return True

    return False


def validate(passport, skip_elements_validation=False):
    return all(
        f in passport and (skip_elements_validation or validate_element(f, passport[f]))
        for f in FIELDS
    )


def calculate_1(x):
    passports = get_passports(x)
    return sum(
        validate(passport, skip_elements_validation=True) for passport in passports
    )


def calculate_2(x):
    passports = get_passports(x)
    return sum(validate(passport) for passport in passports)
