from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class NiceString:
    text: str

    def __has_3_vovels(self) -> bool:
        return sum(1 for i in self.text if i in "aeiou") >= 3

    def __has_one_letter_twice(self) -> bool:
        twice_letter = False
        for c, i in enumerate(self.text):
            if c == len(self.text) - 1:
                break
            if i == self.text[c + 1]:
                twice_letter = True
                break
        return bool(twice_letter)

    def __has_no_forbidden_pairs(self) -> bool:
        return (
            "ab" not in self.text
            and "cd" not in self.text
            and "pq" not in self.text
            and "xy" not in self.text
        )

    @property
    def nice(self) -> bool:
        return (
            self.__has_3_vovels()
            and self.__has_one_letter_twice()
            and self.__has_no_forbidden_pairs()
        )

    def __has_pair_twice(self) -> bool:
        twice_pair = False
        for c, i in enumerate(self.text):
            if c >= len(self.text) - 2:
                break
            for j in range(c + 2, len(self.text) - 1):
                if self.text[c : c + 2] == self.text[j : j + 2]:
                    twice_pair = True
                    break
        return bool(twice_pair)

    def __has_letter_repeats_with_one_between(self) -> bool:
        letter_repeat = False
        for c, i in enumerate(self.text):
            if c >= len(self.text) - 2:
                break
            if self.text[c] == self.text[c + 2]:
                letter_repeat = True
                break
        return bool(letter_repeat)

    @property
    def correct_nice(self) -> bool:
        return self.__has_pair_twice() and self.__has_letter_repeats_with_one_between()


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self) -> None:
        self.__input_data = [NiceString(i) for i in self._input_data[0]]

    def _calculate_1(self) -> int:
        return sum(int(i.nice) for i in self.__input_data)

    def _calculate_2(self) -> int:
        return sum(int(i.correct_nice) for i in self.__input_data)
