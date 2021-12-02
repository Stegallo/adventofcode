from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(1)

    def _preprocess_input(self):
        self.__input_data = [int(i) for i in self._input_data]

    def _calculate_1(self):
        x = self.__input_data
        m = 100000
        result = 0
        for v in x:
            if v > m:
                result += 1
            m = v
        return result

    def _calculate_2(self):
        x = self.__input_data
        result = 0
        m = 100000
        for i, v in enumerate(x):
            if i < 2:
                continue
            t = x[i] + x[i - 1] + x[i - 2]
            if t > m:
                result += 1
            m = t
        return result
