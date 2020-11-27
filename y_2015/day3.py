from collections import defaultdict

OPERATIONS = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}


def deliver(i: str, actors: list) -> int:
    grid = defaultdict(int)
    actor_location = [[1, 1] for i in actors]
    grid[(1, 1)] = 1
    current_actor = 0
    for j in i:
        moves = OPERATIONS[j]
        actor_location[current_actor][0] += moves[0]
        actor_location[current_actor][1] += moves[1]
        grid[tuple(actor_location[current_actor])] = 1
        current_actor = (current_actor + 1) % len(actors)
    return len(grid)


def calculate_1(i: str) -> int:
    return deliver(i, ["santa"])


def calculate_2(i: str) -> int:
    return deliver(i, ["santa", "robo-santa"])
