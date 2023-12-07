from common.aoc import AoCDay
from pydantic.dataclasses import dataclass
from collections import deque
@dataclass
class Card:
    name: str
    win: set
    have: set


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = []
        for i in self._input_data[0]:
            win = set([x for x in i.split(': ' )[1].split(' | ')[0].split(' ') if x])
            have = set([x for x in i.split(': ' )[1].split(' | ')[1].split(' ') if x])
            self.__input_data.append(Card(i.split(': ' )[0], win, have))


    def _calculate_1(self):
        result = 0
        for i in self.__input_data:
            # print(f"{i.win}, {i.have}")
            if len(i.win.intersection(i.have)) > 0:
                res =pow(2, len(i.win.intersection(i.have))-1)
                result += res
        return result

    def _calculate_2(self):
        result = 0

        deck={}
        original_deck = self.__input_data
        for i in original_deck:
            deck[i.name] = 1
        print(deck)
        for c, i in enumerate(original_deck):
            # print(f"{i}")
            # print(f"{i.name}, {len(i.win.intersection(i.have))}")
            res =len(i.win.intersection(i.have))
            # print(res)
            for j in range(res):
                # print(original_deck[c+j+1])
                deck[original_deck[c+j+1].name] += 1*deck[i.name]
            #
        print(sum(deck.values()))
        # while x:
        #     i=x.popleft()
        #     print(f"{i}")
        #     # print(f"{i.win}, {i.have}, {i.win.intersection(i.have)}")
        #     print(f"{len(i.win.intersection(i.have))=}")
        #     #
        #     res =len(i.win.intersection(i.have))
        #     print(res)
        #     for j in range(res):
        #         x.append(x[j])
        #     c+=1
        #     if c==6:
        #         break
        # for i in x:
        #     print(i)
        return 0
