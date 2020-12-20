from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(16)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def _calculate_1(self):
        # info(self._input_data)
        # return 0
        rules = {}
        # yours = []
        others = []
        rules_flag = True
        # your = False
        other = False
        for i in self.__input:
            # print(i)
            if i == "":
                rules_flag = False
            if i == "your ticket:":
                # your = True
                continue
            if i == "nearby tickets:":
                other = True
                continue
            if rules_flag:
                # print(i)
                # print(i[: i.index(":")])
                # print(i[i.index(":") + 2 :].split(" or "))
                rules[i[: i.index(":")]] = i[i.index(":") + 2 :].split(" or ")
            # if your:
            #     # print(i.split())
            #     yours = i.split(",")
            if other:
                others.append(i.split(","))

        print(rules)
        # print(yours)
        # print(others)
        result = 0
        for i in others:
            # print(i)
            for j in i:
                valid = False
                # print(j)
                for k, v in rules.items():
                    # print(f"{k=}, {v=}, {j=}")
                    for c in range(2):
                        a = int(v[c].split("-")[0])
                        b = int(v[c].split("-")[1])
                        # print(f"{j=},{a=},{b=},{a <= int(j) <= b=}")
                        if a <= int(j) <= b:
                            valid = True
                if not valid:
                    print(f"not valid: {j=}")
                    result += int(j)
        return result

    def _calculate_2(self):
        # info(self._input_data)
        rules = {}
        yours = []
        others = []
        rules_flag = True
        your = False
        other = False
        for i in self.__input:
            # print(i)
            if i == "":
                rules_flag = False
            if i == "your ticket:":
                your = True
                continue
            if i == "nearby tickets:":
                other = True
                continue
            if rules_flag:
                # print(i)
                # print(i[: i.index(":")])
                # print(i[i.index(":") + 2 :].split(" or "))
                rules[i[: i.index(":")]] = i[i.index(":") + 2 :].split(" or ")
            if your:
                # print(i.split())
                yours = i.split(",")
                your = False
            if other:
                others.append(i.split(","))

        print(rules)
        # discard invalid
        print(f"{len(others)=}")
        valid_others = [i for i in others if is_valid(i, rules)]
        print(f"{len(valid_others)=}")
        for k in rules:
            print(f"{k=}")
        locations = []
        for p in valid_others[0]:
            locations.append([r for r in rules])
        # print(f"{locations=}")
        for i in valid_others:
            # print(i)
            for p, j in enumerate(i):
                canbe = []
                # print(j)
                for k, v in rules.items():
                    # print(f"{k=}, {v=}, {j=}")
                    for c in range(2):
                        a = int(v[c].split("-")[0])
                        b = int(v[c].split("-")[1])
                        # print(f"{j=},{a=},{b=},{a <= int(j) <= b=}")
                        if a <= int(j) <= b:
                            canbe.append(k)
                            # print("cista")
                            # valid = True
                # print(f"{canbe=} in position {p}\n")
                new_poss_loc = []
                for l in locations[p]:
                    # print(l)
                    if l not in canbe:
                        ...
                        # print(f"remove {l}")
                    else:
                        new_poss_loc.append(l)
                locations[p] = new_poss_loc
                # print(f"{locations[p]=}")
        # print("\n\n")
        print(f"{locations=}")
        iters = 0
        while iters < 100:
            for ci, i in enumerate(locations):
                # print(f"{i=}, {len(i)=}, {ci=}")
                if len(i) == 1:
                    # print(i)
                    for cj, j in enumerate(locations):
                        if ci == cj:
                            continue
                        # print(j)
                        x = []
                        for k in j:
                            # print(f"{k=}, {i[0]=}")
                            if i[0] == k:
                                ...
                            else:
                                x.append(k)
                            #
                        # print(f"{x=}")
                        locations[cj] = x
            iters += 1
        print(f"{locations=}")

        print(f"{len(locations)=}")
        print(f"{len(yours)=}")

        print(f"{yours=}")
        result = 1
        for c, i in enumerate(locations):
            print(f"{i=}, {c=}")
            if "departure" in i[0]:
                print(yours[c])
                result *= int(yours[c])
        return result


def is_valid(i, rules):
    for j in i:
        valid = False
        # print(j)
        for k, v in rules.items():
            # print(f"{k=}, {v=}, {j=}")
            for c in range(2):
                a = int(v[c].split("-")[0])
                b = int(v[c].split("-")[1])
                # print(f"{j=},{a=},{b=},{a <= int(j) <= b=}")
                if a <= int(j) <= b:
                    valid = True
        if not valid:
            return False
    return valid
