from collections import defaultdict

from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(15)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def _calculate_1(self, stop=2020):
        last = {}
        before_last = {}
        d = defaultdict(int)
        list = self.__input[0].split(",")
        c = 0
        t = 0
        prev = None
        while t < stop:
            if t < len(list):
                spoken = int(list[c])
            else:
                if d[prev] == 1:
                    spoken = 0
                else:
                    if prev in before_last:
                        spoken = last[prev] - before_last[prev]
            d[spoken] += 1
            c = (c + 1) % len(list)
            t += 1
            prev = spoken
            if spoken in last:
                before_last[spoken] = last[spoken]
            last[spoken] = t

        return spoken

    def _calculate_2(self):
        return self._calculate_1(30000000)
