import re

from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(9)

    def _preprocess_input(self):
        self.__input = [int(i) for i in self._input_data]

    def _calculate_1(self, size=25):
        c = 0
        for i in self.__input[size:]:
            temp = self.__input[c : size + c]
            c += 1
            correct = False
            for j in temp:
                for k in temp:
                    x = j + k
                    if i == x:
                        correct = True
                        break
                if correct == True:
                    break
            if correct == False:
                break

        self.__problem_1_result = i
        return self.__problem_1_result

    def _calculate_2(self, val=None):
        if not val:
            val = self.__problem_1_result
        c = 0
        l = {}
        for i in self.__input:
            l[i] = []
            for j in self.__input[c:]:
                l[i].append(j)
                if sum(l[i]) == val:
                    return i + max(l[i])
            c += 1
        return 0
