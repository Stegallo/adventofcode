def prod(x):
    c = 1
    for i in x:
        c *= i
    return c


def collapse_strings(x: list):
    p_list = [[]]
    for i in x:
        p = p_list[-1]
        if len(i) != 0:
            p.append(i)
        else:
            p_list.append([])
    return [" ".join(i) for i in p_list]


def dict_from_string(x: str) -> dict:
    el_list = x.split(":")
    return {el_list[0]: el_list[1]}
