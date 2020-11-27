def calculate_1(i: str) -> int:
    l, w, h = [int(x) for x in i.split("x")]
    small_area = min(l * w, l * h, w * h)
    return 2 * l * w + 2 * w * h + 2 * h * l + small_area


def calculate_2(i: str) -> int:
    measures = [int(x) for x in i.split("x")]
    l, w, h = measures
    small_perimeter = sum(2 * x for x in sorted(measures)[:-1])
    return small_perimeter + l * w * h


def main():
    """"""
    with open("y_2015/input_day2.txt") as f:
        x = (f.read()).split("\n")[:-1]

    print(f"sol 1: {sum(calculate_1(i) for i in x)}")
    print(f"sol 1: {sum(calculate_2(i) for i in x)}")


if __name__ == "__main__":
    main()
