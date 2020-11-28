import re
from collections import defaultdict
from typing import DefaultDict

GRID: DefaultDict[tuple, int] = defaultdict(int)


def parse(i):
    command = i[: re.search(" \d", i).start()]  # noqa W605
    positions = re.findall("[\d]+,[\d]+", i)  # noqa W605
    return (
        command,
        tuple(int(x) for x in positions[0].split(",")),
        "through",
        tuple(int(x) for x in positions[1].split(",")),
    )


def operate_ligths(i: str) -> None:
    command, start, _, end = parse(i)
    for j in range(start[0], end[0] + 1):
        for k in range(start[1], end[1] + 1):
            if command == "toggle":
                GRID[(j, k)] = 1 - GRID[(j, k)]
            elif command == "turn off":
                GRID[(j, k)] = 0
            elif command == "turn on":
                GRID[(j, k)] = 1


def operate_ligths_second(i: str) -> None:
    command, start, _, end = parse(i)
    for j in range(start[0], end[0] + 1):
        for k in range(start[1], end[1] + 1):
            if command == "toggle":
                GRID[(j, k)] = GRID[(j, k)] + 2
            elif command == "turn off":
                GRID[(j, k)] = max(GRID[(j, k)] - 1, 0)
            elif command == "turn on":
                GRID[(j, k)] = GRID[(j, k)] + 1


def calculate_1(x: list) -> int:
    for i in x:
        operate_ligths(i)
    return sum(GRID[j] for j in GRID)


def calculate_2(x: str) -> int:
    for i in x:
        operate_ligths_second(i)
    return sum(GRID[j] for j in GRID)
