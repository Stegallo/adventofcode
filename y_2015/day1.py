def calculate_1(i: str):
    result = 0
    for x in i:
        if x == "(":
            result += 1
        if x == ")":
            result -= 1
    return result


def calculate_2(i):
    for j in range(len(i)):
        if calculate_1(i[: j + 1]) == -1:
            return j + 1
    return -1


def main():
    """"""
    with open("y_2015/input_day1.txt") as f:
        x = f.read()

    print(f"sol 1: {calculate_1(x)}")
    print(f"sol 2: {calculate_2(x)}")


if __name__ == "__main__":
    main()
