from .common import AoCDay

DIRECTIONS = ["N", "E", "S", "W"]
DEGREES = {90: 1, 180: 2, 270: 3}


class Day(AoCDay):
    def __init__(self):
        super().__init__(12)

    def _preprocess_input(self):
        self.__input = [(i[0], int(i[1:])) for i in self._input_data]

    def _rotate(self, dir, degree, order):
        x = 1
        if order != "R":
            x = -1

        for c, i in enumerate(DIRECTIONS):
            if i == dir:
                return DIRECTIONS[(c + x * DEGREES[degree]) % 4]

    def _calculate_1(self):
        pos = (0, 0)

        direction = "E"
        MOVES = {
            "E": (0, 1),
            "W": (0, -1),
            "N": (1, 0),
            "S": (-1, 0),
        }
        for i in self.__input:
            if i[0] == "F":
                pos = (
                    pos[0] + MOVES[direction][0] * i[1],
                    pos[1] + MOVES[direction][1] * i[1],
                )
            if i[0] == "E":
                pos = (pos[0], pos[1] + i[1])
            if i[0] == "W":
                pos = (pos[0], pos[1] - i[1])
            if i[0] == "N":
                pos = (pos[0] + i[1], pos[1])
            if i[0] == "S":
                pos = (pos[0] - i[1], pos[1])
            if i[0] == "L":
                direction = self._rotate(direction, i[1], "L")
            if i[0] == "R":
                direction = self._rotate(direction, i[1], "R")

        return abs(pos[0]) + abs(pos[1])

    def _calculate_2(self):
        waypoint_pos = (1, 10)
        pos = (0, 0)
        for i in self.__input:
            increment = (waypoint_pos[0] - pos[0], waypoint_pos[1] - pos[1])
            if i[0] == "F":
                for j in range(i[1]):
                    pos = (
                        pos[0] + increment[0],  # - pos[0],
                        pos[1] + increment[1],  # - pos[1],
                    )
                waypoint_pos = (pos[0] + increment[0], pos[1] + increment[1])
            if i[0] == "E":
                waypoint_pos = (waypoint_pos[0], waypoint_pos[1] + i[1])
            if i[0] == "W":
                waypoint_pos = (waypoint_pos[0], waypoint_pos[1] - i[1])
            if i[0] == "N":
                waypoint_pos = (waypoint_pos[0] + i[1], waypoint_pos[1])
            if i[0] == "S":
                waypoint_pos = (waypoint_pos[0] - i[1], waypoint_pos[1])
            if i[0] == "L":
                if i[1] == 90:
                    waypoint_pos = (pos[0] + increment[1], pos[1] - increment[0])
                if i[1] == 180:
                    waypoint_pos = (pos[0] - increment[0], pos[1] - increment[1])
                if i[1] == 270:
                    waypoint_pos = (pos[0] - increment[1], pos[1] + increment[0])
            if i[0] == "R":
                if i[1] == 90:
                    waypoint_pos = (pos[0] - increment[1], pos[1] + increment[0])
                if i[1] == 180:
                    waypoint_pos = (pos[0] - increment[0], pos[1] - increment[1])
                if i[1] == 270:
                    waypoint_pos = (pos[0] + increment[1], pos[1] - increment[0])

        return abs(pos[0]) + abs(pos[1])
