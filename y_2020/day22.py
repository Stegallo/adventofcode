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
            print(i)
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

    def __play_round(self, player):
        if not self.__p1 or not self.__p2:
            return False
        p1 = self.__p1.popleft()
        p2 = self.__p2.popleft()
        # print(f"{p1=}")
        # print(f"{p2=}")
        if p1 > p2:
            # print("1 wins!")
            self.__p1.append(p1)
            self.__p1.append(p2)
        else:
            # print("2 wins!")
            self.__p2.append(p2)
            self.__p2.append(p1)
        return True

    def _calculate_1(self):
        players = [1, 2]
        i = 0
        while self.__play_round(players[i]):
            i = (i + 1) % 2
        # print(self.__p1)
        # print(self.__p2)
        p = self.__p1 or self.__p2
        l = len(p)
        result = 0
        for i in range(l):
            # print(f"{l-i=}, {p[i]=}")
            result += (l - i) * p[i]
        return result

    def _calculate_2(self):
        return 0
