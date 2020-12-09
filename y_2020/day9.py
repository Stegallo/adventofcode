from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(9)

    def _preprocess_input(self):
        self.__input = [int(i) for i in self._input_data]

    def _calculate_1(self, size=25):
        for c, i in enumerate(self.__input[size:]):
            temp = self.__input[c : size + c]
            correct = False
            for j in temp:
                for k in temp:
                    x = j + k
                    if i == x:
                        correct = True
                        break
                if correct:
                    break
            if not correct:
                break

        self.__problem_1_result = i
        return self.__problem_1_result

    def _calculate_2(self, val=None):
        if not val:
            val = self.__problem_1_result
        range = {}
        for c, start_range in enumerate(self.__input):
            range[start_range] = []
            for j in self.__input[c:]:
                range[start_range].append(j)
                if sum(range[start_range]) == val:
                    return start_range + max(range[start_range])
        return 0
