from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = list(self._input_data)

    def _calculate_1(self):
        max = 0
        partial = 0
        for i in self.__input_data:
            if i == "":
                if partial > max:
                    max = partial
                partial = 0
            else:
                partial += int(i)

        return max

    def _calculate_2(self):
        partials = []
        partial = 0
        counter = 0
        for i in self.__input_data:
            if i == "":
                partials.append(partial)
                partial = 0
                counter += 1
            else:
                partial += int(i)

        partials = sorted(partials)
        return sum(partials[-3:])
