from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0][0]

    def _solution(self, length: int) -> int:
        x = self.__input_data
        return next(
            (
                c + length
                for c in range(len(x) - length)
                if len(set(x[c : c + length])) == length
            ),
            0,
        )

    def _calculate_1(self):
        return self._solution(4)

    def _calculate_2(self):
        return self._solution(14)
