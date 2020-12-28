import re

from .common import AoCDay
from .utils import prod


class Tile:
    def __init__(self, borders):
        self.n_border = borders[0]
        self.e_border = borders[1]
        self.s_border = borders[2]
        self.w_border = borders[3]

    def flip(self):
        return Tile(
            [
                self.s_border,
                "".join(reversed(list(self.e_border))),
                self.n_border,
                "".join(reversed(list(self.w_border))),
            ]
        )

    def rotate90(self):
        return Tile(
            [
                "".join(reversed(list(self.w_border))),
                self.n_border,
                "".join(reversed(list(self.e_border))),
                self.s_border,
            ]
        )

    def rotate180(self):
        return Tile(
            [
                "".join(reversed(list(self.s_border))),
                "".join(reversed(list(self.w_border))),
                "".join(reversed(list(self.n_border))),
                "".join(reversed(list(self.e_border))),
            ]
        )

    def rotate270(self):
        return Tile(
            [
                self.e_border,
                "".join(reversed(list(self.s_border))),
                self.w_border,
                "".join(reversed(list(self.n_border))),
            ]
        )


class Day(AoCDay):
    def __init__(self):
        super().__init__(20)

    def _preprocess_input(self):
        self.__tiles = {}
        current_tile = None
        for i in self._input_data:
            if i == "":
                continue
            # print(f"{i=}")
            if "Tile" in i:
                current_tile = int(re.findall("\d+", i)[0])
                self.__tiles[current_tile] = []
            else:
                self.__tiles[current_tile].append(i)

    def __get_borders(self, i):
        return [
            self.__tiles[i][0],
            "".join([j[-1] for j in self.__tiles[i]]),
            self.__tiles[i][-1],
            "".join([j[0] for j in self.__tiles[i]]),
        ]

    def _calculate_1(self):
        local = {}
        for i in self.__tiles:
            local[i] = Tile(self.__get_borders(i))
        adj = {}
        for k1, v1 in local.items():
            north_match = set()
            east_match = set()
            south_match = set()
            west_match = set()
            for k2, v2 in local.items():
                if k1 == k2:
                    continue
                # print(f"{k2=}{v2}")
                # breakpoint()
                if v1.s_border == v2.n_border:
                    south_match.add(k2)
                if v1.s_border == v2.flip().n_border:
                    south_match.add(k2)
                if v1.s_border == v2.rotate90().n_border:
                    south_match.add(k2)
                if v1.s_border == v2.rotate180().n_border:
                    south_match.add(k2)
                if v1.s_border == v2.rotate270().n_border:
                    south_match.add(k2)

                if v1.flip().s_border == v2.flip().n_border:
                    south_match.add(k2)
                if v1.flip().s_border == v2.rotate90().n_border:
                    south_match.add(k2)
                if v1.flip().s_border == v2.rotate180().n_border:
                    south_match.add(k2)
                if v1.flip().s_border == v2.rotate270().n_border:
                    south_match.add(k2)

                if v1.rotate90().s_border == v2.flip().n_border:
                    south_match.add(k2)
                if v1.rotate90().s_border == v2.rotate90().n_border:
                    south_match.add(k2)
                if v1.rotate90().s_border == v2.rotate180().n_border:
                    south_match.add(k2)
                if v1.rotate90().s_border == v2.rotate270().n_border:
                    south_match.add(k2)

                if v1.rotate180().s_border == v2.flip().n_border:
                    south_match.add(k2)
                if v1.rotate180().s_border == v2.rotate90().n_border:
                    south_match.add(k2)
                if v1.rotate180().s_border == v2.rotate180().n_border:
                    south_match.add(k2)
                if v1.rotate180().s_border == v2.rotate270().n_border:
                    south_match.add(k2)

                if v1.rotate270().s_border == v2.flip().n_border:
                    south_match.add(k2)
                if v1.rotate270().s_border == v2.rotate90().n_border:
                    south_match.add(k2)
                if v1.rotate270().s_border == v2.rotate180().n_border:
                    south_match.add(k2)
                if v1.rotate270().s_border == v2.rotate270().n_border:
                    south_match.add(k2)

                # breakpoint()
                if v1.e_border == v2.w_border:
                    east_match.add(k2)
                if v1.e_border == v2.flip().w_border:
                    east_match.add(k2)
                if v1.e_border == v2.rotate90().w_border:
                    east_match.add(k2)
                if v1.e_border == v2.rotate180().w_border:
                    east_match.add(k2)
                if v1.e_border == v2.rotate270().w_border:
                    east_match.add(k2)

                if v1.flip().e_border == v2.flip().w_border:
                    east_match.add(k2)
                if v1.flip().e_border == v2.rotate90().w_border:
                    east_match.add(k2)
                if v1.flip().e_border == v2.rotate180().w_border:
                    east_match.add(k2)
                if v1.flip().e_border == v2.rotate270().w_border:
                    east_match.add(k2)

                if v1.rotate90().e_border == v2.flip().w_border:
                    east_match.add(k2)
                if v1.rotate90().e_border == v2.rotate90().w_border:
                    east_match.add(k2)
                if v1.rotate90().e_border == v2.rotate180().w_border:
                    east_match.add(k2)
                if v1.rotate90().e_border == v2.rotate270().w_border:
                    east_match.add(k2)

                if v1.rotate180().e_border == v2.flip().w_border:
                    east_match.add(k2)
                if v1.rotate180().e_border == v2.rotate90().w_border:
                    east_match.add(k2)
                if v1.rotate180().e_border == v2.rotate180().w_border:
                    east_match.add(k2)
                if v1.rotate180().e_border == v2.rotate270().w_border:
                    east_match.add(k2)

                if v1.rotate270().e_border == v2.flip().w_border:
                    east_match.add(k2)
                if v1.rotate270().e_border == v2.rotate90().w_border:
                    east_match.add(k2)
                if v1.rotate270().e_border == v2.rotate180().w_border:
                    east_match.add(k2)
                if v1.rotate270().e_border == v2.rotate270().w_border:
                    east_match.add(k2)

                # breakpoint()
                if v1.n_border == v2.s_border:
                    north_match.add(k2)
                if v1.n_border == v2.flip().s_border:
                    north_match.add(k2)
                if v1.n_border == v2.rotate90().s_border:
                    north_match.add(k2)
                if v1.n_border == v2.rotate180().s_border:
                    north_match.add(k2)
                if v1.n_border == v2.rotate270().s_border:
                    north_match.add(k2)

                if v1.flip().n_border == v2.flip().s_border:
                    north_match.add(k2)
                if v1.flip().n_border == v2.rotate90().s_border:
                    north_match.add(k2)
                if v1.flip().n_border == v2.rotate180().s_border:
                    north_match.add(k2)
                if v1.flip().n_border == v2.rotate270().s_border:
                    north_match.add(k2)

                if v1.rotate90().n_border == v2.flip().s_border:
                    north_match.add(k2)
                if v1.rotate90().n_border == v2.rotate90().s_border:
                    north_match.add(k2)
                if v1.rotate90().n_border == v2.rotate180().s_border:
                    north_match.add(k2)
                if v1.rotate90().n_border == v2.rotate270().s_border:
                    north_match.add(k2)

                if v1.rotate180().n_border == v2.flip().s_border:
                    north_match.add(k2)
                if v1.rotate180().n_border == v2.rotate90().s_border:
                    north_match.add(k2)
                if v1.rotate180().n_border == v2.rotate180().s_border:
                    north_match.add(k2)
                if v1.rotate180().n_border == v2.rotate270().s_border:
                    north_match.add(k2)

                if v1.rotate270().n_border == v2.flip().s_border:
                    north_match.add(k2)
                if v1.rotate270().n_border == v2.rotate90().s_border:
                    north_match.add(k2)
                if v1.rotate270().n_border == v2.rotate180().s_border:
                    north_match.add(k2)
                if v1.rotate270().n_border == v2.rotate270().s_border:
                    north_match.add(k2)
                # breakpoint()
                if v1.w_border == v2.e_border:
                    west_match.add(k2)
                if v1.w_border == v2.flip().e_border:
                    west_match.add(k2)
                if v1.w_border == v2.rotate90().e_border:
                    west_match.add(k2)
                if v1.w_border == v2.rotate180().e_border:
                    west_match.add(k2)
                if v1.w_border == v2.rotate270().e_border:
                    west_match.add(k2)

                if v1.flip().w_border == v2.flip().e_border:
                    west_match.add(k2)
                if v1.flip().w_border == v2.rotate90().e_border:
                    west_match.add(k2)
                if v1.flip().w_border == v2.rotate180().e_border:
                    west_match.add(k2)
                if v1.flip().w_border == v2.rotate270().e_border:
                    west_match.add(k2)

                if v1.rotate90().w_border == v2.flip().e_border:
                    west_match.add(k2)
                if v1.rotate90().w_border == v2.rotate90().e_border:
                    west_match.add(k2)
                if v1.rotate90().w_border == v2.rotate180().e_border:
                    west_match.add(k2)
                if v1.rotate90().w_border == v2.rotate270().e_border:
                    west_match.add(k2)

                if v1.rotate180().w_border == v2.flip().e_border:
                    west_match.add(k2)
                if v1.rotate180().w_border == v2.rotate90().e_border:
                    west_match.add(k2)
                if v1.rotate180().w_border == v2.rotate180().e_border:
                    west_match.add(k2)
                if v1.rotate180().w_border == v2.rotate270().e_border:
                    west_match.add(k2)

                if v1.rotate270().w_border == v2.flip().e_border:
                    west_match.add(k2)
                if v1.rotate270().w_border == v2.rotate90().e_border:
                    west_match.add(k2)
                if v1.rotate270().w_border == v2.rotate180().e_border:
                    west_match.add(k2)
                if v1.rotate270().w_border == v2.rotate270().e_border:
                    west_match.add(k2)
            adj[k1] = north_match | east_match | south_match | west_match
        # print(f"{adj=}\n")
        # print([k for k, v in adj.items() if len(v) == 2])
        return prod(k for k, v in adj.items() if len(v) == 2)

    def _calculate_2(self):
        self.__input
        return 0
