import copy


def add(L, c, im, inp, out):
    global L
    p1 = c + 1 if im[0] else L[c + 1]
    p2 = c + 2 if im[1] else L[c + 2]
    p3 = L[c + 3]
    res = L[p1] + L[p2]
    L[p3] = res
    return 4


def mult(L, c, im, inp, out):
    global L
    p1 = c + 1 if im[0] else L[c + 1]
    p2 = c + 2 if im[1] else L[c + 2]
    p3 = L[c + 3]
    res = L[p1] * L[p2]
    L[p3] = res
    return 4
def term(c, im, inp, out):
    print("term")
    return -1

OPS = {1: add, 2: mult, 99: term}
class Operator(object):
    """docstring for Operator."""

    def __init__(self, code, c, inp, out):
        self.__code = code
        self.__c = c
        # self.__im = [0, 0, 0]
        t_op = code[0 + c]
        self.__command = int(str(t_op)[-2:])
        # modes = str(t_op)[0:-2]
        #
        # for i, j in enumerate(reversed(range(len(modes)))):
        #     self.__im[i] = int(modes[j])
        # self.__inp = inp
        # self.__out = out

    def run(self):
        return OPS[self.__command](self.__code, self.__c)
        # , self.__im, self.__inp, self.__out)


class Computer(object):
    """docstring for Computer."""

    def __init__(self, name, code, input=None):
        self.__name = name  # name of the executor (just a label)
        self.__code = copy.deepcopy(code)  # the actual code. A copy of the list
        self.__c = 0  # position of execution. Starts at 0
        # self.__input = input  # list of input values
        # self.__output = []  # list of output values

    def run(self):
        halt = False
        while not halt:
            # print(f"{self.__c=}, {self.__name=}")
            # print(f"{self.__output=}")
            # print(f"{self.__code=}")
            # print(L )
            op = Operator(self.__code, self.__c, self.__input, self.__output)
            r = op.run()
            if r == -1:
                halt = True
                # return self.__output, 1
            # if r == -2:
            #     halt = True
            #     output = copy.deepcopy(self.__output)
            #     self.__output = []
            #     return output, 0
            # if r == -3:
            #     self.__c = self.__c + 2
            #     output = copy.deepcopy(self.__output)
            #     self.__output = []
            #     return output, 0
            self.__c = self.__c + r

    def get_code(self):
        return self.__code
#
# def run_get_output(program, name=None, input=None):
#     c = Computer(name, program, input)
#     return c.run()
#
#
# def run_get_code(program, name=None, input=None):
#     print(input)
#     c = Computer(name, program, input)
#     c.run()
#     return c.get_code()
