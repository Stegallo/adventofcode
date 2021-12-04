from .common import AoCDay


class Element:
    def __init__(self):
        ...


class Board:
    def __init__(self):
        ...


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = [i for i in self._input_data]
        # self.__input_data = [int(i) for i in self._input_data]
        print(f"len of input = {len(self.__input_data)}")
        try:
            print(f"first value = {self.__input_data[0]}")
            print(f"mid value = {self.__input_data[len(self.__input_data)//2]}")
            print(f"last value = {self.__input_data[-1]}")
        except:
            ...
        self.__extracts = self.__input_data[0].split(",")
        self.__boards = []
        board_index = -1
        for row_board in self.__input_data[1:]:
            if row_board == "":
                board_index += 1
                self.__boards.append([])
            else:
                self.__boards[board_index].append(
                    [{int(j): 0} for j in row_board.split()]
                )

    def _calculate_1(self):
        boards = self.__boards
        print(boards)
        # for i in input_data[:2]:
        for i in self.__extracts:
            print(i)
            # flag()
            for board in boards:
                # print(f"{line=}")
                for line in board:
                    # print(f"{pos=}")
                    for elem in line:
                        # print(f"{elem=}")
                        if int(i) in elem:
                            elem[int(i)] = 1
            # check_winner()
            found = False
            winner_board = None
            total_boards = len(boards)
            for board in boards:
                for line in board:
                    if sum(sum(elem.values()) for elem in line) == 5:
                        print("winner")
                        found = True
                        break
                        raise Exception()
                    if found:
                        break

                    # for elem in line:
                    #     print(sum(elem.values()))
                for column in range(5):
                    sum_v = 0
                    for line in board:
                        sum_v += sum(line[column].values())
                    if sum_v == 5:
                        print("winner")
                        found = True
                        break
                        raise Exception()
                    if found:
                        break
                if found:
                    break
            if found:
                winner_board = board
                break

        # print(board)
        score = 0
        for line in board:
            for elem in line:
                if sum(elem.values()) == 0:
                    score += sum(elem.keys())
        print(f"{score=}")

        result = score * int(i)

        return result

    def _calculate_2(self):
        boards = self.__boards
        print(boards)
        # for i in input_data[:2]:
        for i in self.__extracts:
            print(i)
            # flag()
            for board in boards:
                # print(f"{line=}")
                for line in board:
                    # print(f"{pos=}")
                    for elem in line:
                        # print(f"{elem=}")
                        if int(i) in elem:
                            elem[int(i)] = 1
            # check_winner()

            winner_board = None
            # total_boards = len(boards)
            for board in boards:
                found = False
                for line in board:
                    if sum(sum(elem.values()) for elem in line) == 5:
                        print("winner")
                        found = True
                        break
                        raise Exception()
                if found:
                    try:
                        boards.remove(board)
                        print(f"board removed {board}")
                        continue
                    except Exception:
                        print("board not exists")
                    # break

                # for elem in line:
                #     print(sum(elem.values()))
                for column in range(5):
                    sum_v = 0
                    for line in board:
                        sum_v += sum(line[column].values())
                    if sum_v == 5:
                        print("winner")
                        found = True
                        break
                        raise Exception()
                    if found:
                        break
                if found:
                    try:
                        boards.remove(board)
                        print(f"board removed {board}")
                    except Exception:
                        print("board not exists")
                    # break
                # if found:
                #     break
            # if found:
            #     boards.remove(board)
            print(f"{len(boards)=}")
            if len(boards) == 0:
                winner_board = board
                break
        print(winner_board)
        score = 0
        print(board)

        if not winner_board:
            winner_board = board
        for line in winner_board:
            for elem in line:
                if sum(elem.values()) == 0:
                    score += sum(elem.keys())
        print(f"{score=}; {i=}")

        result = score * int(i)

        return result
