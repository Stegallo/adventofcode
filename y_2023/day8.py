from common.aoc import AoCDay
from math import gcd


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)
        self.index = None

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = self._input_data

    def next(self):
        self.index = (self.index+1)%(len(self.__input_data[0][0]))
        # print(f"{self.index=}, {len(self.__input_data[0][0])}")
        return self.__input_data[0][0][self.index]

    def _calculate_1(self):
        return 0
        self.index = -1
        LR = self.__input_data[0]
        inp = self.__input_data[1]
        arr = {}
        for x in inp:
            source = x.split(' = ')[0]
            # print(f"{x.split(' = ')[1].split(', ')}")
            dest_l = x.split(' = ')[1].split(', ')[0].replace('(','')
            dest_r = x.split(' = ')[1].split(', ')[1].replace(')','')
            print(f"{dest_l},{dest_r}")
            arr[source] = (dest_l, dest_r)
        print(arr)
        current = 'AAA'
        c=0
        while current != 'ZZZ':
            action = self.next()
            # breakpoint()
            if action == 'L':
                current = arr[current][0]
            else:
                current = arr[current][1]
            c+=1

        return c

    def _calculate_2(self):

        LR = self.__input_data[0]
        inp = self.__input_data[1]
        arr = {}
        for x in inp:
            source = x.split(' = ')[0]
            # print(f"{x.split(' = ')[1].split(', ')}")
            dest_l = x.split(' = ')[1].split(', ')[0].replace('(','')
            dest_r = x.split(' = ')[1].split(', ')[1].replace(')','')
            # print(f"{dest_l},{dest_r}")
            arr[source] = (dest_l, dest_r)
        # print(arr)
        currents = []
        for i in arr:
            if i[-1]=='A':
                currents.append(i)
        print(currents)

        results = []
        self.index = -1
        for current in currents:
            c=0
            while current[-1] != 'Z':
                action = self.next()
                # breakpoint()
                if action == 'L':
                    current = arr[current][0]
                else:
                    current = arr[current][1]
                c+=1
            results.append(c)
        print(results)
        # c=0
        # ends = [i[-1] for i in currents]
        # print(ends)
        # while set(ends) != set('Z'):
        #     action = self.next()
        #     # breakpoint()
        #     if action == 'L':
        #         currents = [arr[c][0] for c in currents]
        #     else:
        #         currents = [arr[c][1] for c in currents]
        #     ends = [i[-1] for i in currents]
        #     c+=1
        # a = [100, 200, 150]   #will work for an int array of any length
        lcm = 1
        for i in results:
            lcm = lcm*i//gcd(lcm, i)
        print(lcm)
        return lcm
        x = self.__input_data
        print(f"{x=}")
