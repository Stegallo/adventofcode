from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        x = self.__input_data
        print(x)
        return 0

    def _calculate_2(self):
        x = self.__input_data
        print(x)
        return 0
