import re
from collections import defaultdict


def bitand(x, y):
    return x & y


def bitor(x, y):
    return x | y


def lshift(x, y):
    return x << y


def rshift(x, y):
    return x >> y


def bitnot(x):
    return x ^ 65535


BIN_OPERATORS = {"AND": bitand, "OR": bitor, "LSHIFT": lshift, "RSHIFT": rshift}
UN_OPERATORS = {"NOT": bitnot}


class Container:
    content = None


class Link:
    """docstring for Link"""

    @staticmethod
    def create_link(rule):
        if len(rule) == 1:
            try:
                value = int(rule[0])
                return ValueLink(value)
            except ValueError:
                pass
            return DirectLink(WIRING[rule[0]])

        if rule[0] in BIN_OPERATORS:
            try:
                value = int(rule[1])
                op1 = ValueLink(value)
            except ValueError:
                op1 = DirectLink(WIRING[rule[1]])
            try:
                value = int(rule[2])
                op2 = ValueLink(value)
            except ValueError:
                op2 = DirectLink(WIRING[rule[2]])

            return BinaryLink(rule[0], op1, op2)

        if rule[0] in UN_OPERATORS:
            try:
                value = int(rule[1])
                op1 = ValueLink(value)
            except ValueError:
                op1 = DirectLink(WIRING[rule[1]])
            return UnaryLink(rule[0], op1)

        raise Exception("operator not expected")


class DirectLink(Link):
    """"""

    def __init__(self, op1):
        self._cached_result = None
        self._op1 = op1

    def get_value(self):
        if not self._cached_result:
            self._cached_result = self._op1.content.get_value()
        return self._cached_result


class ValueLink(Link):
    """"""

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value


class BinaryLink(Link):
    """"""

    def __init__(self, operator, op1, op2):
        self._cached_result = None
        self._operator = operator
        self._op1 = op1
        self._op2 = op2

    def get_value(self):
        if not self._cached_result:
            self._cached_result = BIN_OPERATORS[self._operator](
                self._op1.get_value(), self._op2.get_value()
            )
        return self._cached_result


class UnaryLink(Link):
    def __init__(self, operator, op1):
        self._cached_result = None
        self._operator = operator
        self._op1 = op1

    def get_value(self):
        if not self._cached_result:
            self._cached_result = UN_OPERATORS[self._operator](self._op1.get_value())
        return self._cached_result


WIRING = defaultdict(Container)


def parse(i):
    x = i[: re.search(" ->", i).start()]
    if "AND" in x:
        first = x[: re.search(" AND", x).start()]
        second = x[re.search(" AND", x).start() + 5 :]

        return [i[re.search(" ->", i).start() + 4 :], "AND", first, second]

    if "OR" in x:
        first = x[: re.search(" OR", x).start()]
        second = x[re.search(" OR", x).start() + 4 :]

        return [i[re.search(" ->", i).start() + 4 :], "OR", first, second]

    if "LSHIFT" in x:
        first = x[: re.search(" LSHIFT", x).start()]
        second = x[re.search(" LSHIFT", x).start() + 8 :]

        return [i[re.search(" ->", i).start() + 4 :], "LSHIFT", first, second]

    if "RSHIFT" in x:
        first = x[: re.search(" RSHIFT", x).start()]
        second = x[re.search(" RSHIFT", x).start() + 8 :]

        return [i[re.search(" ->", i).start() + 4 :], "RSHIFT", first, second]

    if "NOT" in x:
        return [
            i[re.search(" ->", i).start() + 4 :],
            "NOT",
            x[re.search("NOT", x).start() + 4 :],
        ]

    return [i[re.search(" ->", i).start() + 4 :], i[: re.search(" ->", i).start()]]


def inner_1(lista):
    global WIRING
    WIRING = defaultdict(Container)
    parsedl = [parse(i) for i in lista]
    for i in parsedl:
        temp = WIRING[i[0]]
        temp.content = Link.create_link(i[1:])

    return {k: v.content.get_value() for k, v in WIRING.items()}


def calculate_1(x: list) -> int:
    result = inner_1(x)
    return result["a"]


def inner_2(lista):
    global WIRING
    WIRING = defaultdict(Container)
    parsedl = [parse(i) for i in lista]
    for i in parsedl:
        temp = WIRING[i[0]]
        temp.content = Link.create_link(i[1:])
    WIRING["b"].content._value = 46065
    return {k: v.content.get_value() for k, v in WIRING.items()}


def calculate_2(x: str) -> int:
    result = inner_2(x)
    return result["a"]
