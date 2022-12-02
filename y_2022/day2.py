from dataclasses import dataclass

from .common import AoCDay

OPPONENT_MAP = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
PLAYER_MAP = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}

WINNING_PAIRS = [
    # second entry defeats first
    ("SCISSORS", "ROCK"),
    ("PAPER", "SCISSORS"),
    ("ROCK", "PAPER"),
]


@dataclass
class RPS_Round:
    """Round in Rock Paper Scissors game."""

    opponent: str
    player: str

    shape_values = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

    def __outcome(self):  # sourcery skip: assign-if-exp, reintroduce-else
        if self.opponent == self.player:
            return 3
        if (self.opponent, self.player) in WINNING_PAIRS:
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

    def __strategy(self, raw_round):
        if raw_round[1] == "Y":  # draw
            return OPPONENT_MAP[raw_round[0]]
        if raw_round[1] == "X":  # lose
            return {i[1]: i[0] for i in WINNING_PAIRS}[OPPONENT_MAP[raw_round[0]]]
        if raw_round[1] == "Z":  # win
            return {i[0]: i[1] for i in WINNING_PAIRS}[OPPONENT_MAP[raw_round[0]]]

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
