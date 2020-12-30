import re
from .common import AoCDay
from collections import deque
from copy import deepcopy


class Day(AoCDay):
    def __init__(self):
        super().__init__(22)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]
        self.__p1 = deque()
        self.__p2 = deque()
        p1 = False
        p2 = False
        for i in self._input_data:
            # print(i)
            if i == "Player 1:":
                p1 = True
                continue
            if i == "Player 2:":
                p1 = False
                p2 = True
                continue
            if i == "":
                continue
            if p1:
                self.__p1.append(int(i))
            if p2:
                self.__p2.append(int(i))

    def __play_round(self, deck1, deck2):
        if not deck1 or not deck2:
            return False
        p1, p2 = deck1.popleft(), deck2.popleft()

        if p1 > p2:
            # print("1 wins!")
            deck1.extend([p1, p2])
        else:
            # print("2 wins!")
            deck2.extend([p2, p1])
        return True

    def _calculate_1(self):
        p1 = deque(self.__p1)
        p2 = deque(self.__p2)
        while self.__play_round(p1, p2):
            ...
        p = p1 or p2
        l = len(p)
        result = 0
        for i in range(l):
            result += (l - i) * p[i]
        return result

    def recursive_play(self, deck1, deck2):
        seen = set()

        while deck1 and deck2:
            key = tuple(deck1), tuple(deck2)
            if key in seen:
                return True, deck1

            seen.add(key)
            c1, c2 = deck1.popleft(), deck2.popleft()

            if len(deck1) >= c1 and len(deck2) >= c2:
                sub1, sub2 = tuple(deck1)[:c1], tuple(deck2)[:c2]
                p1win, _ = self.recursive_play(deque(sub1), deque(sub2))
            else:
                p1win = c1 > c2

            if p1win:
                deck1.extend((c1, c2))
            else:
                deck2.extend((c2, c1))

        return (True, deck1) if deck1 else (False, deck2)

    def _calculate_2(self):
        _, winner_deck = self.recursive_play(self.__p1, self.__p2)
        l = len(winner_deck)
        result = 0
        for i in range(l):
            result += (l - i) * winner_deck[i]
        return result
