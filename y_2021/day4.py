from typing import Dict, List

from .common import AoCDay


class Element:
    def __init__(self, raw_element: str) -> None:
        self.__element_number: int = int(raw_element)
        self.__called: bool = False

    def call(self) -> None:
        self.__called = True

    def called(self) -> bool:
        return self.__called

    def __repr__(self) -> str:
        return str(f"({self.__element_number}; {self.__called})")


class Board:
    def __init__(self) -> None:
        self.__rows: List = []
        self.__columns: List = []
        self.__elements: Dict[int, Element] = {}

    def __repr__(self) -> str:
        return "\n".join([str(list(rows)) for rows in self.__rows])

    def add_row(self, row_board: str) -> None:
        self.__rows.append([])
        for column, raw_element in enumerate(row_board.split()):
            element = Element(raw_element)
            self.__elements[int(raw_element)] = element
            self.__rows[-1].append(element)
            if column >= len(self.__columns):
                self.__columns.append([])
            self.__columns[column].append(element)

    def winner(self) -> bool:
        for i in self.__rows:
            if all(j.called() for j in i):
                return True
        return any(all(j.called() for j in i) for i in self.__columns)

    def flag(self, number: int) -> None:
        if self.__elements.get(number):
            self.__elements.get(number).call()

    def sum_unmarked(self) -> int:
        return sum(key for key, value in self.__elements.items() if not value.called())


class Day(AoCDay):
    def __init__(self, test: int = 0) -> None:
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self) -> None:
        self.__input_data = list(self._input_data)
        self.__extracts = self.__input_data[0].split(",")
        self.__boards = []

        for row_board in self.__input_data[1:]:
            if row_board == "":
                # new board!
                board = Board()
                self.__boards.append(board)
            else:
                board.add_row(row_board)

    def _calculate_1(self) -> int:
        boards = self.__boards

        for i in self.__extracts:
            for board in boards:
                board.flag(int(i))

            for board in boards:
                if is_winner := board.winner():
                    break
            if is_winner:
                break

        return board.sum_unmarked() * int(i)

    def _calculate_2(self) -> int:
        boards = self.__boards

        for i in self.__extracts:
            for board in boards:
                board.flag(int(i))

            for board in boards:
                if board.winner():
                    boards.remove(board)

            if len(boards) == 0:
                break

        return board.sum_unmarked() * int(i)
