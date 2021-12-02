from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(1)

    def _preprocess_input(self):
        self.__input_data = [int(i) for i in self._input_data]

    def _calculate_1(self):
        data = self.__input_data
        previous = 100000
        result = 0
        for value in data:
            if value > previous:
                result += 1
            previous = value
        return result

    def _calculate_2(self):
        data = self.__input_data
        result = 0
        previous = 100000
        for index, value in enumerate(data):
            if index < 2:
                continue
            sum = data[index] + data[index - 1] + data[index - 2]
            if sum > previous:
                result += 1
            previous = sum
        return result
