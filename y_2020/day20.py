import re
from collections import defaultdict
from itertools import combinations
from .common import AoCDay
from .utils import prod
import json
import copy
from operator import itemgetter


class Day(AoCDay):
    def __init__(self):
        super().__init__(20)

    def _preprocess_input(self):

        self.__tiles = {}
        current_tile = None
        for i in self._input_data:
            if i == "":
                continue
            if "Tile" in i:
                current_tile = int(re.findall("\d+", i)[0])
                self.__tiles[current_tile] = []
            else:
                self.__tiles[current_tile].append(i)

    def rotate90(self, tile):
        new = []
        for c in range(len(tile[0])):
            new_row = "".join(row[c] for row in tile)[::-1]
            new.append(new_row)
        return new

    def edge(self, matrix, side):
        if side == "n":
            return matrix[0]
        if side == "s":
            return matrix[-1]
        if side == "e":
            return "".join(map(itemgetter(-1), matrix))
        # 'w'
        return "".join(map(itemgetter(0), matrix))

    def get_corners(self):
        matching_sides = defaultdict(str)

        corners = {}

        # For every pair of distinct tiles
        for id_a, id_b in combinations(self.__tiles, 2):
            a, b = self.__tiles[id_a], self.__tiles[id_b]

            # For each possible pair of sides
            for side_a in "nsew":
                for side_b in "nsew":
                    # Extract the edges correspoinding to these sides
                    edge_a, edge_b = self.edge(a, side_a), self.edge(b, side_b)

                    # Check if they match
                    if edge_a == edge_b or edge_a == edge_b[::-1]:
                        matching_sides[id_a] += side_a
                        matching_sides[id_b] += side_b

        # Find the corner tiles by checking tiles that only match two other tiles
        for tid, sides in matching_sides.items():
            if len(sides) == 2:
                corners[tid] = sides  # changed
        assert len(corners) == 4  # Sanity check
        return corners

    def _calculate_1(self):
        return prod(self.get_corners())

    def orientations(self, tile):
        yield tile
        for _ in range(3):
            tile = self.rotate90(tile)
            yield tile

    def arrangements(self, tile):
        yield from self.orientations(tile)
        yield from self.orientations(tile[::-1])

    def build_image(self, top_left_tile, image_dimension):
        # Start from the top left
        first = top_left_tile
        image = []

        while 1:
            # Get a row of matching tiles
            image_row = self.matching_row(first, image_dimension)
            # Strip the outermost edges from each of them
            image_row = map(self.strip_edges, image_row)
            # Add together each row of the tiles into a single big row, and add it to the final image
            image.extend(map("".join, zip(*image_row)))

            # Do this until tiles run out
            if not self.__tiles:
                break

            # Match the first tile of the next row, which is south of the first tile of the current row
            first = self.matching_tile(first, "s", "n")

        return image

    def matching_tile(self, tile, side_a, side_b):
        prev_side = self.edge(tile, side_a)

        # Iterate over all possible tiles
        for other_id, other in self.__tiles.items():
            if tile is other:
                continue

            # Arrange second tile in any possible way
            for other in self.arrangements(other):
                # Until the two sides match
                if prev_side == self.edge(other, side_b):
                    self.__tiles.pop(other_id)
                    return other

    def matching_row(self, prev, tiles_per_row):
        yield prev
        for _ in range(tiles_per_row - 1):
            tile = self.matching_tile(prev, "e", "w")
            prev = tile
            yield prev

    def strip_edges(self, tile):
        return [row[1:-1] for row in tile[1:-1]]

    def count_pattern(self, image, pattern):
        pattern_h, pattern_w = len(pattern), len(pattern[0])
        image_sz = len(image)
        deltas = []

        for r, row in enumerate(pattern):
            for c, cell in enumerate(row):
                if cell == "#":
                    deltas.append((r, c))

        for img in self.arrangements(image):
            n = 0
            for r in range(image_sz - pattern_h):
                for c in range(image_sz - pattern_w):
                    if all(img[r + dr][c + dc] == "#" for dr, dc in deltas):
                        n += 1

            if n != 0:
                return n

    def _calculate_2(self):
        corners = self.get_corners()
        top_left_id, matching_sides = corners.popitem()
        top_left = self.__tiles[top_left_id]

        if matching_sides in (
            "ne",
            "en",
        ):  # North & East edges match other tiles, rotate 90 degrees clockwise
            top_left = self.rotate90(top_left)
        elif matching_sides in (
            "nw",
            "wn",
        ):  # North & West edges match other tiles, rotate 180 degrees clockwise
            top_left = self.rotate90(self.rotate90(top_left))
        elif matching_sides in (
            "sw",
            "ws",
        ):  # South & West edges match other tiles, rotate 270 degrees clockwise
            top_left = self.rotate90(self.rotate90(self.rotate90(top_left)))

        import math

        size = int(math.sqrt(len(self.__tiles)))
        self.__tiles.pop(top_left_id)

        image = self.build_image(top_left, size)
        MONSTER_PATTERN = (
            "                  # ",
            "#    ##    ##    ###",
            " #  #  #  #  #  #   ",
        )

        monster_cells = sum(row.count("#") for row in MONSTER_PATTERN)
        water_cells = sum(row.count("#") for row in image)
        n_monsters = self.count_pattern(image, MONSTER_PATTERN)
        roughness = water_cells - n_monsters * monster_cells

        return roughness
