import re
from pydantic.dataclasses import dataclass
from collections import defaultdict, deque
from common.aoc import AoCDay


@dataclass
class Route:
    start: str
    end: str
    distance: int


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_data = [
            Route(*list(re.search(r"(.*) to (.*) = (\d*)", x).groups()))
            for x in self._input_data[0]
        ]

    def _calculate_1(self):
        distances = defaultdict(dict)
        result = deque()
        result_n = []
        for x in self.__input_data:
            print(f"{x=}")
            distances[x.start][x.end] = x.distance
            distances[x.end][x.start] = x.distance
        print(distances)
        print(len(distances))
        head = x.start
        tail = x.start
        covered = {x.start}
        result.append(x.start)
        remaining = {x for x in distances.keys()} - covered
        print(f"{head=}, {tail=}, {covered=}, {remaining=}")
        for x in remaining:
            print(f"{x=}, {distances[x]=}")
        #     for j in distances[x]:
        #         print(f">>{j=}")
        #         if j in covered:
        #             print('alredy considered')
        #         else:
        #             print('valid candidate')
        #             if j == head:
        #                 breakpoint()

        while remaining:
            # min distance from head
            distance_from_head = 100_000
            close_to_head = None
            for x in remaining:
                if x in covered:
                    continue
                for j in distances[x]:
                    if j == head:
                        print(
                            f"""{x} candidate connection to {head}, """
                            f"""far {distances[x][j]}""",
                        )
                        if distances[x][j] < distance_from_head:
                            distance_from_head = distances[x][j]
                            close_to_head = x

            # min distance from tail
            distance_from_tail = 100_000
            close_to_tail = None
            for x in remaining:
                if x in covered:
                    continue
                for j in distances[x]:
                    if j == tail:
                        print(
                            f"""{x} candidate connection to {tail}, """
                            f"""far {distances[x][j]}""",
                        )
                        if distances[x][j] < distance_from_tail:
                            distance_from_tail = distances[x][j]
                            close_to_tail = x
            print(close_to_head, distance_from_head, close_to_tail, distance_from_tail)
            if distance_from_head < distance_from_tail:
                result.append(close_to_head)
                head = close_to_head
                covered.add(close_to_head)
                result_n.append(distance_from_head)
            else:
                result.appendleft(close_to_tail)
                tail = close_to_tail
                covered.add(close_to_tail)
                result_n.append(distance_from_tail)
            remaining = {x for x in distances.keys()} - covered
            print(f"{head=}, {tail=}, {covered=}, {remaining=}, {result=}")
        print(f"{result=}")
        print(f"{result_n=}")
        # 266 high
        return sum(result_n)

    def _calculate_2(self):
        return 0
        x = self.__input_data
        print(f"{x=}")
        return 0
