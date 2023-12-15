from typing import List, Dict
from common.aoc import AoCDay
from pydantic.dataclasses import dataclass
from collections import Counter

rank_type = {
    "Five of a kind": 1,
    "Four of a kind": 2,
    "Full house": 3,
    "Three of a kind": 4,
    "Two pair": 5,
    "One pair": 6,
    "High card": 7,
}
rank_card = {
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
rank_card_2 = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
    "J": 14,
}


@dataclass
class Hand:
    cards: str
    # sort_ord: Optional[int] = None
    # sort_ord_2: Optional[int] = None

    # def __post_init__(self) -> None:
    # self.sort_ord = [rank_card[i] for i in self.cards]
    # self.sort_ord_2 = [rank_card_2[i] for i in self.cards]

    @property
    def sort_ord(self) -> List[int]:
        return [rank_card[i] for i in self.cards]

    @property
    def sort_ord_2(self) -> List[int]:
        return [rank_card_2[i] for i in self.cards]

    def rate(self):
        cou = Counter(self.cards)
        if cou.most_common()[0][1] == 5:
            # Five of a kind, where all five cards have the same label: AAAAA
            return "Five of a kind", cou.most_common()[0][0]
        if cou.most_common()[0][1] == 4:
            # Four of a kind, where four cards have the same label and one card
            # has a different label: AA8AA
            return "Four of a kind", cou.most_common()[0][0]
        if cou.most_common()[0][1] == 3 and cou.most_common()[1][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Full house", cou.most_common()[0][0], cou.most_common()[1][0]
        if cou.most_common()[0][1] == 3:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Three of a kind", cou.most_common()[0][0]
        if cou.most_common()[0][1] == 2 and cou.most_common()[1][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "Two pair", cou.most_common()[0][0], cou.most_common()[1][0]
        if cou.most_common()[0][1] == 2:
            # Full house, where three cards have the same label, and the
            # remaining two cards share a different label: 23332
            return "One pair", cou.most_common()[0][0]

        return "High card", None

    def rate2(self):
        if "J" in self.cards:
            # breakpoint()
            str_clone = self.cards
            cou = Counter(self.cards)
            # print(cou)
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
                return "Five of a kind", cou.most_common()[0][0]
            if cou.most_common()[0][1] == 4:
                # Four of a kind, where four cards have the same label and one
                # card has a different label: AA8AA
                return "Four of a kind", cou.most_common()[0][0]
            if cou.most_common()[0][1] == 3 and cou.most_common()[1][1] == 2:
                # Full house, where three cards have the same label, and the
                # remaining two cards share a different label: 23332
                return "Full house", cou.most_common()[0][0], cou.most_common()[1][0]
            if cou.most_common()[0][1] == 3:
                # Full house, where three cards have the same label, and the
                # remaining two cards share a different label: 23332
                return "Three of a kind", cou.most_common()[0][0]
            if cou.most_common()[0][1] == 2 and cou.most_common()[1][1] == 2:
                # Full house, where three cards have the same label, and the
                # remaining two cards share a different label: 23332
                return "Two pair", cou.most_common()[0][0], cou.most_common()[1][0]
            if cou.most_common()[0][1] == 2:
                # Full house, where three cards have the same label, and the
                # remaining two cards share a different label: 23332
                return "One pair", cou.most_common()[0][0]

            return "High card", None
        else:
            return self.rate()


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

    def _calculate_1(self) -> int:  # 246424613
        ranks: Dict[str, List[Row]] = {i: [] for i in rank_type}
        for i in self.__input_data:
            ranks[i.hand.rate()[0]].append(i)

        final_ordering = []
        for i in ranks.values():
            final_ordering.extend(sorted([x for x in i], key=lambda x: x.hand.sort_ord))

        result = 0
        for c, i in enumerate(final_ordering):
            result += (len(final_ordering) - c) * int(i.bid)

        return result

    def _calculate_2(self) -> int:  # 248256639
        ranks: Dict[str, List[Row]] = {i: [] for i in rank_type}
        for i in self.__input_data:
            ranks[i.hand.rate2()[0]].append(i)

        final_ordering = []
        for i in ranks.values():
            final_ordering.extend(
                sorted([x for x in i], key=lambda x: x.hand.sort_ord_2),
            )

        result = 0
        for c, i in enumerate(final_ordering):
            result += (len(final_ordering) - c) * int(i.bid)

        return result
