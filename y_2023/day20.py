from typing import Optional, List, Any, Dict

from pydantic.dataclasses import dataclass
from pydantic import Field
from common.aoc import AoCDay
import math
from collections import deque, defaultdict
from functools import lru_cache

MODULES = {}
PULSES = defaultdict(int)
press = 0

@dataclass
class Broadcaster:
    name: str
    dest: Any
    pulse: Optional[str] = None

    @property
    def state(self):
        return 'Broadcaster has no state'


    def send_pulse(self, name, pulse):
        self.pulse = pulse
        # print(f'>> Broadcaster received {pulse=}')

    def process(self):
        output = self.pulse
        res = []
        for i in self.dest:
            j = MODULES[i]
            # print(f"mando {output=} to {i}")
            PULSES[output]+=1
            j.send_pulse(self.name, output)
            res.append(j)
        self.pulse = None
        return res

    def advertise(self, name):
        # print(name)
        ...

@dataclass
class FlipFlop:
    name: str
    status: bool
    dest: Any
    pulse: Any = Field(default_factory=deque)
    output: Optional[str] = None

    @property
    def state(self):
        return self.output

    def __hash__(self) -> int:
        return hash(tuple((self.name, self.status, tuple(self.dest), tuple(self.pulse))))

    def send_pulse(self, name, pulse):
        self.pulse.append(pulse)
        # print(f'>> ff {self.name} received {pulse=}')

    # @lru_cache
    def process(self):
        # print(f'FlipFlop {self.name}, {self.pulse=} , {self.status=}')
        pulse = self.pulse.popleft()
        if pulse == 'high':
            return []
        if pulse == 'low':
            self.status = not self.status

        output = 'high' if self.status else 'low'
        self.output = output
        res = []
        for i in self.dest:
            j = MODULES[i]
            # print(f"mando {output=} to {i}")
            PULSES[output]+=1
            j.send_pulse(self.name, output)
            res.append(j)

        return res

    def advertise(self, name):
        # print(name)
        ...

@dataclass
class Conjunction:
    # Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; they initially default to remembering a low pulse for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
    name: str
    status: bool
    memory: Any #Dict[List[bool]]
    dest: Any
    inputs: Any = Field(default_factory=list)
    output: Optional[str] = None

    @property
    def state(self):
        return self.output

    def __hash__(self) -> int:
#         print(f"""{self.name}
# {type(self.status)}, {self.status}
# {type(self.memory)}, {self.memory.items()}
# {type(self.dest)}, {self.dest}
# {type(self.inputs)}, {self.inputs}""")
#         print(tuple((self.name, self.status, tuple(sorted(self.memory.items())), tuple(self.dest), tuple(self.inputs))))
        return hash(tuple((self.name, self.status, tuple(sorted(self.memory.items())), tuple(self.dest), tuple(self.inputs))))

    def send_pulse(self, name, pulse):
        self.memory[name] = pulse

    # @lru_cache
    def process(self):
        # print(f'Conjunction {self.name}, {self.status=}, {self.memory=}, {self.inputs=}, {self.dest=}')
        # breakpoint()
        # print(f"{self.memory=}")
        v = []
        for i in self.inputs:
            if i in self.memory:
                v.append(self.memory[i])
            else:
                v.append('low')
        # for i in self.memory.values():
        #     v.append(i.popleft())
        # print(f"{v=}")
        output = 'low' if all(i=='high' for i in v) else 'high'
        # if self.name in ('kd', 'zf', 'vg', 'gs'):
        # if self.name in ('zf', 'vg', 'gs'):
        # if self.name in ('vg', 'gs'):
        if self.name in ('vg'):
                if output == 'high':
                    print(f"{self.name},{press=}")
                    raise Exception()

                    # kd,press=3767
                    # zf,press=3779
                    # gs,press=3889
                    # vg,press=4057
                    # 3767*3779*3889*4057
                    # 224_602_953_547_789

        self.output = output
        res = []
        for i in self.dest:
            # if i=='rx':
            #     breakpoint()
            j = MODULES[i]
            # print(f"mando {output=} to {i}")
            PULSES[output]+=1
            j.send_pulse(self.name, output)
            res.append(j)
        # self.memory = []
        return res

    def advertise(self, name):
        # print(name)
        self.inputs.append(name)
        # print(f"{self.inputs=}")

