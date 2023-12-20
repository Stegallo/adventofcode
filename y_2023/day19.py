from typing import Optional, List

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from itertools import product

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

def process_branch(branch, branch_intervals):
    branch_valid_intervals = {}
    branch_else_intervals  = {}
    tmp = branch.split(':')
    print(tmp)
    if len(tmp)>1:
        cond, dest = tmp
    else:
        cond = None
        dest = tmp[0]

    var = cond[0] if cond else None
    op = cond[1] if cond else None
    value = int(cond[2:]) if cond else None

    # if dest in ('A', 'R'):
    #     final_rule = True
    #     if dest == 'A':
    #         return 1 #rule_intervals
    #     if dest == 'R':
    #         return 0
    print(op)
    if op == '<':
        x = [branch_intervals[var][0], value]
        branch_valid_intervals[var] = x
        y = [value, branch_intervals[var][1]]
        branch_else_intervals[var] = y
        # print(branch_valid_intervals)
        # print(branch_else_intervals)
        return (branch_valid_intervals, branch_else_intervals)
    if op == '>':
        x = [value, branch_intervals[var][1]]
        branch_valid_intervals[var] = x
        y = [branch_intervals[var][0], value]
        branch_else_intervals[var] = y
        return (branch_valid_intervals, branch_else_intervals)
        # y = [value-1, branch_intervals[var][1]]
        # branch_intervals[var] = x
        # branch_else_intervals[var] = y
        # branch_result = process_rule(dest, branch_intervals)
        # print(f"{branch_result=}")
    return
