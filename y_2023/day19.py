from typing import Optional, List, Any

from pydantic.dataclasses import dataclass
from math import prod
from common.aoc import AoCDay
from common.utilities import fprint
from itertools import product

@dataclass
class Branch:
    var:str
    op:str
    value:int
    dest:str

    @staticmethod
    def from_input(input: str) -> Any:
        varop, dest = input.split(':')
        var= varop[0]
        op = varop[1]
        value = int(varop[2:])
        return Branch(var, op, value, dest)

    def combinations(self, var) -> int:
        assert False
        options = var.split(self.value)
        result = None
        # breakpoint()
        if self.op == '<':
            if options[0].start < self.value:
                result = options
        if self.op == '>':
            if options[0].start < self.value:
                result = options[::-1]
        # if self.dest == 'A':
        #     return 1
        # if self.dest == 'R':
        #     return 0
        assert result is not None
        return result

    def evaluate(self, var: int) ->bool:
        if self.op == '<':
            if var.start < self.value:
                return True
        if self.op == '>':
            if var.start > self.value:
                return True
        return False

    def intervals(self, var):
        # breakpoint()
        options = var.split(self.value, self.op)
        # print(f'{self.op=}\t{self.value=}, {var=}\t{options=}')

        if self.op == '<':
            return options
        if self.op == '>':
            return options[::-1]
        assert False
        return None

@dataclass
class ElseBranch:
    dest:str

@dataclass
class Rule:
    name: str
    branches: List[Branch]
    else_rule: ElseBranch

    @staticmethod
    def from_input(input: str) -> Any:
        a,b=input.split('{')
        bs=b.replace('}','').split(',')

        return Rule(a, [Branch.from_input(i) for i in bs[:-1]],ElseBranch(bs[-1]))

@dataclass
class Rating:
    name:str
    rate:int

@dataclass
class Input:
    original: str
    processed: List[Rating] = None

    def __post_init__(self) -> None:
        self.processed = [Rating(*i.split('=')) for i in self.original.replace('{', '').replace('}', '').split(',')]

    @property
    def value(self) -> int:
        return sum(i.rate for i in self.processed)

@dataclass
class Interval:
    start:int
    end:int

    def split(self, int, op):
        if int>self.end or int<self.start:
            raise Exception()
        if op == '<':
            return [Interval(self.start, int), Interval(int, self.end)]
        if op == '>':
            return [Interval(self.start, int+1), Interval(int+1, self.end)]
        assert False

    @property
    def len(self):
        return self.end-self.start

@dataclass
class State:
    state: Any = None

    def __init__(self, state):
        self.state = state

    @property
    def len(self):
        return prod(i.len for i in self.state.values())

    def apply(self, rule, rules, pad = ''):
        # print(f"{pad}{rule}")
        if not rule.branches:
            # breakpoint()
            # print(f"{pad}rule {rule.name} with no branches")
            if rule.else_rule.dest == 'A':
                return self.len
            if rule.else_rule.dest == 'R':
                return 0
            assert False
        states = []
        else_intervals = {}
        branch_results = []
        else_result = None
        for i in rule.branches:
            # print(f"{pad}{rule.name=}, branch={i}")
            var = self.state[i.var]
            intervals = i.intervals(var)
            # print(intervals)
            # create 2 new states
            state1 = State(self.state | {i.var: intervals[0]} | else_intervals)
            # state2 = State(self.state | {i.var: intervals[1]})
            else_intervals[i.var] = intervals[1]
            # print(state1)
            # print(state2)
            states.append(state1)
            # breakpoint()
            state1result = state1.apply(rules[i.dest], rules, pad+' ')
            # states.append(state2)
            # breakpoint()
            # print(f"{pad}{rule.name=}branch={i}\t{state1result=} {state1.len=}")
            # branch_results.append(state1result)
            # breakpoint()
            # if not state1result
            # if state1result not in (0,1):
            #     print(f"{pad}here")
            #     branch_results.append(state1result)
            # else:
            branch_results.append(state1result)
            # return state1result * state1.len
            # print(f"{pad}{rule.name=}branch={i}{branch_results=}")
        # breakpoint()
        # print(f"{pad}{branch_results=}")
        states.append(State(self.state | else_intervals))
        else_state = State(self.state | else_intervals)
        else_result = else_state.apply(rules[rule.else_rule.dest], rules, pad+' ')
        # print(f"{pad}{else_result=}")
        # print(f"{pad}states=")
        # for i in states:
        #     print(f"{pad}{i}")
        # print(f"{pad}{branch_results=}{else_result=}")
        return sum(branch_results)+else_result
        print()

