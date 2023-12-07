from common.aoc import AoCDay
from collections import defaultdict

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        result = 0
        simbols={}
        for c, x in enumerate(self.__input_data):
        #     print(f"{x=}")
            # print(f"{x.split('.')=}")
            for d, y in enumerate(x):
                if y != '.' and not y.isnumeric():
                    simbols[(c,d)] = y
        # print(simbols)
        for c, x in enumerate(self.__input_data):
            splits = x.split('.')
            numbers = []
            for i in splits:
                if i.isnumeric():
                    numbers.append(i)
                elif i[:-1].isnumeric():
                        numbers.append(i[:-1])
                elif i[1:].isnumeric():
                        numbers.append(i[1:])
                elif len(i)>1:
                    # print(i)
                    j = i.split('*')
                    numbers.extend(j)
                    # 1/0
            # print(f'{numbers=}')
            # continue
            num_ind = 0
            start = 0
            end = 0
            while x:
                # print(x, x[0], numbers, num_ind, start, end)
                if num_ind>=len(numbers):
                    break
                if x[0]=='.' or not x[0].isnumeric():
                    x=x[1:]
                    start += 1
                if x.startswith(str(numbers[num_ind])):
                    end = start+ len(str(numbers[num_ind]))-1
                    # print(numbers[num_ind], start, end)
                    for k in range(c-1, c+2):
                        for l in range(start-1, end +2):
                            # print((k,l), simbols.get((k,l)))
                            if simbols.get((k,l)):
                                # print(int(numbers[num_ind]))
                                result+=int(numbers[num_ind])
                    start = end+1
                    x=x[len(str(numbers[num_ind])):]
                    num_ind += 1

                # break

        return result

    def _calculate_2(self):
        result = 0
        simbols={}
        new_simbols=defaultdict(list)
        for c, x in enumerate(self.__input_data):
        #     print(f"{x=}")
            # print(f"{x.split('.')=}")
            for d, y in enumerate(x):
                if y != '.' and not y.isnumeric():
                    simbols[(c,d)] = (y,[])
        # print(simbols)
        for c, x in enumerate(self.__input_data):
            splits = x.split('.')
            numbers = []
            for i in splits:
                if i.isnumeric():
                    numbers.append(i)
                elif i[:-1].isnumeric():
                        numbers.append(i[:-1])
                elif i[1:].isnumeric():
                        numbers.append(i[1:])
                elif len(i)>1:
                    # print(i)
                    j = i.split('*')
                    numbers.extend(j)
                    # 1/0
            # print(f'{numbers=}')
            # continue
            num_ind = 0
            start = 0
            end = 0
            while x:
                # print(x, x[0], numbers, num_ind, start, end)
                if num_ind>=len(numbers):
                    break
                if x[0]=='.' or not x[0].isnumeric():
                    x=x[1:]
                    start += 1
                if x.startswith(str(numbers[num_ind])):
                    end = start+ len(str(numbers[num_ind]))-1
                    # print(numbers[num_ind], start, end)
                    for k in range(c-1, c+2):
                        for l in range(start-1, end +2):
                            # print((k,l), simbols.get((k,l)))
                            if simbols.get((k,l)):
                                # print(int(numbers[num_ind]))
                                # result+=int(numbers[num_ind])
                                new_simbols[k,l].append(int(numbers[num_ind]))
                    start = end+1
                    x=x[len(str(numbers[num_ind])):]
                    num_ind += 1

                # break
        print(new_simbols)
        for i in simbols:
            if simbols[i][0] == '*' and len(new_simbols[i])==2:
                print(simbols[i])
                print(new_simbols[i])
                print( new_simbols[i][0]*new_simbols[i][1] )
                result+=new_simbols[i][0]*new_simbols[i][1]

        return result
