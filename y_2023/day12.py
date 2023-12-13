from typing import Optional, List
from functools import lru_cache
from pydantic.dataclasses import dataclass
from itertools import product
from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    map: Optional[str] = None
    check: Optional[str] = None

    def __post_init__(self) -> None:
        self.map, self.check = self.original.split(" ")

    def solve(self) -> int:
        map = self.map
        # for i in map:
        # result = process(map, self.check, 0)
        result = process(map, tuple(self.check.split(",")), 0)
        # for p in PADS.values():
        # print(f"{p=}")
        return result


@dataclass
class Row2:
    original: str
    map: Optional[str] = None
    check: Optional[str] = None

    def __post_init__(self) -> None:
        map, check = self.original.split(" ")
        self.map = map
        self.check = check
        for i in range(4):
            self.map += "?" + map
            self.check += "," + check

    def solve(self) -> int:
        map = self.map
        # for i in map:
        # result = process(map, self.check, 0)
        result = process(map, tuple(self.check.split(",")), 0)
        # for p in PADS.values():
        # print(f"{p=}")
        return result


PADS = {}


@lru_cache
def process(map: str, check: List[str], seq_len) -> int:
    # print(f"{pad}::{map=}, {check=}, {seq_len=}")
    if not map:
        if not check:
            # print(f'sequence complete!!! >>> {pad} <<<')
            return 1
        else:
            return 0
    i = map[0]
    if i == ".":
        # breakpoint()
        # print(f'here we are {i=}, {check=}, {seq_len=}')
        if check and check[0] == ",":
            # breakpoint()
            return process(map[1:], check[1:], 0)
        if check and seq_len == 0:
            return process(map[1:], check, 0)
        else:
            if check and seq_len < int(check[0]):
                return 0
        return process(map[1:], check, seq_len)
    if i == "#":
        seq_len += 1
        # print(f"{pad=}")
        if check:
            # print(f"there is check: {check=}; {check[0]=}")
            # print(f"{seq_len=} vs {check[0]=}")
            if check[0] == ",":
                return 0
            if seq_len == int(check[0]):
                # print(f"valid check: {seq_len=} == {int(check[0])=}")
                # print(f"calling process{(map[1:], check[1:], 0, pad+' ')}")
                # return process(map[1:], check[1:], 0, pad+'#')
                new_c = []
                if len(check) > 1:
                    new_c = [","]
                    new_c.extend(check[1:])
                # print(f"{new_c=}")
                return process(map[1:], tuple(new_c), 0)
            else:
                # print(f"{seq_len=} < {check[0]=}, {int(check[0])=}")
                if seq_len < int(check[0]):
                    # print("in progress")
                    # print(f"calling process{(map[1:], check, seq_len, pad+' ')}")
                    return process(map[1:], check, seq_len)
                else:
                    # print("no valid check")
                    return 0
        else:
            # print("no check")
            return 0
    if i == "?":
        l = [i for i in map[1:]]
        a = ["."]
        a.extend(l)
        b = ["#"]
        b.extend(l)
        # print(f"calling process{(''.join(a), check, seq_len, pad+' ')}")
        # print(f"calling process{(''.join(b), check, seq_len, pad+' ')}")
        r1 = process("".join(a), check, seq_len)
        r2 = process("".join(b), check, seq_len)
        # print(f"{pad}::{map=}, {r1=}, {r2=}\n")
        return r1 + r2
    return 0


def process_old(
    map: str,
    check: List[str],
    current_d,
    original_d,
    pad: str = "",
) -> int:
    PADS[pad] = (map, "")
    # print(f"{pad}, {map=}, {check=}, {current_d=}, {original_d=}")
    if not map:
        if not check or check and check[0] == 0:
            if current_d == original_d:
                PADS[pad] = (map, 1)
                return 1
            if not current_d and not original_d:
                PADS[pad] = (map, 1)
                return 1
        PADS[pad] = (map, 0)
        return 0
    i = map[0]

    # print(i)
    if i == ".":
        # breakpoint()
        if check and check[0] == 0:
            # print('ok')
            # print(map[1:])
            new_original_d = check[1] if len(check) > 1 else None
            return process(map[1:], check[1:], 0, new_original_d, pad + " ")
        else:
            return process(map[1:], check, 0, original_d, pad + " ")
    if i == "#":
        # print(f"{i=}, {map=}, {check}")
        if check:
            # print('ok', check[0])
            if check[0] < 1:
                PADS[pad] = (map, 0)
                return 0
            new_check = [check[0] - 1]
            new_check.extend(check[1:])
            return process(map[1:], new_check, current_d + 1, original_d, pad + " ")
        else:
            PADS[pad] = (map, 0)
            return 0
    if i == "?":
        # k = ['.'] #.extend(map[1:])
        l = [i for i in map[1:]]
        # print(f"{k=}, {l=}")
        # k.extend(l)
        # print(f"{k}")
        a = ["."]
        a.extend(l)
        b = ["#"]
        b.extend(l)
        # print(a, b)
        sol1 = process("".join(a), check, current_d, original_d, pad + " ")
        sol2 = process("".join(b), check, current_d, original_d, pad + " ")
        # print(f"{pad} {sol1=}, {sol2=}")

    PADS[pad] = (map, (sol1 + sol2))
    return sol1 + sol2


