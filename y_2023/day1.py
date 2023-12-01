from common.aoc import AoCDay

SPELLED = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        # return 0
        # print(f"{self.__input_data=}")
        s = 0
        for i in self.__input_data:
            first = None
            for j in i:
                if j.isnumeric():
                    first = int(j)
                    break
            for j in i[::-1]:
                if j.isnumeric():
                    last = int(j)
                    break
            s = s + first * 10 + last
        return s
        # return max(sum(i) for i in self.__input_data)

    def _calculate_2(self):
        s = 0
        for i in self.__input_data:
            for c, k in enumerate(SPELLED):
                i = i.replace(k, k + str(c + 1) + k)
            # print(f'{i=}')
            first = None
            for j in i:
                if j.isnumeric():
                    first = int(j)
                    break
            for j in i[::-1]:
                if j.isnumeric():
                    last = int(j)
                    break
            s = s + first * 10 + last
        return s