class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        self.__input_rules = [Rule.from_input(i) for i in self._input_data[0]]
        x = [Input(i) for i in self._input_data[1]]
        z = []
        for i in x:
            y = [(j.name, j.rate) for j in i.processed]
            z.append(dict(y))
        self.__input_data2 = zip(x,z)

    def get_possibile(self, rule, variables, pad=''):
        print(f"{pad}{rule=}")
        # breakpoint()
        # x=Interval(1,4001)
        # m=Interval(1,4001)
        # a=Interval(1,4001)
        # s=Interval(1,4001)

        result = None
        else_intervals = {}
        for branch in rule.branches:
            branch_intervals = {}
            print(f"{pad}{branch=}")
            # if branch.dest in ('A', 'R'):
            #     return branch.dest
            print(f"{variables[branch.var]=}")
            # evaluation = branch.evaluate(variables[branch.var])
            # breakpoint()
            evaluation = branch.combinations(variables[branch.var])
            print(f"{pad}{evaluation=}")
            branch_intervals[branch.var]=evaluation[0]
            else_intervals[branch.var]=evaluation[1]
            # breakpoint()
            if branch.dest in ('A', 'R'):
                breakpoint()
                if branch.dest == 'A':
                    return {branch.var: evaluation[0]}
                # if branch.dest == 'R':
                #     return False
            for k,v in variables.items():
                if k not in branch_intervals:
                    branch_intervals[k] = v
            possible = self.get_possibile(self.rules[branch.dest], branch_intervals, pad+'  ')
            if possible is not None:

                for k,v in variables.items():
                    if k not in possible:
                        possible[k] = v
                breakpoint()
                print(f"{possible=}")
            continue

        if result is not None:
            return result
        print(f"{pad}{rule.else_rule=}")
        for k,v in variables.items():
            if k not in else_intervals:
                else_intervals[k] = v
        if rule.else_rule.dest in ('A', 'R'):
            if rule.else_rule.dest == 'A':
                return else_intervals
            # if rule.else_rule.dest == 'R':
            #     return 0
            # return rule.else_rule.dest
        print(f"{else_intervals=}")
        return self.get_possibile(self.rules[rule.else_rule.dest], else_intervals, pad+'  ')
        return 0

    def _calculate_1(self) -> int:
        return 0
        self.rules = {}
        for i in self.__input_rules:
            self.rules[i.name] = i
        rule = self.rules['in']
        result=0
        variables = {}
        for i in self.__input_data2:
            print(f"{i=}")
            for vars in ('x','m','a','s'):
                variables[vars] = Interval(i[1][vars],i[1][vars]+1)
            print(variables)
            if self.get_possibile(rule, variables) == 1:
                result += i[0].value
        return result
        # variables = {
        # 'x':Interval(787, 788),
        # 'm':Interval(2655, 2656),
        # 'a':Interval(1222, 1223),
        # 's':Interval(2876, 2877),
        # }

    def _calculate_2(self) -> int:
        s = State({
         'x':Interval(1, 4001),
         'm':Interval(1, 4001),
         'a':Interval(1, 4001),
         's':Interval(1, 4001),
         })
        self.rules = {}
        for i in self.__input_rules:
            self.rules[i.name] = i
        rule = self.rules['in']
        # rule = self.rules['end']
        self.rules['A']= Rule.from_input('A{A}')
        self.rules['R']= Rule.from_input('R{R}')
        # print(s)

        # 167409079868000
        # 167409079868000
        return s.apply(rule, self.rules)
        # 268730360502076
        # 256000000000000

        variables = {'x':Interval(1, 4001),
         'm':Interval(1, 4001),
         'a':Interval(1, 4001),
         's':Interval(1, 4001)}
        self.get_possibile(rule, variables)
        return 0
