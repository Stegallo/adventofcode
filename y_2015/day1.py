from common.aoc import AoCDay

OPERATIONS = {"(": 1, ")": -1}


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0][0]

    def _calculate_1(self):
        return sum(OPERATIONS[x] for x in self.__input_data)

    def _calculate_2(self):
        result = 0
        for j, x in enumerate(self.__input_data, start=1):
            result += OPERATIONS[x]
            if result == -1:
                return j
        return -1
