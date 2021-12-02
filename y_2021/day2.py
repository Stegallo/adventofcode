from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(2)

    def _preprocess_input(self):
        self.__input_data = [i for i in self._input_data]

    def _calculate_1(self):
        x = self.__input_data
        o = 0
        d = 0
        for i in x:
            com = i.split(" ")
            if com[0] == "forward":
                o = o + int(com[1])
            if com[0] == "down":
                d = d + int(com[1])
            if com[0] == "up":
                d = d - int(com[1])

        return d * o

    def _calculate_2(self):
        x = self.__input_data
        o = 0
        d = 0
        a = 0
        for i in x:
            com = i.split(" ")
            if com[0] == "forward":
                o = o + int(com[1])
                d = d + a * int(com[1])
            if com[0] == "down":
                a = a + int(com[1])
            if com[0] == "up":
                a = a - int(com[1])

        return d * o
