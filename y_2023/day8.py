from typing import List, Dict

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Input:
    instructions: str
    network: Dict[str, List[str]]

    @staticmethod
    def from_source(source: List):
        instructions, network = source
        return Input(
            instructions[0],
            dict(
                [
                    (lambda x, y: (x, y.split(", ")))(
                        *i.replace("(", "").replace(")", "").split(" = "),
                    )
                    for i in network
                ],
            ),
        )


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self) -> None:
        self.__input_data = Input.from_source(self._input_data)

    def _calculate_1(self) -> int:
        print(f"{self.__input_data=}")
        return 0

    def _calculate_2(self) -> int:
        return 0
