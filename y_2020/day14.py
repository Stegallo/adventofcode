from .common import AoCDay
import copy


class Day(AoCDay):
    def __init__(self):
        super().__init__(14)

    def _preprocess_input(self):
        # print(f"{self._input_data}")
        self.__input = [i for i in self._input_data]
        # print(f"{self.__input}")
        self.__memory = {}

    def _calculate_1(self):
        # info(self._input_data)
        print("here")
        # breakpoint()
        print(f"{self.__input}")
        instr = {}
        instr["instr"] = []
        instr["new"] = []
        for i in self.__input:
            # print(f"{i.split(' ')=}")
            x = i.split(" ")
            if x[0] == "mask":
                temp_mask = x[2]
            else:
                # breakpoint()
                instr["instr"].append((x[0][4:-1], int(x[2]), temp_mask))

        len_mask = len(instr["instr"][0][2])
        for i in instr["instr"]:
            binary_rep = "{0:b}".format(i[1])
            # print(binary_rep)
            transformed = []
            print(f"{instr=}")
            for j in range(len_mask):
                # print(binary_rep[len(binary_rep) - j - 1])
                # print(f"{instr['mask']=}")
                # print(f"{instr['mask'][len(instr['mask']) - j - 1]=}")
                if i[2][len_mask - j - 1] == "X":
                    # print(f"{len(binary_rep)=}, {len(instr['mask'])=}, {j=}")
                    if j <= len(binary_rep) - 1:
                        transformed.append(binary_rep[len(binary_rep) - j - 1])
                    else:
                        transformed.append("0")
                elif i[2][len_mask - j - 1] == "1":
                    transformed.append("1")
                elif i[2][len_mask - j - 1] == "0":
                    transformed.append("0")
            # print(f"{transformed=}")
            transformed.reverse()
            instr["new"].append(int("".join(transformed), 2))
            # print(("".join(transformed)))
            # print(int("".join(transformed), 2))
        print(instr)
        for c, i in enumerate(instr["new"]):
            print(f"{i=}")
            print(f"{instr['instr'][c][0]=}")
            self.__memory[instr["instr"][c][0]] = i
        print(self.__memory)
        res = 0
        for k, i in self.__memory.items():
            res = res + i
        # temp = [i for i in self._input_data.split(",")]
        # print(temp)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        self.__input
        return res

    def _calculate_2(self):
        self.__memory = {}
        instr = {}
        instr["instr"] = []
        instr["new"] = []
        for i in self.__input:
            # print(f"{i.split(' ')=}")
            x = i.split(" ")
            if x[0] == "mask":
                temp_mask = x[2]
            else:
                instr["instr"].append((x[0][4:-1], int(x[2]), temp_mask))

        print(f"{instr=}")
        len_mask = len(instr["instr"][0][2])
        for i in instr["instr"]:
            # print(f"{i=}")
            # breakpoint()
            binary_rep = "{0:b}".format(int(i[0]))
            # print(f"{binary_rep=}")
            transformed = []
            # print(f"{i=}")
            # continue
            for j in range(len_mask):
                # print(binary_rep[len(binary_rep) - j - 1])
                # print(f"{instr['mask']=}")
                # print(f"{instr['mask'][len(instr['mask']) - j - 1]=}")
                if i[2][len_mask - j - 1] == "0":
                    # print(f"{len(binary_rep)=}, {len(instr['mask'])=}, {j=}")
                    if j <= len(binary_rep) - 1:
                        transformed.append(binary_rep[len(binary_rep) - j - 1])
                    else:
                        transformed.append("0")
                elif i[2][len_mask - j - 1] == "1":
                    transformed.append("1")
                elif i[2][len_mask - j - 1] == "X":
                    transformed.append("#")
            # print(f"{transformed=}")
            transformed.reverse()
            # instr["new"].append(int("".join(transformed), 2))
            instr["new"].append(("".join(transformed)))
            # print(("".join(transformed)))
            # print(int("".join(transformed), 2))
        print(instr)
        mem_cells = []
        for i in instr["new"]:
            out = []
            out.append([])
            # print(f"{i=}")
            for j in i:
                # print(f"{j=}, {i=}, {out=}")
                if j == "0":
                    # do nothing
                    for k in out:
                        k.append("0")
                    # print(f"{out[-1]=}")
                elif j == "1":
                    # do nothing
                    for k in out:
                        k.append("1")
                    # print(f"{out[-1]=}")
                elif j == "#":
                    # generate
                    temp = copy.deepcopy(out)
                    # print(f"{temp=}")
                    # print(f"{out=}")
                    out.extend(temp)
                    # print(f"{out=}")
                    # breakpoint()

                    for c, k in enumerate(out):
                        # print(f"{out=}{k=}")
                        if c < len(out) / 2:
                            k.append("0")
                        else:
                            k.append("1")
                # print(f"{out=}")
            memories = []
            for o in out:
                print("".join(o))
                memories.append(int("".join(o), 2))
            mem_cells.append(memories)

        print(instr)
        print(mem_cells)

        for c, i in enumerate(instr["instr"]):
            # print(i)
            # print(mem_cells[c])
            for j in mem_cells[c]:
                self.__memory[j] = i[1]
        print(f"{self.__memory=}")

        res = 0
        for k, i in self.__memory.items():
            res = res + i

        return res

        return
        for c, i in enumerate(instr["new"]):
            print(f"{i=}")
            print(f"{instr['instr'][c][0]=}")
            self.__memory[instr["instr"][c][0]] = i
        print(self.__memory)
        res = 0
        for k, i in self.__memory.items():
            res = res + i
        # temp = [i for i in self._input_data.split(",")]
        # print(temp)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        self.__input
        return res
