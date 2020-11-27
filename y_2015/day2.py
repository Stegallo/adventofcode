try:
    from common import load_input
except:
    pass


def get_measures(i: str) -> tuple:
    return [int(x) for x in i.split("x")]


def calculate_1(i: str) -> int:
    l, w, h = get_measures(i)
    small_area = min(l * w, l * h, w * h)
    return 2 * l * w + 2 * w * h + 2 * h * l + small_area


def calculate_2(i: str) -> int:
    measures = get_measures(i)
    l, w, h = measures
    small_perimeter = sum(2 * x for x in sorted(measures)[:-1])
    return small_perimeter + l * w * h


def main():
    """"""
    x = load_input(2)

    print(f"sol 1: {sum(calculate_1(i) for i in x)}")
    print(f"sol 1: {sum(calculate_2(i) for i in x)}")


if __name__ == "__main__":
    main()
