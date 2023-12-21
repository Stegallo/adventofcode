from typing import Optional, List, Any

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
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

    def split(self, int):
        if int>self.end or int<self.start:
            raise Exception()
        return [Interval(self.start, int), Interval(int, self.end)]

    @property
    def len(self):
        return self.end-self.start

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
        self.rules = {}
        for i in self.__input_rules:
            self.rules[i.name] = i
        rule = self.rules['in']
        variables = {'x':Interval(1, 4001),
         'm':Interval(1, 4001),
         'a':Interval(1, 4001),
         's':Interval(1, 4001)}
        self.get_possibile(rule, variables)
        return 0
