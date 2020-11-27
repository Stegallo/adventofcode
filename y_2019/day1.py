def calculate_1(i):
    return i // 3 - 2


def calculate_2(i):
    if (w := calculate_1(i)) < 0:
        return 0
    return w + calculate_2(w)


def main():
    """"""
    with open("y_2019/input_day1.txt") as f:
        x = [int(i) for i in f.read().split("\n")[:-1]]

    print(f"sol 1: {sum(i for i in [calculate_1(i) for i in x])}")
    print(f"sol 2: {sum(i for i in [calculate_2(i) for i in x])}")


if __name__ == "__main__":
    main()
