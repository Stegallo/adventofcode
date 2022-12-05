from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        self.__input_data = self._input_data

    def _calculate_1(self):
        start = self.__input_data[0]
        moves = self.__input_data[1]
        print(start[-1].split("   "))
        d = {}
        max_rack = 0
        for i in start[-1][1:].split("   "):
            d[int(i)] = []
            max_rack += 1
        for i in range(len(start) - 2, -1, -1):
            # print(i)
            # print(start[i])
            for j in range(max_rack):
                if container := start[i][j * 4 : (j + 1) * 4].strip():
                    d[j + 1].append(container)
                        # print(start[i][j*4:(j+1)*4])
        print(f"{d=}")
        for i in moves:
            # print(i.split(' '))
            (_, quantity, _, fro, _, to) = i.split(" ")
            print(quantity, fro, to)
            for _ in range(int(quantity)):
                # print(j)
                d[int(to)].append(d[int(fro)].pop())
        print(f"{d=}")
        r = [d[i + 1].pop().replace("[", "").replace("]", "") for i in range(max_rack)]
        print("".join(r))
        # print(f"{d=}")
        # start[:-1]:
        # print(i)

        # print(max_rack)
        # print(moves)
        return 0

    def _calculate_2(self):
        start = self.__input_data[0]
        moves = self.__input_data[1]
        print(start[-1].split("   "))
        d = {}
        max_rack = 0
        for i in start[-1][1:].split("   "):
            d[int(i)] = []
            max_rack += 1
        for i in range(len(start) - 2, -1, -1):
            # print(i)
            # print(start[i])
            for j in range(max_rack):
                if container := start[i][j * 4 : (j + 1) * 4].strip():
                    d[j + 1].append(container)
                        # print(start[i][j*4:(j+1)*4])
        print(f"{d=}")
        for i in moves:
            # print(i.split(' '))
            (_, quantity, _, fro, _, to) = i.split(" ")
            print(quantity, fro, to)
            t = []
            for _ in range(int(quantity)):
                # print(j)
                t.insert(0, d[int(fro)].pop())
            d[int(to)].extend(t)
                # break
        print(f"{d=}")
        # return
        r = [d[i + 1].pop().replace("[", "").replace("]", "") for i in range(max_rack)]
        print("".join(r))
        # print(f"{d=}")
        # start[:-1]:
        # print(i)

        # print(max_rack)
        # print(moves)
        return 0
