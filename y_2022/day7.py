from typing import Dict, List, Optional

from .common import AoCDay


class File:
    def __init__(self, file: str) -> None:
        raw_size, name = file.split()
        self.size = int(raw_size)
        self.name = name


class Folder:
    def __init__(self, name: str, parent: Optional["Folder"]) -> None:
        self.name = name
        self.parent = parent
        self.dirs: List["Folder"] = []
        self.files: List[File] = []

    @property
    def full_name(self):
        return f"{self.parent.full_name}#{self.name}" if self.parent else self.name

    @property
    def folder_size(self) -> int:
        return sum(i.size for i in self.files)

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
        self.__folders: Dict[str, Folder] = {}
        current_folder = None
        for i in self._input_data[0]:
            if i[0] == "$":
                if i[2:4] == "cd":
                    if ".." in i[5:]:
                        current_folder = current_folder.parent
                    else:
                        f = Folder(i[5:], current_folder)
                        self.__folders[f.full_name] = f
                        if current_folder:
                            current_folder.dirs.append(self.__folders[f.full_name])
                        current_folder = f

            elif "dir" not in i[:3]:
                current_folder.files.append(File(i))

    def _calculate_1(self):
        return sum(
            i.total_size for i in self.__folders.values() if i.total_size <= 100000
        )

    def _calculate_2(self):
        needed = abs(70000000 - 30000000 - self.__folders["/"].total_size)

        sorted_folder = dict(
            sorted(self.__folders.items(), key=lambda item: item[1].total_size),
        )
        for v in sorted_folder.values():
            if v.total_size > needed:
                return v.total_size
