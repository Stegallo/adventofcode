from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = []
        sublist = []
        for c, elem in enumerate(self._input_data):
            if elem != "":
                sublist.append(int(elem))
                if c == len(self._input_data) - 1:
                    self.__input_data.append(sublist)
            else:
                self.__input_data.append(sublist)
                sublist = []

    def _calculate_1(self):
        return max(sum(i) for i in self.__input_data)

    def _calculate_2(self):
        return sum(sorted([sum(i) for i in self.__input_data])[-3:])
