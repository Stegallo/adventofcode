from collections import defaultdict

from .common import AoCDay

TOT = 0
FOLDER_SIZES = {}
MIN_SIZE = 0


def size(local_pos, folders_files, folders_dirs):
    global TOT
    global FOLDER_SIZES
    # print(f'{folders_files[local_pos]=}')

    local_size = sum(int(i.split()[0]) for i in folders_files[local_pos])
    # print(local_size)
    # print(f'{folders_dirs[local_pos]=}')
    nested_size = sum(
        size(f"{local_pos}#{i}", folders_files, folders_dirs)
        for i in folders_dirs[local_pos]
    )
    sum_size = local_size + nested_size
    # print(f"{local_pos} has size {sum_size}")
    FOLDER_SIZES[local_pos] = sum_size
    if sum_size <= 100000:
        TOT += sum_size
    return sum_size


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = self._input_data[0]

    def _calculate_1(self):
        x = self.__input_data
        current_pos = []
        folders_files = defaultdict(list)
        folders_dirs = defaultdict(list)
        for i in x:
            # print(f"{i=}")
            # if '..' in i:
            #     breakpoint()
            if i[0] == "$":
                # print(f'command {i}')
                if i[2:4] == "cd":
                    # print(f'cd {i}')
                    if ".." in i[5:]:
                        # print(f'up one level {i}, {current_pos=}')
                        current_pos.pop()
                    else:
                        current_pos.append(i[5:])
                        # print(f'go inside {i}, {current_pos=}')
                # else:
                #     if i[2:4]=='ls':
                #         print(f'ls {i}')
                #         folders['#'.join(current_pos)]={files:}
            elif "dir" in i[:3]:
                # print(f'command {i}')
                folders_dirs["#".join(current_pos)].append(i[4:])
            else:
                folders_files["#".join(current_pos)].append(i)
            # if i[0]==''
        # print(f"{current_pos=}")
        # print(f"{folders_dirs=}")
        # print(f"{folders_files=}")
        local_pos = "/"
        # print(f"{folders_files[local_pos]=}")
        size(local_pos, folders_files, folders_dirs)
        # print(FOLDER_SIZES)

        return TOT

    def _calculate_2(self):
        needed = abs(70000000 - 30000000 - FOLDER_SIZES["/"])
        # print(needed)
        sorted_folder_sizes = dict(
            sorted(FOLDER_SIZES.items(), key=lambda item: item[1]),
        )
        for v in sorted_folder_sizes.values():
            if v > needed:
                return v
