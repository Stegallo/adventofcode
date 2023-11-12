import re
from pydantic.dataclasses import dataclass
from collections import defaultdict, deque
from common.aoc import AoCDay


@dataclass
class Route:
    start: str
    end: str
    distance: int


def touch_all(i, distances):
    potenziali = {x: 100_000 for x in distances.keys()}
    fringe = deque()
    fringe.append(i)
    potenziali[i] = 0
    print(f"{i=}, {potenziali=}")
    tot_dist = 0
    while fringe:
        j = fringe.popleft()
        print(f"{fringe=}")
        for k in distances[j]:
            print(j, k, distances[j][k])
            if potenziali[j] + distances[j][k] < potenziali[k]:
                potenziali[k] = potenziali[j] + distances[j][k]
                print(f"{potenziali=}, {fringe=}")
                if k not in fringe:
                    fringe.append(k)

        # while remaining:
        #     min_dist = 100_000
        #     close = None
        #     for i in fringe:
        #         for j in distances[i]:
        #             if j in fringe:
        #                 print(f"processing {i}: {j} already in {fringe}")
        #                 continue
        #             print(f"{j=}, {distances[i][j]}")
        #             if distances[i][j] < min_dist:
        #                 min_dist = distances[i][j]
        #                 close = j
        #     # breakpoint()
        #     tot_dist += min_dist
        #     fringe.add(close)
        #     remaining = remaining-{close}
        print(f"{fringe=}, {potenziali=}, {tot_dist}")
    return max(potenziali.values())


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
        # result = deque()
        result_n = []
        for x in self.__input_data:
            print(f"{x=}")
            distances[x.start][x.end] = x.distance
            distances[x.end][x.start] = x.distance
        print(distances)
        print(len(distances))
        for i in distances:
            result_n.append(touch_all(i, distances))
            print(f"{i}; {result_n=}")
        # head = x.start
        # tail = x.start
        # covered = {x.start}
        # result.append(x.start)
        # remaining = {x for x in distances.keys()} - covered
        # print(f"{head=}, {tail=}, {covered=}, {remaining=}")
        # for x in remaining:
        #     print(f"{x=}, {distances[x]=}")
        # #     for j in distances[x]:
        # #         print(f">>{j=}")
        # #         if j in covered:
        # #             print('alredy considered')
        # #         else:
        # #             print('valid candidate')
        # #             if j == head:
        # #                 breakpoint()
        #
        # while remaining:
        #     # min distance from head
        #     distance_from_head = 100_000
        #     close_to_head = None
        #     for x in remaining:
        #         if x in covered:
        #             continue
        #         for j in distances[x]:
        #             if j == head:
        #                 print(
        #                     f"""{x} candidate connection to {head}, """
        #                     f"""far {distances[x][j]}""",
        #                 )
        #                 if distances[x][j] < distance_from_head:
        #                     distance_from_head = distances[x][j]
        #                     close_to_head = x
        #
        #     # min distance from tail
        #     distance_from_tail = 100_000
        #     close_to_tail = None
        #     for x in remaining:
        #         if x in covered:
        #             continue
        #         for j in distances[x]:
        #             if j == tail:
        #                 print(
        #                     f"""{x} candidate connection to {tail}, """
        #                     f"""far {distances[x][j]}""",
        #                 )
        #                 if distances[x][j] < distance_from_tail:
        #                     distance_from_tail = distances[x][j]
        #                     close_to_tail = x
        #     print(close_to_head, distance_from_head, close_to_tail,
        # distance_from_tail)
        #     if distance_from_head < distance_from_tail:
        #         result.append(close_to_head)
        #         head = close_to_head
        #         covered.add(close_to_head)
        #         result_n.append(distance_from_head)
        #     else:
        #         result.appendleft(close_to_tail)
        #         tail = close_to_tail
        #         covered.add(close_to_tail)
        #         result_n.append(distance_from_tail)
        #     remaining = {x for x in distances.keys()} - covered
        #     print(f"{head=}, {tail=}, {covered=}, {remaining=}, {result=}")
        # print(f"{result=}")
        # print(f"{result_n=}")
        # 266 high
        # 206 low
        return min(result_n)

    def _calculate_2(self):
        return 0
        x = self.__input_data
        print(f"{x=}")
        return 0
