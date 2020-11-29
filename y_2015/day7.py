import re


def parse(i):
    x = i[: re.search(" ->", i).start()]
    if "AND" in x:
        first = x[: re.search(" AND", x).start()]
        second = x[re.search(" AND", x).start() + 5 :]

        return [i[re.search(" ->", i).start() + 4 :], "AND", first, second]

    if "OR" in x:
        first = x[: re.search(" OR", x).start()]
        second = x[re.search(" OR", x).start() + 4 :]

        return [i[re.search(" ->", i).start() + 4 :], "OR", first, second]

    if "LSHIFT" in x:
        first = x[: re.search(" LSHIFT", x).start()]
        second = x[re.search(" LSHIFT", x).start() + 8 :]

        return [i[re.search(" ->", i).start() + 4 :], "LSHIFT", first, second]

    if "RSHIFT" in x:
        first = x[: re.search(" RSHIFT", x).start()]
        second = x[re.search(" RSHIFT", x).start() + 8 :]

        return [i[re.search(" ->", i).start() + 4 :], "RSHIFT", first, second]

    if "NOT" in x:
        return [
            i[re.search(" ->", i).start() + 4 :],
            "NOT",
            x[re.search("NOT", x).start() + 4 :],
        ]

    return [i[re.search(" ->", i).start() + 4 :], i[: re.search(" ->", i).start()]]


def evaluate(i):

    solved = False
    while not solved:
        no_evaluated = True
        for j in i:
            if len(i[j]) > 1:
                no_evaluated = False

                if i[j][0] == "AND":
                    try:
                        i[j] = [int(i[i[j][1]][0]) & int(i[i[j][2]][0])]
                    except ValueError:
                        pass
                    except KeyError:
                        first = None
                        second = None
                        try:
                            first = int(i[j][1])
                        except ValueError:
                            pass
                        try:
                            second = int(i[j][2])
                        except ValueError:
                            pass
                        try:
                            i[j] = [
                                (first or int(i[i[j][1]][0]))
                                & (second or int(i[i[j][2]][0]))
                            ]
                        except ValueError:
                            pass

                if i[j][0] == "OR":
                    try:
                        i[j] = [int(i[i[j][1]][0]) | int(i[i[j][2]][0])]
                    except ValueError:
                        pass
                    except KeyError:
                        first = None
                        second = None
                        try:
                            first = int(i[j][1])
                        except ValueError:
                            pass
                        try:
                            second = int(i[j][2])
                        except ValueError:
                            pass
                        try:
                            i[j] = [
                                (first or int(i[i[j][1]][0]))
                                | (second or int(i[i[j][2]][0]))
                            ]
                        except ValueError:
                            pass

                if i[j][0] == "LSHIFT":
                    try:
                        i[j] = [int(i[i[j][1]][0]) << int(i[j][2])]
                    except ValueError:
                        pass
                    except KeyError:
                        first = None
                        second = None
                        try:
                            first = int(i[j][1])
                        except ValueError:
                            pass
                        try:
                            second = int(i[j][2])
                        except ValueError:
                            pass
                        try:
                            i[j] = [
                                (first or int(i[i[j][1]][0]))
                                << (second or int(i[i[j][2]][0]))
                            ]
                        except ValueError:
                            pass

                if i[j][0] == "RSHIFT":
                    try:
                        i[j] = [int(i[i[j][1]][0]) >> int(i[j][2])]
                    except ValueError:
                        pass
                    except KeyError:
                        first = None
                        second = None
                        try:
                            first = int(i[j][1])
                        except ValueError:
                            pass
                        try:
                            second = int(i[j][2])
                        except ValueError:
                            pass
                        try:
                            i[j] = [
                                (first or int(i[i[j][1]][0]))
                                >> (second or int(i[i[j][2]][0]))
                            ]
                        except ValueError:
                            pass

                if i[j][0] == "NOT":
                    try:
                        i[j] = [int(i[i[j][1]][0]) ^ 65535]
                    except ValueError:
                        pass
                    except KeyError:
                        first = None
                        try:
                            first = int(i[j][1])
                        except ValueError:
                            pass
                        try:
                            i[j] = [(first or int(i[i[j][1]][0])) ^ 65535]
                        except ValueError:
                            pass

            else:
                try:
                    i[j] = [int(i[j][0])]
                except ValueError:
                    pass
        if no_evaluated:
            solved = True
    print(i)
    return {k: int(v[0]) for k, v in i.items()}


def inner_1(lista):
    result = {}
    parsedl = [parse(i) for i in lista]
    for i in parsedl:
        result[i[0]] = i[1:]
    result = evaluate(result)
    return result


def calculate_1(x: list) -> int:
    result = inner_1(x)
    return result["a"]


def inner_2(lista):
    result = {}
    parsedl = [parse(i) for i in lista]
    for i in parsedl:
        result[i[0]] = i[1:]
    result["b"] = ["46065"]
    result = evaluate(result)
    return result


def calculate_2(x: str) -> int:
    result = inner_2(x)
    return result["a"]
