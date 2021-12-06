from .common import AoCDay


class Element:
    def __init__(self, raw_element: str):
        self.__element_number = int(raw_element)
        self.__called: bool = False

    def call(self):
        self.__called = True

    def called(self):
        return self.__called

    def __repr__(self):
        return str(f"({self.__element_number}; {self.__called})")


class Board:
    def __init__(self):
        self.__rows = []
        self.__columns = []
        self.__elements: Dict[int, Element] = {}

    def __repr__(self):
        return "\n".join([str(list(rows)) for rows in self.__rows])

    def add_row(self, row_board):
        self.__rows.append([])
        for column, raw_element in enumerate(row_board.split()):
            element = Element(raw_element)
            self.__elements[int(raw_element)] = element
            self.__rows[-1].append(element)
            if column >= len(self.__columns):
                self.__columns.append([])
            self.__columns[column].append(element)

    def winner(self):
        for i in self.__rows:
            if all(j.called() for j in i):
                return True
        return any(all(j.called() for j in i) for i in self.__columns)

    def flag(self, number: int):
        if self.__elements.get(number):
            self.__elements.get(number).call()

    def sum_unmarked(self):
        return sum(key for key, value in self.__elements.items() if not value.called())


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
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

    def _calculate_1(self):
        boards = self.__boards

        for i in self.__extracts:
            for board in boards:
                board.flag(int(i))

            for board in boards:
                if is_winner := board.winner():
                    winner_board = board
                    break
            if is_winner:
                break

        return board.sum_unmarked() * int(i)

    def _calculate_2(self):
        boards = self.__boards

        for i in self.__extracts:
            for board in boards:
                board.flag(int(i))

            for board in boards:
                if board.winner():
                    boards.remove(board)

            if len(boards) == 0:
                winner_board = board
                break

        return board.sum_unmarked() * int(i)
