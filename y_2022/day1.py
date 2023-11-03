from common.aoc import AoCDay

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]

    def _calculate_1(self):
        return max(sum(i) for i in self.__input_data)

    def _calculate_2(self):
        return sum(sorted([sum(i) for i in self.__input_data])[-3:])
