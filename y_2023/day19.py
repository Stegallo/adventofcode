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

    def combinations(self) -> int:
        if self.dest == 'A':
            return 1
        if self.dest == 'R':
            return 0
        return None

    def evaluate(self, var: int) ->bool:
        # breakpoint()
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
        x=Interval(1,4001)
        m=Interval(1,4001)
        a=Interval(1,4001)
        s=Interval(1,4001)

        result = None
        for branch in rule.branches:
            print(f"{pad}{branch=}")
            # if branch.dest in ('A', 'R'):
            #     return branch.dest
            evaluation = branch.evaluate(variables[branch.var])
            print(f"{pad}{evaluation=}")
            if evaluation:
                if branch.dest in ('A', 'R'):
                    return branch.dest
                result = self.get_possibile(self.rules[branch.dest], variables, pad+'  ')
                print(f"{pad}{result=}")
                break
            # else:
            #     continue

        if result:
            return result
        print(f"{pad}{rule.else_rule=}")
        if rule.else_rule.dest in ('A', 'R'):
            return rule.else_rule.dest
        return self.get_possibile(self.rules[rule.else_rule.dest], variables, pad+'  ')
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
            if self.get_possibile(rule, variables) == 'A':
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
        return 0
