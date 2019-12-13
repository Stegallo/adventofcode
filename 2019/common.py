import copy


def add(*args, **kwargs):
    L, c, im = args[:3]
    p1 = c + 1 if im[0] else L[c + 1]
    p2 = c + 2 if im[1] else L[c + 2]
    p3 = L[c + 3]
    res = L[p1] + L[p2]
    L[p3] = res
    return 4


def mult(*args, **kwargs):
    L, c, im = args[:3]
    p1 = c + 1 if im[0] else L[c + 1]
    p2 = c + 2 if im[1] else L[c + 2]
    p3 = L[c + 3]
    res = L[p1] * L[p2]
    L[p3] = res
    return 4


def term(*args, **kwargs):
    return -1


def inp(*args, **kwargs):
    L, c, im, inpu = args[:4]
    p1 = L[c + 1]
    if not inpu:
        return -2
    input_val = int(inpu[0])
    inpu.pop(0)
    L[p1] = input_val
    return 2


def out(*args, **kwargs):
    L, c, im, _, out = args[:5]
    p1 = c + 1 if im[0] else L[c + 1]
    out.append(L[p1])
    return 2


def jit(*args, **kwargs):
    L, c, im = args[:3]
    p1 = L[c + 1]
    p2 = L[c + 2]
    ev = p1 if im[0] else L[p1]
    dest = p2 if im[1] else L[p2]
    if ev == 0:
        return 3
    return dest - c


def jif(*args, **kwargs):
    L, c, im = args[:3]
    p1 = L[c + 1]
    p2 = L[c + 2]
    ev = p1 if im[0] else L[p1]
    dest = p2 if im[1] else L[p2]
    if ev != 0:
        return 3
    return dest - c


def let(*args, **kwargs):
    L, c, im = args[:3]
    p1 = c + 1 if im[0] else L[c + 1]
    p2 = c + 2 if im[1] else L[c + 2]
    p3 = L[c + 3]
    result = 0
    if L[p1] < L[p2]:
        result = 1
    L[p3] = result
    return 4


def equ(*args, **kwargs):
    L, c, im = args[:3]
    p1 = L[c + 1]
    p2 = L[c + 2]
    p3 = L[c + 3]
    c1 = p1 if im[0] else L[p1]
    c2 = p2 if im[1] else L[p2]
    c3 = p3 if im[2] else L[p3]
    result = 0
    if c1 == c2:
        result = 1
    L[p3] = result
    return 4


OPS = {1: add, 2: mult, 3: inp, 4: out, 5: jit, 6: jif, 7: let, 8: equ, 99: term}


class Operator(object):
    """docstring for Operator."""

    def __init__(self, code, c, inp=None, out=None):
        self.__code = code
        self.__c = c
        self.__im = [0, 0, 0]
        t_op = code[0 + c]
        self.__command = int(str(t_op)[-2:])
        modes = str(t_op)[0:-2]

        for i, j in enumerate(reversed(range(len(modes)))):
            self.__im[i] = int(modes[j])
        self.__inp = inp
        self.__out = out

    def run(self):
        return OPS[self.__command](
            self.__code, self.__c, self.__im, self.__inp, self.__out
        )


class Computer(object):
    """docstring for Computer."""

    def __init__(self, name, code, input=None):
        self.__name = name  # name of the executor (just a label)
        self.__code = copy.deepcopy(code)  # the actual code. A copy of the list
        self.__c = 0  # position of execution. Starts at 0
        self.__input = input  # list of input values
        self.__output = []  # list of output values

    def run(self):
        halt = False
        while not halt:
            op = Operator(self.__code, self.__c, self.__input, self.__output)
            r = op.run()
            if r == -1:
                halt = True
                output = copy.deepcopy(self.__output)
                return output, 0
            if r == -2:
                halt = True
                output = copy.deepcopy(self.__output)
                self.__output = []
                return output, 0
            # if r == -3:
            #     self.__c = self.__c + 2
            #     output = copy.deepcopy(self.__output)
            #     self.__output = []
            #     print(output)
            #     # return output, 0
            self.__c = self.__c + r

    def get_code(self):
        return self.__code


def run_get_code(program, name=None, input=None):
    c = Computer(name, program, input)
    c.run()
    return c.get_code()


def run_get_output(program, name=None, input=None):
    c = Computer(name, program, input)
    if w := c.run():
        return w[0]
