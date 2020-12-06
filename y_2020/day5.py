from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(5)

    def _preprocess_input(self):
        self.__decoded_seats = [
            int("".join(["1" if i in ["B", "R"] else "0" for i in encoded_seat]), 2)
            for encoded_seat in self._input_data
        ]

    def _calculate_1(self):
        return max(self.__decoded_seats)

    def _calculate_2(self):
        seats = sorted(self.__decoded_seats)
        for c, value in enumerate((seats)):
            if seats[c] != seats[c + 1] - 1:
                return value + 1
        return 0
