from .common import AoCDay
import copy


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = [i for i in self._input_data]
        print(f"len of input = {len(self.__input_data)}")
        try:
            print(f"first value = {self.__input_data[0]}")
            print(f"mid value = {self.__input_data[len(self.__input_data)//2]}")
            print(f"last value = {self.__input_data[-1]}")
        except:
            ...

    def __pivot(self, x):
        p = []
        for c, v in enumerate(x):
            for d, u in enumerate(v):
                if len(p) <= d:
                    p.append([])
                p[d].append(u)
        # print(p)
        return p

    def _calculate_1(self):
        x = self.__input_data
        # p = []
        # for c, v in enumerate(x):
        #     for d, u in enumerate(v):
        #         if len(p) <= d:
        #             p.append([])
        #         p[d].append(u)
        # # print(p)
        # p = self.pivot()
        # r = []
        # for i in p:
        #     print(len(i))
        #     if sum([int(j) for j in i]) > 500:
        #         print(1)
        #         r.append(1)
        #     else:
        #         print(0)
        #         r.append(0)
        # print(r)
        # print([1 - i for i in r])
        result = 0

        #
        # [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1]
        # [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
        #
        # 001100100101
        #
        # 805
        #
        # 110011011010
        #
        # 3290
        # 2648450
        return result

    def __inner_ox(self, x, p, incr):
        result = []
        # print(p)
        for c, i in enumerate(p):
            v = "1"
            print(f"{len(i)=}")
            # print(sum([int(j) for j in i]))
            # print(sum([1 - int(j) for j in i]))
            if sum([int(j) for j in i]) < sum([1 - int(j) for j in i]):
                v = "0"
            if c >= incr:
                break
            # print(f"{v=}")

        for i in x:
            if i[incr] == v:
                result.append(i)
        return result

    def __inner_sc(self, x, p, incr):
        result = []
        for c, i in enumerate(p):
            v = "0"
            print(f"{len(i)=}")
            # print(sum([int(j) for j in i]))
            # print(sum([1 - int(j) for j in i]))
            if sum([int(j) for j in i]) < sum([1 - int(j) for j in i]):
                v = "1"
            if c >= incr:
                break

        for i in x:
            if i[incr] == v:
                result.append(i)
        return result

    def _calculate_2(self):
        x = self.__input_data
        y = self.__input_data
        # p = self.__pivot(x)
        # print(*p, sep="\n")
        incr = 0
        while len(x) > 1:
            print(f"{len(x)=}")
            x = self.__inner_ox(x, self.__pivot(x), incr)

            incr += 1
            print(f"{incr=}")
        print(x)

        incr = 0
        while len(y) > 1:
            print(f"{len(y)=}")
            y = self.__inner_sc(y, self.__pivot(y), incr)
            incr += 1
            print(f"{incr=}")
        print(y)
        return 841 * 3384

        # 001101001001
        # 841

        # 110100111000
        # 3384