class Output:
    dest = []

    @property
    def state(self):
        return 'Output has no state'

    def send_pulse(self, name, pulse):
        pass

    def process(self):
        return []

    def advertise(self, name):
        # print(name)
        ...

class Machine:
    name = 'Machine'

    @property
    def state(self):
        return 'Machine has no state'

    def send_pulse(self, name, pulse):
        # breakpoint()
        if pulse == 'low':
            breakpoint()

    def process(self):
        return []

    def advertise(self, name):
        # print(name)
        ...
@dataclass
class Row:
    original: str
    object: Optional[FlipFlop | Conjunction | Broadcaster]


    @staticmethod
    def from_input(str):
        if str:
            splits = str.split(' -> ')

            if str[0] == '%':
                return Row(str, FlipFlop(splits[0][1:], False, splits[1].split(', ')))
            if str[0] == '&':
                return Row(str, Conjunction(splits[0][1:], False, {}, str.split(' -> ')[1].split(', ')))
            if str.startswith('broadcaster'):
                return Row(str, Broadcaster('broadcaster', splits[1].split(', ')))
        return Row(str, None)


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = [Row.from_input(i) for i in self._input_data[0]]

    def iterate(self):

        signal_sequence= deque()
        signal_sequence.append(MODULES['broadcaster'])
        pulse = 'low'

        PULSES[pulse]+=1

        MODULES['broadcaster'].send_pulse('button', pulse)

        while signal_sequence:
            module = signal_sequence.popleft()

            res = module.process()

            signal_sequence.extend(res)
            # print(PULSES)

    def _calculate_1(self):
        return 0
        global PULSES
        PULSES = defaultdict(int)

        for x in self.__input_data:
            MODULES[x.object.name] = x.object
        MODULES['output'] = Output()

        signal_sequence= deque()

        items = [k for k in MODULES]
        for k in items:
            for i in MODULES[k].dest:
                try:
                    MODULES[i].advertise(k)
                except:
                    if i == 'rx':
                        MODULES[i] = Machine()
                    else:
                        MODULES[i] = Output()


        BUTTON_PRESSES = 1_000

        for press in range(BUTTON_PRESSES):
            self.iterate()

        print(f"{PULSES=}")
        return PULSES['low']*PULSES['high']

    def _calculate_2(self):
        # return 0
        global PULSES
        global press
        PULSES = defaultdict(int)

        for x in self.__input_data:
            MODULES[x.object.name] = x.object
        MODULES['output'] = Output()

        signal_sequence= deque()

        items = [k for k in MODULES]
        for k in items:
            for i in MODULES[k].dest:
                try:
                    MODULES[i].advertise(k)
                except:
                    if i == 'rx':
                        MODULES[i] = Machine()
                    else:
                        MODULES[i] = Output()

        press = 1
        result = defaultdict(list)
        while True:
            self.iterate()
            # print(f"{press=}")
            if press > 10_000_000:
                break
            press+=1
        print(f"{PULSES=}")
        # kd, zf, vg, gs
        #     for k, v in MODULES.items():
        #         result[k].append(v.state)
        #         # print(f"{k=}, \t{v.state=}")
        # unchanged = 0
        # total=0
        # for k, v in result.items():
        #     # print(set(v))
        #     new_v = set(v) if len(set(v))>1 else None
        #     if new_v:
        #         print(f"{k=}, \t{v=}")
        #         unchanged+=1
        #     total+=1
        # print(f"{unchanged=}, {total=}")
        return 0
