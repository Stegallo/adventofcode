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
    day._input_data = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
    ]
    day._preprocess_input()
    assert day._Day__passport_list == [
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
    day._Day__passport_list = [
        {
            "byr": "1937",
            "cid": "147",
            "ecl": "gry",
            "eyr": "2020",
            "hcl": "#fffffd",
            "hgt": "183cm",
            "iyr": "2017",
            "pid": "860033327",
        },
        {
            "byr": "1929",
            "cid": "350",
            "ecl": "amb",
            "eyr": "2023",
            "hcl": "#cfa07d",
            "iyr": "2013",
            "pid": "028048884",
        },
        {
            "byr": "1931",
            "ecl": "brn",
            "eyr": "2024",
            "hcl": "#ae17e1",
            "hgt": "179cm",
            "iyr": "2013",
            "pid": "760753108",
        },
        {
            "ecl": "brn",
            "eyr": "2025",
            "hcl": "#cfa07d",
            "hgt": "59in",
            "iyr": "2011",
            "pid": "166559648",
        },
    ]
    assert day._calculate_1() == 2


def test_calculate_2():
    day._Day__passport_list = [
        {
            "byr": "1926",
            "cid": "100",
            "ecl": "amb",
            "eyr": "1972",
            "hcl": "#18171d",
            "hgt": "170",
            "iyr": "2018",
            "pid": "186cm",
        },
        {
            "byr": "1946",
            "ecl": "grn",
            "eyr": "1967",
            "hcl": "#602927",
            "hgt": "170cm",
            "iyr": "2019",
            "pid": "012533040",
        },
        {
            "byr": "1992",
            "cid": "277",
            "ecl": "brn",
            "eyr": "2020",
            "hcl": "dab227",
            "hgt": "182cm",
            "iyr": "2012",
            "pid": "021572410",
        },
        {
            "byr": "2007",
            "ecl": "zzz",
            "eyr": "2038",
            "hcl": "74454a",
            "hgt": "59cm",
            "iyr": "2023",
            "pid": "3556412378",
        },
    ]
    assert day._calculate_2() == 0

    day._Day__passport_list = [
        {
            "byr": "1980",
            "ecl": "grn",
            "eyr": "2030",
            "hcl": "#623a2f",
            "hgt": "74in",
            "iyr": "2012",
            "pid": "087499704",
        },
        {
            "byr": "1989",
            "cid": "129",
            "ecl": "blu",
            "eyr": "2029",
            "hcl": "#a97842",
            "hgt": "165cm",
            "iyr": "2014",
            "pid": "896056539",
        },
        {
            "byr": "2001",
            "cid": "88",
            "ecl": "hzl",
            "eyr": "2022",
            "hcl": "#888785",
            "hgt": "164cm",
            "iyr": "2015",
            "pid": "545766238",
        },
        {
            "byr": "1944",
            "ecl": "blu",
            "eyr": "2021",
            "hcl": "#b6652a",
            "hgt": "158cm",
            "iyr": "2010",
            "pid": "093154719",
        },
    ]
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
