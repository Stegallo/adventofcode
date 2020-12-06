from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(1)

    def _preprocess_input(self, input_data):
        return [int(i) for i in input_data]

    def _calculate_1(self):
        y = self._input_data

        for i in y:
            for j in y:
                if (i + j) == 2020:
                    return i * j

        return 0

    def _calculate_2(self):
        y = self._input_data

        for i in y:
            for j in y:
                for k in y:
                    if (i + j + k) == 2020:
                        return i * j * k

        return 0
