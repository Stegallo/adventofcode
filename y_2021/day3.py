from .common import AoCDay
import copy
from typing import Dict
from .utils import decimal_from_binary


class Element:
    def __init__(self, digit):
        self.__digit = int(digit)
        self.__valid = True

    def digit(self):
        return self.__digit

    def invalidate(self):
        self.__valid = False

    def validate(self):
        self.__valid = True

    def valid(self):
        return self.__valid


class Diagnostic:
    def __init__(self):
        self.__rows = []
        self.__columns = []

    def __repr__(self):
        return "\n".join([str(list(rows)) for rows in self.__rows])

    def reset(self):
        for row in self.__rows:
            for element in row:
                element.validate()

    def add_row(self, number):
        self.__rows.append([])
        for column, digit in enumerate(number):
            element = Element(digit)
            self.__rows[-1].append(element)
            if column >= len(self.__columns):
                self.__columns.append([])
            self.__columns[column].append(element)

    def gamma(self):
        result = []
        for x in self.__columns:
            if sum(int(i.digit()) for i in x) > len(x) // 2:
                result.append(1)
            else:
                result.append(0)
        return result

    def epsilon(self):
        result = []
        for x in self.__columns:
            if sum(int(i.digit()) for i in x) < len(x) // 2:
                result.append(1)
            else:
                result.append(0)
        return result

    def oxygen(self):
        self.reset()
        for c, x in enumerate(self.__columns):
            keep = (
                1
                if sum([int(i.digit()) for i in x if i.valid()])
                >= len([i for i in x if i.valid()]) / 2
                else 0
            )
            for i in self.__rows:
                if i[c].digit() != keep:
                    for j in i:
                        j.invalidate()

            rows = []
            for c, i in enumerate(self.__rows):
                if temp := [x.digit() for x in i if x.valid()]:
                    rows.append(temp)
            if len(rows) == 1:
                break
        return rows[0]

    def c02(self):
        self.reset()
        for c, x in enumerate(self.__columns):
            keep = (
                1
                if sum([int(i.digit()) for i in x if i.valid()])
                < len([i for i in x if i.valid()]) / 2
                else 0
            )
            for i in self.__rows:
                if i[c].digit() != keep:
                    for j in i:
                        j.invalidate()

            rows = []
            for c, i in enumerate(self.__rows):
                if temp := [x.digit() for x in i if x.valid()]:
                    rows.append(temp)
            if len(rows) == 1:
                break
        return rows[0]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__diagnostic = Diagnostic()
        for number in self._input_data:
            self.__diagnostic.add_row(number)

    def _calculate_1(self):
        return decimal_from_binary(self.__diagnostic.gamma()) * decimal_from_binary(
            self.__diagnostic.epsilon()
        )

    def _calculate_2(self):
        return decimal_from_binary(self.__diagnostic.oxygen()) * decimal_from_binary(
            self.__diagnostic.c02()
        )
