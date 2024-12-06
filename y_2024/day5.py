from typing import Optional

from pydantic.dataclasses import dataclass
from collections import defaultdict
from common.aoc import AoCDay


@dataclass
class Row:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = ""  # self.original

@dataclass
class Rule:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = self.original.split('|')

@dataclass
class Update:
    original: str
    processed: Optional[str] = None

    def __post_init__(self) -> None:
        self.processed = self.original.split(',')

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        # print(f"{len(self._input_data[0])=}")
        self.__input_data_1 = [Rule(i) for i in self._input_data[0]]
        self.__input_data_2 = [Update(i) for i in self._input_data[1]]

    def _calculate_1(self):
        result = 0
        return result
        foll=defaultdict(list)
        prec=defaultdict(list)
        for x in self.__input_data_1:
            foll[x.processed[0]].append(x.processed[1])
            prec[x.processed[1]].append(x.processed[0])


        # print(foll)
        # print(prec)
        self.valids = []
        for x in self.__input_data_2:

            valid = True
            for c,i in enumerate(x.processed):
                for d,j in enumerate(x.processed[c+1:]):
                    # print(i,j)
                    if not j in foll[i]:
                        valid = False
            if valid:
                # print(f"{x.processed}, {len(x.processed)//2=}")
                result+=int(x.processed[len(x.processed)//2])
                self.valids.append(x.processed)

        return result

    def _calculate_2(self):
        # print(self.valids)
        # return 0
        result = 0
        foll=defaultdict(list)
        orfoll=defaultdict(list)
        fixed = []
        prec=defaultdict(list)
        for x in self.__input_data_1:
            foll[x.processed[0]].append(x.processed[1])
            orfoll[x.processed[0]].append(x.processed[1])
            # prec[x.processed[1]].append(x.processed[0])
        print(foll)

        # for k,v in prec.foll():
        #     print(k, len(v))
        # return
        # first = True
        # while True:
        #
        #     if len(foll.keys())<1:
        #         break
        #     for i in foll.keys():
        #         #
        #         if len(foll[i])==1:
        #             if first:
        #                 fixed.append(foll[i][0])
        #                 first = False
        #             fixed.append(i)
        #             del foll[i]
        #             for k, v in foll.items():
        #                 new_val = [k for k in v if k!=i]
        #                 foll[k]= new_val
        #             break
        #
        # fixed = fixed[::-1]
        # fixed = {i: c for c,i in enumerate(fixed)}
        # print(fixed)



        # return 0
        for x in self.__input_data_2:

            valid = True
            for c,i in enumerate(x.processed):
                for d,j in enumerate(x.processed[c+1:]):
                    # print(i,j)
                    if not j in orfoll[i]:
                        valid = False
            if valid:
                # print(f"{x.processed}, {len(x.processed)//2=}")
                pass
                # result+=int(x.processed[len(x.processed)//2])
            else:
                # breakpoint()
                proposed = list(x.processed)
                valid_p = False
                while not valid_p:
                    ordered = True
                    # print(proposed)
                    for i in range(len(proposed)-1):
                        j = i+1
                        # print(proposed, i, j)
                        if not proposed[j] in foll[proposed[i]]:
                            ordered = False
                            proposed[j], proposed[i] = proposed[i], proposed[j]
                    if ordered:
                        valid_p = True
                        break
                # print(proposed)
                # n = {i:fixed[i] for i in x.processed}
                # # print(n)
                # sort_n = list(dict(sorted(n.items(), key=lambda item: item[1])).keys())
                # print(sort_n)

                result+=int(proposed[len(proposed)//2])

        return result
