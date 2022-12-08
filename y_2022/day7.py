from typing import Any, List, Optional

from .common import AoCDay


class Folder:
    def __init__(self, name: str, parent: Optional["Folder"]) -> None:
        self.name = name
        self.parent = parent
        self.dirs: List[Any] = []
        self.files: List[Any] = []

    @property
    def full_name(self):
        return f"{self.parent.full_name}#{self.name}" if self.parent else self.name

    @property
    def folder_size(self) -> int:
        return sum(int(i.split()[0]) for i in self.files)

    @property
    def nested_size(self) -> int:
        return sum(i.total_size for i in self.dirs)

    @property
    def total_size(self) -> int:
        return self.nested_size + self.folder_size


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.TOT = 0
        self.FOLDER_SIZES = {}
        self.MIN_SIZE = {}

        self.folders = {}
        current_folder = None
        for i in self._input_data[0]:
            if i[0] == "$":
                if i[2:4] == "cd":
                    if ".." in i[5:]:
                        current_folder = current_folder.parent
                    else:
                        f = Folder(i[5:], current_folder)
                        self.folders[f.full_name] = f
                        if current_folder:
                            current_folder.dirs.append(self.folders[f.full_name])
                        current_folder = f

            elif "dir" not in i[:3]:
                current_folder.files.append(i)

    def _calculate_1(self):
        return sum(
            i.total_size for i in self.folders.values() if i.total_size <= 100000
        )

    def _calculate_2(self):
        needed = abs(70000000 - 30000000 - self.folders["/"].total_size)

        sorted_folder_sizes = dict(
            sorted(self.folders.items(), key=lambda item: item[1].total_size),
        )
        for v in sorted_folder_sizes.values():
            if v.total_size > needed:
                return v.total_size
