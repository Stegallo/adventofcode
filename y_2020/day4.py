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


def get_passports(x):
    pl = collapse_strings(x)
    l = []
    for passport in pl:
        x = {}
        elements = passport.split(" ")
        for element in elements:
            el_list = element.split(":")
            n = {el_list[0]: el_list[1]}
            x = {**x, **n}
        l.append(x)
    return l


def validate_1(passport):
    result = True
    for f in FIELDS:
        if f not in passport:
            result = False

    return result


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


def validate_2(passport):
    result = True
    for f in FIELDS:
        if f not in passport or not validate_element(f, passport[f]):
            result = False

    return result


def calculate_1(x):
    passports = get_passports(x)
    c = 0
    for passport in passports:
        c += validate_1(passport)

    return c


def calculate_2(x):
    passports = get_passports(x)
    c = 0
    for passport in passports:
        c += validate_2(passport)

    return c
