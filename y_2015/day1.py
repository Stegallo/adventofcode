OPERATIONS = {"(": 1, ")": -1}


def calculate_1(i: str):
    return sum(OPERATIONS[x] for x in i)


def calculate_2(i):
    result = 0
    for j, x in enumerate(i, start=1):
        result += OPERATIONS[x]
        if result == -1:
            return j


def main():
    """"""
    with open("y_2015/input_day1.txt") as f:
        x = f.read()

    print(f"sol 1: {calculate_1(x)}")
    print(f"sol 2: {calculate_2(x)}")


if __name__ == "__main__":
    main()
