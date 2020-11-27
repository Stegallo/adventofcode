try:
    from common import load_input
except:
    pass


OPERATIONS = {"(": 1, ")": -1}


def calculate_1(i: str) -> int:
    return sum(OPERATIONS[x] for x in i)


def calculate_2(i: str) -> int:
    result = 0
    for j, x in enumerate(i, start=1):
        result += OPERATIONS[x]
        if result == -1:
            return j


def main():
    """"""
    x = load_input(1)

    print(f"sol 1: {sum(calculate_1(i) for i in x)}")
    print(f"sol 2: {sum(calculate_2(i) for i in x)}")


if __name__ == "__main__":
    main()
