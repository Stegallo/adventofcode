from typing import List, Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay

MAX_N = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


@dataclass
class Draw:
    quantity: int
    color: str


@dataclass
class Game:
    original: str
    game_id: Optional[int] = None
    set_cubes: Optional[List[List[Draw]]] = None

    def __post_init__(self) -> None:
        game_id, set_list = self.original.split(": ")
        self.game_id = int(game_id.split(" ")[1])
        self.set_cubes = [
            [Draw(*draw.split()) for draw in i.split(", ")]  # type: ignore[arg-type]
            for i in set_list.split("; ")
        ]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Game(game) for game in self._input_data[0]]

    def _calculate_1(self) -> int:
        result = 0
        for game in self.__input_data:
            possible = True
            for set_cube in game.set_cubes:
                for draw in set_cube:
                    if draw.quantity > MAX_N[draw.color]:
                        possible = False
            if possible:
                result += game.game_id
        return result

    def _calculate_2(self) -> int:
        result = 0
        for game in self.__input_data:
            max_n = {"red": 0, "green": 0, "blue": 0}
            for set_cube in game.set_cubes:
                for draw in set_cube:
                    if draw.quantity > max_n[draw.color]:
                        max_n[draw.color] = draw.quantity
            power = max_n["red"] * max_n["green"] * max_n["blue"]
            result += power
        return result