def process_rule(rule, rule_intervals, rules):
    print(f"{rule=}, {rule_intervals=}")
    if len(rule) <=1:
        if rule[0] == 'A':
            return rule_intervals
        if rule[0] == 'R':
            return None
    # breakpoint()
    rule_possible = {}
    else_possible = {}
    # branch_intervals = {}
    branch_else_intervals = {}
    for branch in rule:
        branch_intervals = {}
        # branch_else_intervals = {}
        print(f"{branch=}, {branch_intervals=}")
        rez = process_branch(branch, rule_intervals)
        print(f"{rez=}")
        if rez:
            branch_intervals = branch_intervals | rez[0]
            branch_else_intervals = branch_else_intervals | rez[1]

        print(f"{branch_intervals=}")
        print(f"{branch_else_intervals=}")
        tmp = branch.split(':')
        if len(tmp)>1:
            cond, dest = tmp
        else:
            cond = None
            dest = tmp[0]
        print(f"{dest=}")
        if not cond:
            print('in the else')
            # else_possible
            if dest == 'A':
                # acceptance
                else_possible = branch_else_intervals
            elif dest == 'R':
                # reject
                else_possible = {}
            else:
                # run rule dest
                ...
                print(f"qui qui qui {dest=}")
        if dest == 'A':
            # acceptance
            rule_possible = rule_possible | branch_intervals
        elif dest == 'R':
            # reject
            ... #rule_possible = rule_possible | else_possible
        else:
            # run rule dest
            ...
            print(f"{rules=}, {dest=}")
            print(f"{(rules[dest], branch_intervals, rules)=}")
            local_rezult = process_rule(rules[dest], branch_intervals, rules)
            if local_rezult:
                rule_possible = rule_possible | local_rezult

        print()
        continue
        branch_valid_intervals = []
        tmp = branch.split(':')
        if len(tmp)>1:
            cond, dest = tmp
        else:
            cond = None
            dest = tmp[0]

        var = cond[0] if cond else None
        op = cond[1] if cond else None
        value = int(cond[2:]) if cond else None

        if dest in ('A', 'R'):
            final_rule = True
            if dest == 'A':
                return rule_intervals
            if dest == 'R':
                return 0
        else:
            final_rule = False
        # print(f"{branch=},{var=},{op=},{value=} \t{dest=}, {final_rule=}")

        if op == '<':
            # print(f"{rule_intervals[var]=}")
            # x = rule_intervals[var]
            # print(f"{x[0]=};{x[1]=},{value=}")
            x = [rule_intervals[var][0], value-1]
            y = [value-1, rule_intervals[var][1]]
            # print(f"{x=}")
            # print(f"{y=}")
            branch_intervals[var] = x
            branch_else_intervals[var] = y
            branch_result = process_rule(dest, branch_intervals)
            print(f"{branch_result=}")
        # else:
            # branch_intervals[var] = y
            # print(f"{branch_else_intervals=}")
        if op == '>':
            # print(f"{rule_intervals[var]=}")
            # x = rule_intervals[var]
            # print(f"{x[0]=};{x[1]=},{value=}")
            x = [value, rule_intervals[var][1]]
            y = [rule_intervals[var][0], value]

            branch_intervals[var] = x
            branch_else_intervals[var] = y

        print(f"{var} {op} {value}, go to {dest}, {branch_intervals=}, {branch_else_intervals=}")
        print()
    # print(f"{branch_intervals=}")
    # print(f"{branch_else_intervals=}")
    print(f"{rule_possible=}")
    print(f"{else_possible=}")
    return rule_possible | else_possible

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
        return result
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

    def _calculate_2_(self):
        # 167409079868000
        # 256000000000000
        poss = {}
        poss2 = {}
        for i in ('x', 'm', 'a', 's'):
            poss[i] = [0, 4000]
            poss2[i] = set()
        print(f"{poss=}")

        rules = {}
        for x in self.__input_data1:
            rules[x.name] = x.processed
        print(f"{rules=}\n")

        # rule = rules['in']
        for rule in rules.values():
            # print(f"{rule=}")
            possible_dests= set()
            for j in rule:
                # continue
                tmp = j.split(':')
                var = None
                op = None
                value = None
                if len(tmp)>1:
                    cond, dest = tmp
                    var = cond[0]
                    op = cond[1]
                    value = int(cond[2:])

                    # poss[var].append(value)
                else:
                    cond = None
                    dest = tmp[0]
                possible_dests.add(dest)
            # print(f"{possible_dests=}, {len(possible_dests)=}")
            if len(possible_dests) <=1:
                continue
            for j in rule:
                tmp = j.split(':')
                var = None
                op = None
                value = None
                if len(tmp)>1:
                    cond, dest = tmp
                    var = cond[0]
                    op = cond[1]
                    value = int(cond[2:])

                    poss[var].append(value)
                else:
                    cond = None
                    dest = tmp[0]

                # print(f"{cond=},{var=},{op=},{value=} \t{dest=}")

                if dest in ('A', 'R'):
                    final_rule = True
                else:
                    final_rule = False

        # print(f"{poss=}")
        # return 0
        poss = {k:sorted(v) for k,v in poss.items()}
        print(f"{poss=}")

        for k,v in poss.items():
            # print(k, v)
            print(k, len(v))
        combs = list(product(poss['x'], poss['m'], poss['a'], poss['s']))
        print(f"{len(combs)=}")

        # template = f"x={x},m={m},a={a},s={s}"
        template = "x={0},m={1},a={2},s={3}"
        new_input = [Row2(template.format(*i)) for i in combs]
        # for i in combs:
        #     print(i)
        #     print(Row2(template.format(*i)))
        # print(self.__input_data2[0])
        #     for val in v:
        #         print(k, val)
        #
        acceptance = {}
        for x in new_input:
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

            print(dest)
            if dest=='A':
                acceptance[x.original] = True
        print(len(acceptance))
        print(poss)

        c= 0
        for k,v in acceptance.items():
            c+=1
            print(k)
            print(Row("{" + k +"}").processed)
            if c>10:
                break
        return 0
        result = 1
        for i in poss:
            # print(f"{len(poss[i])=}")
            pox=0
            for j in range(len(poss[i])-1):
                # print(poss[i][j+1], poss[i][j])
                # print(poss[i][j+1] - poss[i][j])
                pox+=(poss[i][j+1] - poss[i][j])
                # print(f"{pox=}")
            result*=pox
        return result

    def _calculate_2(self):
        poss ={}
        for i in ('x', 'm', 'a', 's'):
            poss[i] = [4000]
        # print(f"{poss=}")
        rules = {}
        for x in self.__input_data1:
            rules[x.name] = x.processed
        # print(f"{rules=}")
        # for rule in rules.values():
        #     print(f"{rule=}")
            # break
        rule = rules['in']
        rule_intervals = {i:[0, 4000] for i in ('x', 'm', 'a', 's')}
        process_rule(rule, rule_intervals, rules)
        return 0
        print(f"{rule=}")
        rule_intervals = {i:[0, 4000] for i in ('x', 'm', 'a', 's')}
        branch_intervals = {k:v for k,v in rule_intervals.items()}
        for branch in rule:

            print(f"{branch=}, {branch_intervals=}")
            tmp = branch.split(':')
            if len(tmp)>1:
                cond, dest = tmp
            else:
                cond = None
                dest = tmp[0]

            var = cond[0] if cond else None
            op = cond[1] if cond else None
            value = int(cond[2:]) if cond else None

            if dest in ('A', 'R'):
                final_rule = True
            else:
                final_rule = False
            print(f"{branch=},{var=},{op=},{value=} \t{dest=}, {final_rule=}")

            if op == '<':
                # if k.rate < value:
                print(f"{branch_intervals[var]=}")
                x = branch_intervals[var]
                print(f"{x[0]=};{x[1]=},{value=}")
                x = [branch_intervals[var][0], value-1]
                y = [value-1, branch_intervals[var][1]]
                print(f"{x=}")
                print(f"{y=}")
                branch_intervals[var] = y
                print(f"{var} {op} {value}, go to {dest}")
                #     if final_rule:
                #         rule = None
                #     else:
                #         rule = rules[dest]
                #     found = True
                #     break
            if op == '>':
                # if k.rate > value:
                print(f"{branch_intervals[var]}")
                print(f"{var} {op} {value}, go to {dest}")
                #     if final_rule:
                #         rule = None
                #     else:
                #         rule = rules[dest]
                #     found = True
                #     break
            print(f">>>{branch=}, {branch_intervals=}")
        print(f"{rule_intervals=}")
        return 0
