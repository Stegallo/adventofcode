from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    report: Optional[list[int]] = None

    def __post_init__(self) -> None:
        self.report = [int(i) for i in self.original.split()]

    @property
    def safe(self) -> bool:
        return self.is_report_safe(self.report)  # type: ignore

    @property
    def dampener_safe(self) -> bool:
        if self.safe:
            return True
        for remove in range(len(self.report)):  # type: ignore
            dampened_report = (
                self.report[:remove]  # type: ignore
                + self.report[remove + 1 :]  # type: ignore
            )
            if self.is_report_safe(dampened_report):
                return True
        return False

    @staticmethod
    def is_report_safe(report: list[int]) -> bool:
        all_increasing = True
        all_decreasing = True
        for i in range(len(report) - 1):
            if report[i + 1] - report[i] not in (1, 2, 3):
                all_increasing = False
            if report[i] - report[i + 1] not in (1, 2, 3):
                all_decreasing = False
        return all_increasing or all_decreasing


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [Row(i) for i in self._input_data[0]]

    def _calculate_1(self):
        return sum(x.safe for x in self.__input_data)

    def _calculate_2(self):
        return sum(x.dampener_safe for x in self.__input_data)
