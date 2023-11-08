from common.aoc import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        string_len = sum(len(x) for x in self.__input_data)
        mem_len = sum(len(eval(x)) for x in self.__input_data)
        return string_len - mem_len

    def _calculate_2(self):
        return sum(2 + x.count("\\") + x.count('"') for x in self.__input_data)
