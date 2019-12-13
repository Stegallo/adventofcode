import copy


def add(*args, **kwargs):
    L, c = args
    p1 = L[c + 1]
    p2 = L[c + 2]
    p3 = L[c + 3]
    res = L[p1] + L[p2]
    L[p3] = res
    return 4


def mult(*args, **kwargs):
    L, c = args
    p1 = L[c + 1]
    p2 = L[c + 2]
    p3 = L[c + 3]
    res = L[p1] * L[p2]
    L[p3] = res
    return 4


def term(*args, **kwargs):
    return -1


OPS = {1: add, 2: mult, 99: term}


class Operator(object):
    """docstring for Operator."""

    def __init__(self, code, c):
        self.__code = code
        self.__c = c
        t_op = code[0 + c]
        self.__command = int(str(t_op)[-2:])

    def run(self):
        return OPS[self.__command](self.__code, self.__c)


class Computer(object):
    """docstring for Computer."""

    def __init__(self, name, code):
        self.__name = name  # name of the executor (just a label)
        self.__code = copy.deepcopy(code)  # the actual code. A copy of the list
        self.__c = 0  # position of execution. Starts at 0

    def run(self):
        halt = False
        while not halt:
            op = Operator(self.__code, self.__c)
            r = op.run()
            if r == -1:
                halt = True
            self.__c = self.__c + r

    def get_code(self):
        return self.__code


def run_get_code(program, name=None):
    c = Computer(name, program)
    c.run()
    return c.get_code()
