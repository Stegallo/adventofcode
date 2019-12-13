from collections import defaultdict

from utils import load_input
T = 0

SPY = []
SPS = []

def traverse(c, d, x):
    global T
    print(f"{x=}")

    if not x:
        return c
    for i in x:

        T = T + c + 1
        traverse(c+1, d, d[i])


def calculate_1(l):
    global T
    T = 0
    d = defaultdict(list)
    print(f"{l=}")
    for i in l:
        print(f"{i=}")
        o = i.split(")")
        print(o)
        d[o[0]].append(o[1])
    print(d)

    traverse(0, d, d['COM'])
    return T


def traverse2(c, d, x, w, SP):
    for i in d[x]:
        print(f"{i=}")
        if i==w:
            print('hi')
            SP.append(x)
            return x
        k = traverse2(c+1, d, i, w, SP)
        if k:
            SP.append(x)
            return k

    return False

def calculate_2(l):
    d = defaultdict(list)
    for i in l:
        o = i.split(")")
        d[o[0]].append(o[1])
    print(d)

    traverse2(0, d, 'COM', 'SAN', SPY)
    print(f"{list(reversed(SPY))=}")
    traverse2(0, d, 'COM', 'YOU', SPS)
    print(f"{list(reversed(SPS))=}")
    for i in range(0, max(len(SPY), len(SPS))):
        print(list(reversed(SPY))[i], list(reversed(SPS))[i])
        if list(reversed(SPY))[i] != list(reversed(SPS))[i]:
            break
    print()
    print(list(reversed(SPY))[i], list(reversed(SPS))[i])
    # print(i)
    print(f"{SPY=}")
    print(f"{SPS=}")
    print(len(SPY)-i+len(SPS)-i)
    return len(SPY)-i+len(SPS)-i


def main():
    input_data = load_input()
    # print(input_data)
    # calculate_1(i)
    # calculate_2(i)
    res_1 = calculate_1(input_data)
    res_2 = calculate_2(input_data)
    print(f"sol 1: {res_1}")
    print(f"sol 1: {res_2}")


if __name__ == "__main__":
    main()


def test_calculate_1():
    assert calculate_1([]) == 0
    assert calculate_1(["COM)B"]) == 1
    assert calculate_1(["COM)B", "COM)C"]) == 2
    assert calculate_1(["COM)B", "B)C", "C)D"]) == 6
    # assert calculate_1(["COM)B", "B)C", "C)D", "D)E", "E)J", "J)K", "K)L",]) == 7
    assert (
        calculate_1(
            [
                "COM)B",
                "B)C",
                "C)D",
                "D)E",
                "E)F",
                "B)G",
                "G)H",
                "D)I",
                "E)J",
                "J)K",
                "K)L",
            ]
        )
        == 42
    )


def test_calculate_2():
    print()
    assert (
        calculate_2(
            [
                "COM)B",
                "B)C",
                "C)D",
                "D)E",
                "E)F",
                "B)G",
                "G)H",
                "D)I",
                "E)J",
                "J)K",
                "K)L",
                "K)YOU",
                "I)SAN",
            ]
        )
        == 4
    )
