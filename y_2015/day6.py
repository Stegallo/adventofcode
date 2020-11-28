from collections import defaultdict
from typing import DefaultDict
import re

GRID: DefaultDict[tuple, int] = defaultdict(int)


def parse(i):
    command = i[: re.search(" \d", i).start()]
    positions = re.findall("[\d]+,[\d]+", i)
    return (
        command,
        tuple([int(x) for x in positions[0].split(",")]),
        "through",
        tuple([int(x) for x in positions[1].split(",")]),
    )


def operate_ligths(i: str) -> None:
    command, start, _, end = parse(i)
    if command == "turn on":
        for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                GRID[(j, k)] = 1
    if command == "toggle":
        for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                GRID[(j, k)] = 1 - GRID[(j, k)]
    if command == "turn off":
        for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                GRID[(j, k)] = 0


def operate_ligths_second(i: str) -> None:
    command, start, _, end = parse(i)
    if command == "turn on":
        for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                GRID[(j, k)] = GRID[(j, k)] + 1
    if command == "toggle":
        for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                GRID[(j, k)] = GRID[(j, k)] + 2
    if command == "turn off":
        for j in range(start[0], end[0] + 1):
            for k in range(start[1], end[1] + 1):
                GRID[(j, k)] = max(GRID[(j, k)] - 1, 0)


def calculate_1(x: list) -> int:
    for i in x:
        operate_ligths(i)
    result = 0
    for j in GRID:
        result += GRID[j]
    return result


def calculate_2(x: str) -> int:
    for i in x:
        operate_ligths_second(i)
    result = 0
    for j in GRID:
        result += GRID[j]
    return result
