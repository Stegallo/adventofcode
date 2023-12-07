from common.aoc import AoCDay

MAX_N = {"red": 12, "green": 13, "blue": 14}


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        result = 0
        x = self.__input_data
        for game in x:
            pairs = game.split(": ")[1].split("; ")
            # print(f"{pairs=}, {len(pairs)=}")
            possible = True
            for pair in pairs:
                print(pair.split(", "))
                for m in pair.split(", "):
                    tuple = m.split(" ")
                    # print(f"{tuple=}")
                    if int(tuple[0]) > MAX_N[tuple[1]]:
                        # print('impossibl')
                        possible = False
            if possible:
                result += int(game.split(":")[0].split(" ")[1])
        print(result)
        return result

    def _calculate_2(self):
        result = 0
        for game in self.__input_data:
            max_n = {"red": 0, "green": 0, "blue": 0}
            pairs = game.split(": ")[1].split("; ")
            for pair in pairs:
                # print(pair.split(', '))
                for m in pair.split(", "):
                    tuple = m.split(" ")
                    # print(f"{tuple}")
                    if int(tuple[0]) > max_n[tuple[1]]:
                        max_n[tuple[1]] = int(tuple[0])
            print(max_n)
            power = max_n["red"] * max_n["green"] * max_n["blue"]
            result += power
        return result
        x = self.__input_data
        print(f"{x=}")
