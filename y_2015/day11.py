from common.aoc import AoCDay


def increment_string(source: str) -> str:
    reversed_source = source[::-1]
    incremented = []
    act = 1
    for i in reversed_source:
        # print(i)
        if not act:
            incremented.append(i)
            continue
        if i == "z":
            incremented.append("a")
        else:
            incremented.append(chr(ord(i) + 1))
            act = 0
    if act:
        incremented.append("a")

    return "".join(incremented[::-1])


def increasing(source) -> bool:
    consec = 0
    for c, i in enumerate(source):
        if consec == 0:
            consec = 1
            continue
        if chr(ord(source[c - 1]) + 1) == i:
            consec += 1
        else:
            consec = 1
        if consec == 3:
            return True
    return False


def not_iol(source) -> bool:
    return not ("i" in source or "o" in source or "l" in source)


def pairs(source) -> bool:
    first_pair = None
    for c, i in enumerate(source):
        if c == 0:
            continue
        if source[c - 1] == i:
            if first_pair and first_pair != i:
                return True
            first_pair = i
    return False


def valid(source: str) -> bool:
    return increasing(source) and not_iol(source) and pairs(source)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self) -> None:
        self.__input_data = self._input_data[0][0]

    def _calculate_1(self) -> str:
        proposed_pwd = increment_string(self.__input_data)
        while not valid(proposed_pwd):
            proposed_pwd = increment_string(proposed_pwd)
        self.cached_solution_1 = proposed_pwd
        return proposed_pwd

    def _calculate_2(self) -> str:
        x = self.cached_solution_1
        proposed_pwd = increment_string(x)
        while not valid(proposed_pwd):
            proposed_pwd = increment_string(proposed_pwd)
        return proposed_pwd
