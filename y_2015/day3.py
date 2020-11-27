from collections import defaultdict

try:
    from common import load_input
except:
    pass

OPERATIONS = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}


def calculate_1(i: str) -> int:
    # print(i)
    grid = defaultdict(int)
    x = 1
    y = 1
    grid[(x, y)] = 1
    for j in i:
        # print(x)
        moves = OPERATIONS[j]
        # print(moves)
        # breakpoint()
        x += moves[0]
        y += moves[1]
        grid[(x, y)] = 1
    return len(grid)


def calculate_2(i: str) -> int:
    # print(i)
    grid = defaultdict(int)
    sx = 1
    sy = 1
    rx = 1
    ry = 1
    grid[(1, 1)] = 1
    s_moves = 1
    for j in i:
        # print(x)
        moves = OPERATIONS[j]
        # print(moves)
        # breakpoint()
        if s_moves:
            sx += moves[0]
            sy += moves[1]
            grid[(sx, sy)] = 1
        else:
            rx += moves[0]
            ry += moves[1]
            grid[(rx, ry)] = 1
        s_moves = (s_moves + 1) % 2
    return len(grid)
