from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        tot = 0
        for i in self.__input_data:
            y = i.split(",")
            a = y[0].split("-")
            b = y[1].split("-")
            s = set()
            for j in range(int(a[0]), int(a[1]) + 1):
                s.add(j)
            t = set()
            for j in range(int(b[0]), int(b[1]) + 1):
                t.add(j)
            if (s & t) == s or (s & t) == t:
                tot += 1

        return tot

    def _calculate_2(self):
        x = self.__input_data
        tot = 0
        for i in x:
            y = i.split(",")
            a = y[0].split("-")
            b = y[1].split("-")
            s = set()
            for j in range(int(a[0]), int(a[1]) + 1):
                s.add(j)
            t = set()
            for j in range(int(b[0]), int(b[1]) + 1):
                t.add(j)
            if (s & t) != set():
                tot += 1

        return tot
