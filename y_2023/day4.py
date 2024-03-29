from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Card:
    original: str
    name: Optional[str] = None
    win: Optional[set] = None
    have: Optional[set] = None

    def __post_init__(self) -> None:
        self.name = self.original.split(": ")[0]
        self.win = {
            x for x in self.original.split(": ")[1].split(" | ")[0].split(" ") if x
        }
        self.have = {
            x for x in self.original.split(": ")[1].split(" | ")[1].split(" ") if x
        }


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = []
        self.__input_data.extend(Card(i) for i in self._input_data[0])

    def _calculate_1(self) -> int:
        result = 0
        for i in self.__input_data:
            if len(i.win.intersection(i.have)) > 0:
                res = pow(2, len(i.win.intersection(i.have)) - 1)
                result += res

        return result

    def _calculate_2(self) -> int:
        original_deck = self.__input_data
        deck = {i.name: 1 for i in original_deck}
        for c, i in enumerate(original_deck):
            res = len(i.win.intersection(i.have))
            for j in range(res):
                deck[original_deck[c + j + 1].name] += 1 * deck[i.name]

        return sum(deck.values())
