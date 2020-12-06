from unittest.mock import mock_open, patch

from y_2020.day4 import Day, collapse_strings

with patch("builtins.open", mock_open(read_data=":")):
    day = Day()


def test_collapse_strings():
    assert collapse_strings(["x", "", "y1", "y2"]) == ["x", "y1 y2"]
    assert collapse_strings(["x", "y", "", "z"]) == ["x y", "z"]
    assert collapse_strings(
        [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
        ]
    ) == [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd "
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
    ]


def test_preprocess_input():
    assert day._preprocess_input(
        [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
        ]
    ) == [
        {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm",
        },
        {
            "iyr": "2013",
            "ecl": "amb",
            "cid": "350",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929",
        },
    ]


def test_calculate_1():
    day._input_data = day._preprocess_input(
        [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in",
        ]
    )
    assert day._calculate_1() == 2


def test_calculate_2():
    day._input_data = day._preprocess_input(
        [
            "eyr:1972 cid:100",
            "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
            "",
            "iyr:2019",
            "hcl:#602927 eyr:1967 hgt:170cm",
            "ecl:grn pid:012533040 byr:1946",
            "",
            "hcl:dab227 iyr:2012",
            "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
            "",
            "hgt:59cm ecl:zzz",
            "eyr:2038 hcl:74454a iyr:2023",
            "pid:3556412378 byr:2007",
        ]
    )
    assert day._calculate_2() == 0

    day._input_data = day._preprocess_input(
        [
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
            "hcl:#623a2f",
            "",
            "eyr:2029 ecl:blu cid:129 byr:1989",
            "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            "",
            "hcl:#888785",
            "hgt:164cm byr:2001 iyr:2015 cid:88",
            "pid:545766238 ecl:hzl",
            "eyr:2022",
            "",
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu " "byr:1944 eyr:2021 pid:093154719",
        ]
    )
    assert day._calculate_2() == 4


def test_validate_element():
    assert day._Day__validate_element("byr", "2002") is True
    assert day._Day__validate_element("byr", "2003") is False

    assert day._Day__validate_element("hgt", "60in") is True
    assert day._Day__validate_element("hgt", "190cm") is True

    assert day._Day__validate_element("hgt", "190in") is False
    assert day._Day__validate_element("hgt", "190") is False

    assert day._Day__validate_element("hcl", "#123abc") is True
    assert day._Day__validate_element("hcl", "#123abz") is False
    assert day._Day__validate_element("hcl", "123abc") is False
    assert day._Day__validate_element("hcl", "dab227") is False

    assert day._Day__validate_element("ecl", "brn") is True
    assert day._Day__validate_element("ecl", "wat") is False

    assert day._Day__validate_element("pid", "000000001") is True
    assert day._Day__validate_element("pid", "0123456789") is False
