import re

from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(2)

    def _preprocess_input(self):
        self.__password_list = [self.__extract(i) for i in self._input_data]

    def _calculate_1(self):
        return sum(self.__valid_1(i) for i in self.__password_list)

    def _calculate_2(self):
        return sum(self.__valid_2(i) for i in self.__password_list)

    @staticmethod
    def __extract(x):
        regex = "([\d]+)-([\d]+) ([\D]): ([\D]*)$"
        elements = re.findall(regex, x)[0]
        return int(elements[0]), int(elements[1]), elements[2], elements[3]

    @staticmethod
    def __valid_1(i):
        min, max, char, pwd = i

        c = pwd.count(char)
        return c >= min and c <= max

    @staticmethod
    def __valid_2(i):
        min, max, char, pwd = i

        return (pwd[min - 1] == char) != (pwd[max - 1] == char)
