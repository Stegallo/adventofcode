from utils import load_input


def calculate_1(i):
    return i // 3 - 2


def calculate_2(i):
    if (w:= calculate_1(i)) < 0:
        return 0
    return w + calculate_2(w)


def main():
    input_data = load_input()
    result = [(calculate_1(i), calculate_2(i)) for i in input_data]
    print(f"sol 1: {sum(i for i, j in result)}")
    print(f"sol 2: {sum(j for i, j in result)}")


if __name__ == "__main__":
    main()
