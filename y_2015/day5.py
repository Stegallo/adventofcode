from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class NiceString:
    text: str

    @property
    def nice(self) -> bool:
        # 3 vovels
        n_vovels = 0
        for i in self.text:
            if i in "aeiou":
                n_vovels += 1
        if n_vovels < 3:
            return False

        # one letter twice
        twice_letter = False
        for c, i in enumerate(self.text):
            if c == len(self.text) - 1:
                break
            if i == self.text[c + 1]:
                twice_letter = True
                break
        if not twice_letter:
            return False

        # not ab, cd, pq, or xy
        if (
            "ab" in self.text
            or "cd" in self.text
            or "pq" in self.text
            or "xy" in self.text
        ):
            return False
        return True

    @property
    def correct_nice(self) -> bool:
        # pair of any two letters that appears at least twice in the string
        # without overlapping
        twice_pair = False
        for c, i in enumerate(self.text):
            if c >= len(self.text) - 2:
                break
            for j in range(c + 2, len(self.text) - 1):
                if self.text[c : c + 2] == self.text[j : j + 2]:
                    twice_pair = True
                    break
        if not twice_pair:
            return False

        # one letter which repeats with exactly one letter between them
        letter_repeat = False
        for c, i in enumerate(self.text):
            if c >= len(self.text) - 2:
                break
            if self.text[c] == self.text[c + 2]:
                letter_repeat = True
                break
        if not letter_repeat:
            return False

        return True


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self) -> None:
        self.__input_data = [NiceString(i) for i in self._input_data[0]]

    def _calculate_1(self) -> int:
        return sum(int(i.nice) for i in self.__input_data)

    def _calculate_2(self) -> int:
        return sum(int(i.correct_nice) for i in self.__input_data)
