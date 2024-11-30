from common.aoc import AoCDay


def diffrences(input):
    diff = []
    for i in range(len(input)-1):
        # print(int(input[i+1]) - int(input[i]))
        diff.append(int(input[i+1]) - int(input[i]))
    if set(diff) == {0}:
        print('zeros')
        return 0
    else:
        # breakpoint()
        x  = diffrences(diff)
        diff.append(diff[-1]+x)
        # print(diff)
        return diff[-1]

def diffrences2(input):
    diff = []
    for i in range(len(input)-1):
        # print(int(input[i+1]) - int(input[i]))
        diff.append(int(input[i+1]) - int(input[i]))
    if set(diff) == {0}:
        print('zeros')
        return 0
    else:
        # breakpoint()
        x  = diffrences2(diff)
        new_diff = [diff[0]-x]
        new_diff.extend(diff[1:])
        diff = list(new_diff)
        print(diff)
        return diff[0]
class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        print(f"{self._input_data=}")
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        result = 0
        for x in self.__input_data:
            # print(f"{x.split()}")
            y = x.split()
            z = diffrences(x.split())
            print(f"{z=}")
            result+=(int(y[-1])+z)
        return result

    def _calculate_2(self):
        result = 0
        for x in self.__input_data:
            # print(f"{x.split()}")
            y = x.split()
            z = diffrences2(x.split())
            print(f"{z=}")
            result+=(int(y[0])-z)
        return result
