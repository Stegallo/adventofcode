from dataclasses import dataclass

from .common import AoCDay

OPPONENT_MAP = {"A": "R", "B": "P", "C": "S"}
PLAYER_MAP = {"X": "R", "Y": "P", "Z": "S"}


@dataclass
class RPS_Round:
    """Round in Rock Paper Scissors game."""

    opponent: str
    player: str

    shape_values = {"R": 1, "P": 2, "S": 3}

    def __outcome(self):  # sourcery skip: assign-if-exp, reintroduce-else
        if self.opponent == self.player:
            return 3
        if self.opponent == "S" and self.player == "R":
            return 6
        if self.opponent == "P" and self.player == "S":
            return 6
        if self.opponent == "R" and self.player == "P":
            return 6
        return 0

    @property
    def score(self):
        return self.shape_values[self.player] + self.__outcome()


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]

    def __strategy(self, x):
        if x[1] == "Y":  # draw
            return OPPONENT_MAP[x[0]]
        if x[1] == "X":  # lose
            if OPPONENT_MAP[x[0]] == "R":
                return "S"
            if OPPONENT_MAP[x[0]] == "S":
                return "P"
            if OPPONENT_MAP[x[0]] == "P":
                return "R"
        if x[1] == "Z":  # win
            if OPPONENT_MAP[x[0]] == "R":
                return "P"
            if OPPONENT_MAP[x[0]] == "S":
                return "R"
            if OPPONENT_MAP[x[0]] == "P":
                return "S"

    def _calculate_1(self):
        incr = 0
        for i in self.__input_data:
            raw_round = i.split(" ")
            rps_round = RPS_Round(OPPONENT_MAP[raw_round[0]], PLAYER_MAP[raw_round[1]])
            incr += rps_round.score
        return incr

    def _calculate_2(self):
        incr = 0
        for i in self.__input_data:
            raw_round = i.split(" ")
            r = raw_round
            response = self.__strategy(raw_round)
            rps_round = RPS_Round(OPPONENT_MAP[r[0]], response)
            incr += rps_round.score
        return incr
