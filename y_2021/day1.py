from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = [int(i) for i in self._input_data]

    def _calculate_1(self):
        data = self.__input_data

        return sum(data[index] < value for index, value in enumerate(data[1:]))

    def _calculate_2(self):
        data = self.__input_data
        return sum(data[index] < value for index, value in enumerate(data[3:]))