def generate_possible(input: str):
    result = []
    # '' -> ['.', '#']
    # '.' -> '.', '.'
    # '.' -> '.', '#'
    # '#' -> '#', '.'
    # '#' -> '#', '#'
    c = 0
    for i in input:
        if i == "?":
            c += 1
    result = list(product([".", "#"], repeat=c))
    result = ["".join(i) for i in result]
    new_result = [[] for i in result]
    # print(f"{new_result=}")

    for c, j in enumerate(new_result):
        d = 0
        for i in input:
            if i == "?":
                # print(f"{i=}")
                # print(f"{result[c]=}")
                # print(f"{result[c][d]=}")
                j.append(result[c][d])
                d += 1
                # print(j)
            else:
                j.append(i)
    # print(f"{new_result=}")
    # new_result.append()
    result = ["".join(i) for i in new_result]
    return result


def is_valid(input: str, check: str) -> bool:
    # print([len(i) for i in input.split('.')])
    input = input.replace(".", " ")
    # print(input.split(''))
    nums = ",".join([str(len(i)) for i in input.split(" ") if i])
    # print(input, nums, check)
    # print(nums, check)
    if nums == check:
        return True
    return False


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = [Row(i) for i in self._input_data[0]]
        self.__input_data2 = [Row2(i) for i in self._input_data[0]]

    def _calculate_1(self):
        result = 0
        import json

        with open("day12_result.json", "r") as fp:
            old = json.load(fp)
        # print(len(old))
        # print(sum([len(i) for i in old.values()]))
        # return result
        # if False:
        for k, x in enumerate(self.__input_data):
            # print(f"{x.solve()}, {len(old[str(k)+x.map])}")
            # if x.solve() != len(old[str(k)+x.map]):
            # breakpoint()
            result += x.solve()
        return result

    def _calculate_1_(self):
        self.map = {}
        self.check = {}
        result = 0
        # return result
        # if False:
        for k, x in enumerate(self.__input_data):
            self.map[str(k) + x.map] = []
            self.check[str(k) + x.map] = x.check
            # it+=1
            # print(f"{x.map}")
            y = generate_possible(x.map)
            # print(f"{len(y)}")
            c = 0
            for i in y:
                if is_valid(i, x.check):
                    c += 1
                    self.map[str(k) + x.map].append(i)
            # print(c)
            result += c
        import json

        with open("day12_result.json", "w") as fp:
            # json.dump(self.map, fp)
            json.dump(self.map, fp)
        # for i in self.map:
        #     print(i, len(self.map[i]))
        return result

    def _calculate_2(self):
        result = 0
        for x in self.__input_data2:
            result += x.solve()
        return result
        return result
        c = 0
        # for i in self.map:
        #     # print(i)
        #     for j in self.map[i]:
        #         # print(j, self.check[i])
        #         check = self.check[i]
        #         # continue
        #         map=j
        #         for _ in range(4):
        #             check += ','+check
        #             map += '?' + map
        #         y = generate_possible(map)
        #
        #         for k in y:
        #             if is_valid(k, check):
        #                 print(k, check)
        #                 c+=1
        #                 result += 1
        # return result
        # return result
        # ???.###????.###????.###????.###????.###
        # ???.###????.###????.###????.###????.###
        for x in self.__input_data:
            check = x.check
            map = x.map
            for i in range(4):
                check += "," + x.check
                map += "?" + x.map
            print(check, map)
            # it+=1
            # print(f"{x.map}")
            # y = generate_possible(x.map*5)
            # print(f"{len(y)}")
            c = 0
            # for i in y:
            #     if is_valid(i, x.check):
            #         c+=1
            # print(c)
            result += c
            # break
        return result
