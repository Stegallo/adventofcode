from typing import Optional, List

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay


# OPS = ['>':>, '<':<]

# @dataclass
# class Rule:
#     var: str
#     cond: str
#     dest: str
@dataclass
class Row:
    original: str
    name: Optional[str] = None
    processed: List[str] = None

    def __post_init__(self) -> None:
        self.name = self.original.split('{')[0]
        # self.processed = [(lambda x: Rule(x[0],x[1:]) ) (i) for i in self.original.replace('}', '').split('{')[1].split(',')]
        self.processed = [i for i in self.original.replace('}', '').split('{')[1].split(',')]

@dataclass
class Rating:
    name:str
    rate:int

@dataclass
class Row2:
    original: str
    processed: List[Rating] = None

    def __post_init__(self) -> None:
        self.processed = [Rating(*i.split('=')) for i in self.original.replace('{', '').replace('}', '').split(',')]


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data1 = [Row(i) for i in self._input_data[0]]
        self.__input_data2 = [Row2(i) for i in self._input_data[1]]

    def _calculate_1(self):
        result = 0
        first = None
        rules = {}
        for x in self.__input_data1:
            # print(f"{x}, {x.original.replace('}', '').split('{')}")
            # if 'in' in x.original :
            #     # print(x.original)
            #     first = x
            rules[x.name] = x.processed
        # print(rules)
        # print(first)
        # print(rules['in'])
        for x in self.__input_data2:
            print(f"{x=}")
            # print(rules['in'])
            rule = rules['in']
            # print(rule)
            c=0
            while rule:
                # print(f"{rule=}")
                c+=1
                for j in rule:
                    tmp = j.split(':')
                    if len(tmp)>1:
                        cond, dest = tmp
                    else:
                        cond = None
                        dest = tmp[0]

                    var = cond[0] if cond else None
                    op = cond[1] if cond else None
                    value = int(cond[2:]) if cond else None
                    # print(f"{cond=},{var=},{op=},{value=} \t{dest=}, {x.processed=}")
                    if dest in ('A', 'R'):
                        final_rule = True
                    else:
                        final_rule = False
                    found = False
                    for k in x.processed:
                        if k.name == var:
                            if op == '<':
                                if k.rate < value:
                                    print(f"{k.rate} is {op} {value}")
                                    if final_rule:
                                        rule = None
                                    else:
                                        rule = rules[dest]
                                    found = True
                                    break
                        if k.name == var:
                            if op == '>':
                                if k.rate > value:
                                    print(f"{k.rate} is {op} {value}, go to {dest}")
                                    if final_rule:
                                        rule = None
                                    else:
                                        rule = rules[dest]
                                    found = True
                                    break
                    if found:
                        break

                    if not cond:
                        print(f"last rule, go to {dest}")
                        if final_rule:
                            rule = None
                        else:
                            rule = rules[dest]

                    #     if j.name == 's':
                    #         print(j)
                # if c>3:
                #     break
            # break
            print(dest)
            if dest=='A':
                result+=sum(i.rate for i in x.processed)
            ...
        return result

    def _calculate_2(self):
        return 0
