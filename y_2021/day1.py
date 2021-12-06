from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test: int = 0) -> None:
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self) -> None:
        self.__input_data = [int(i) for i in self._input_data]

    def _calculate_1(self) -> int:
        data = self.__input_data
        return sum(data[index] < value for index, value in enumerate(data[1:]))

    def _calculate_2(self) -> int:
        data = self.__input_data
        return sum(data[index] < value for index, value in enumerate(data[3:]))
