from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Present:
    length: int
    width: int
    height: int

    @property
    def wrapping_paper(self):
        side1 = self.length * self.width
        side2 = self.width * self.height
        side3 = self.height * self.length

        return 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)

    @property
    def ribbon(self):
        ordered_measures = sorted([self.length, self.width, self.height])
        bow = self.length * self.width * self.height

        return 2 * ordered_measures[0] + 2 * ordered_measures[1] + bow


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Present(*i.split("x")) for i in self._input_data[0]]

    def _calculate_1(self):
        return sum(present.wrapping_paper for present in self.__input_data)

    def _calculate_2(self):
        return sum(present.ribbon for present in self.__input_data)
