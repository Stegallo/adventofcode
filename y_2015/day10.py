from common.aoc import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0][0]

    def say_loud(self, x: str) -> str:
        if len(x) == 1:
            return f"1{x[0]}"
        chunks = []
        chunk = [x[0]]
        for c in range(len(x)):
            if c == 0:
                continue

            if x[c - 1] == x[c]:
                chunk.append(x[c])
            else:
                chunks.append(chunk)
                chunk = [x[c]]
        chunks.append(chunk)
        k = [str(len(i)) + i[0] for i in chunks]
        return "".join(k)

    def _apply_times(self, input: str, times: int) -> str:
        result = input
        for _ in range(times):
            result = self.say_loud(result)
        return result

    def _calculate_1(self):
        return len(self._apply_times(self.__input_data, 40))

    def _calculate_2(self):
        return len(self._apply_times(self.__input_data, 50))
