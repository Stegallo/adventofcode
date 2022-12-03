from collections import defaultdict

from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        x = self.__input_data
        t = 0
        for i in x:
            # print(len(i))
            a = set(i[: len(i) // 2])
            b = set(i[len(i) // 2 :])
            # print(a,b)
            # print(list(a.intersection(b))[0])
            k = ord(list(a.intersection(b))[0])
            # print(k)
            n = 0
            if k <= 122 and k >= 97:
                n = k - 96
            if k <= 90 and k >= 65:
                n = k - 64 + 26
            # print(n)
            t += n
        # print(x)
        return t

    def _calculate_2(self):
        x = self.__input_data
        d = defaultdict(list)
        t = 0
        for c, i in enumerate(x):
            # print(c//3,i)
            d[c // 3].append(i)
        # print(d[0])
        for i in d.values():
            # print(i)
            k = ord(list(set(i[0]).intersection(set(i[1])).intersection(set(i[2])))[0])
            n = 0
            if k <= 122 and k >= 97:
                n = k - 96
            if k <= 90 and k >= 65:
                n = k - 64 + 26
            # print(n)
            t += n
        # print(k)

        # print(d[1])
        return t
