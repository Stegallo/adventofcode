from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(13)

    def _preprocess_input(self):
        self.__input = [i for i in self._input_data]

    def _calculate_1(self):
        # info(self._input_data)
        # print(*self._input_data, sep="\n")
        # y = [int(i) for i in self._input_data.split(",")]
        # print(sum(y))
        print(self.__input)
        arr = int(self.__input[0])
        buses = [int(i) for i in self.__input[1].split(",") if i != "x"]
        print(f"{buses=}")
        schedule = {}  # defaultdict(int)
        for i in buses:
            c = 0
            schedule[i] = []
            while True:
                c += 1
                schedule[i].append(i * c)
                if i * c > arr * 2:
                    break
        # print(f"{schedule=}")
        mins = {}
        for k, v in schedule.items():
            for i in v:
                if i >= arr:
                    mins[k] = i
                    break
        # print(f"{mins=}")
        min_x = min([m for m in mins.values()])
        min_x = arr * 10
        for k, v in mins.items():
            if v < min_x:
                min_x = v
                bus_id = k

        print(f"{min_x=}")
        return (min_x - arr) * bus_id

    def _calculate_2(self):
        buses = {
            int(value): position
            for position, value in enumerate(self.__input[1].split(","))
            if value != "x"
        }
        print(f"{buses=}")

        time = 0
        step = 1

        for value, gap in buses.items():
            # print(f"{value=}, {gap=}")
            for i in range(time, step * value, step):
                # print(f"{i=}, {(i + gap)=}, {(i + gap) % value=}")
                if not (i + gap) % value:
                    step = step * value
                    time = i
                    break
        return time
