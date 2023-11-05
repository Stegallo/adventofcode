import hashlib

from common.aoc import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self) -> None:
        self.__secret_k = self._input_data[0][0]

    def hash_logic(self, num_zeros: int) -> int:
        i = self.__secret_k
        n = 0
        while True:
            result = hashlib.md5(i.encode("ascii") + str(n).encode("ascii")).hexdigest()
            if result[:num_zeros] == "0" * num_zeros:
                return n
            n += 1

    def _calculate_1(self) -> int:
        return self.hash_logic(5)

    def _calculate_2(self) -> int:
        return self.hash_logic(6)
