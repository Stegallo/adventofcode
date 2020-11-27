OPERATIONS = {"(": 1, ")": -1}


def calculate_1(i: str) -> int:
    return sum(OPERATIONS[x] for x in i)


def calculate_2(i: str) -> int:
    result = 0
    for j, x in enumerate(i, start=1):
        result += OPERATIONS[x]
        if result == -1:
            return j
