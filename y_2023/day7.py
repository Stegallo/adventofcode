from typing import List, Dict
from common.aoc import AoCDay
from pydantic.dataclasses import dataclass
from collections import Counter

RANK_TYPE = {
    "Five of a kind": 1,
    "Four of a kind": 2,
    "Full house": 3,
    "Three of a kind": 4,
    "Two pair": 5,
    "One pair": 6,
    "High card": 7,
}
RANK_CARD = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
}
RANK_CARD_2 = {k: v if k != "J" else 14 for k, v in RANK_CARD.items()}


@dataclass
class Hand:
    cards: str

    def sort_ord(self, type: str) -> List[int]:
        if type == "original":
            return [RANK_CARD[i] for i in self.cards]
        if type == "joker":
            return [RANK_CARD_2[i] for i in self.cards]
        return []

    @property
    def __rate(self) -> str:
        cou = Counter(self.cards)
        if cou.most_common()[0][1] == 5:
            # Five of a kind, where all five cards have the same label: AAAAA
            return "Five of a kind"  # , cou.most_common()[0][0]
        if cou.most_common()[0][1] == 4:
            # Four of a kind, where four cards have the same label and one card
            # has a different label: AA8AA
            return "Four of a kind"  # , cou.most_common()[0][0]
        if cou.most_common()[0][1] == 3 and cou.most_common()[1][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Full house"  # , cou.most_common()[0][0], cou.most_common()[1][0]
        if cou.most_common()[0][1] == 3:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Three of a kind"  # , cou.most_common()[0][0]
        if cou.most_common()[0][1] == 2 and cou.most_common()[1][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Two pair"  # , cou.most_common()[0][0], cou.most_common()[1][0]
        if cou.most_common()[0][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "One pair"  # , cou.most_common()[0][0]

        return "High card"  # , None

    def rate(self, type: str) -> str:
        if type != "joker" or "J" not in self.cards:
            return self.__rate
        str_clone = self.cards
        cou = Counter(self.cards)

        if cou.most_common()[0][1] > 1 and cou.most_common()[0][0] != "J":
            str_clone = str_clone.replace("J", cou.most_common()[0][0])
        if (
            cou.most_common()[0][1] > 1
            and cou.most_common()[0][0] == "J"
            and cou.most_common()[0][1] < 5
        ):
            str_clone = str_clone.replace("J", cou.most_common()[1][0])
        if cou.most_common()[0][1] == 1 and cou.most_common()[0][0] == "J":
            str_clone = str_clone.replace("J", cou.most_common()[1][0])
        if cou.most_common()[0][1] == 1 and cou.most_common()[0][0] != "J":
            str_clone = str_clone.replace("J", cou.most_common()[0][0])

        cou = Counter(str_clone)
        if cou.most_common()[0][1] == 5:
            # Five of a kind, where all five cards have the same label: AAAAA
            return "Five of a kind"  # , cou.most_common()[0][0]
        if cou.most_common()[0][1] == 4:
            # Four of a kind, where four cards have the same label and one
            # card has a different label: AA8AA
            return "Four of a kind"  # , cou.most_common()[0][0]
        if cou.most_common()[0][1] == 3 and cou.most_common()[1][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Full house"  # , cou.most_common()[0][0], cou.most_common()[1][0]
        if cou.most_common()[0][1] == 3:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Three of a kind"  # , cou.most_common()[0][0]
        if cou.most_common()[0][1] == 2 and cou.most_common()[1][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Two pair"  # , cou.most_common()[0][0], cou.most_common()[1][0]
        if cou.most_common()[0][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "One pair"  # , cou.most_common()[0][0]

        return "High card"  # , None


@dataclass
class Row:
    hand: Hand
    bid: int


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [
            (lambda x, y: Row(Hand(x), y))(*i.split()) for i in self._input_data[0]
        ]

    def __compute(self, type: str) -> int:
        ranks: Dict[str, List[Row]] = {i: [] for i in RANK_TYPE}
        for i in self.__input_data:
            ranks[i.hand.rate(type)].append(i)

        final_ordering = []
        for i in ranks.values():
            final_ordering.extend(
                sorted([x for x in i], key=lambda x: x.hand.sort_ord(type)),
            )

        result = 0
        for c, i in enumerate(final_ordering):
            result += (len(final_ordering) - c) * int(i.bid)

        return result

    def _calculate_1(self) -> int:  # 246424613
        return self.__compute("original")

    def _calculate_2(self) -> int:  # 248256639
        return self.__compute("joker")
