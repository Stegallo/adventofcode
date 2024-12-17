from typing import Optional

from pydantic.dataclasses import dataclass

from common.aoc import AoCDay
from common.grid import Grid, Cursor, Direction, Point


# from pprint import pprint as print
@dataclass
class Row:
    original: str
    processed: Optional[list[str]] = None

    def __post_init__(self) -> None:
        self.processed = list(self.original)


@dataclass
class Box:
    name: int
    point_1: Optional[Point] = None
    point_2: Optional[Point] = None

    def try_orizontal_push(self, point_box_map, dir: Direction, grid) -> bool:
        # print(f"{id(grid)=}")
        if dir.icon == ">":
            # print('try to push >')
            right_of_p1 = Point(self.point_2.x + 1, self.point_1.y)  # type: ignore
            box_to_right = point_box_map.get(right_of_p1)
            if box_to_right:
                if (
                    box_to_right.point_1 != right_of_p1
                    and box_to_right.point_2 != right_of_p1
                ):
                    raise Exception()

                if box_to_right.try_orizontal_push(point_box_map, dir, grid):
                    point_box_map[self.point_1] = None
                    self.point_1, self.point_2 = self.point_2, right_of_p1
                    grid[self.point_1] = "["
                    grid[self.point_2] = "]"
                    point_box_map[right_of_p1] = self
                    return True
                return False
            else:
                if grid[right_of_p1] == ".":
                    point_box_map[self.point_1] = None
                    self.point_1, self.point_2 = self.point_2, right_of_p1
                    grid[self.point_1] = "["
                    grid[self.point_2] = "]"
                    point_box_map[right_of_p1] = self
                    return True
                if grid[right_of_p1] == "#":
                    return False

        if dir.icon == "<":
            # print('try to push <')
            left_of_p1 = Point(self.point_1.x - 1, self.point_1.y)  # type: ignore
            box_to_left = point_box_map.get(left_of_p1)
            if box_to_left:
                if (
                    box_to_left.point_1 != left_of_p1
                    and box_to_left.point_2 != left_of_p1
                ):
                    raise Exception()

                if box_to_left.try_orizontal_push(point_box_map, dir, grid):
                    point_box_map[self.point_2] = None
                    self.point_1, self.point_2 = left_of_p1, self.point_1
                    grid[self.point_1] = "["
                    grid[self.point_2] = "]"
                    point_box_map[left_of_p1] = self
                    return True
                return False
            else:
                if grid[left_of_p1] == ".":
                    point_box_map[self.point_2] = None
                    self.point_1, self.point_2 = left_of_p1, self.point_1
                    grid[self.point_1] = "["
                    grid[self.point_2] = "]"
                    point_box_map[left_of_p1] = self
                    return True
                if grid[left_of_p1] == "#":
                    return False

        raise Exception()

    def check_vertical_push(self, point_box_map, dir: Direction, grid) -> bool:
        if dir.icon == "^":
            up_of_p1 = Point(self.point_1.x, self.point_1.y - 1)  # type: ignore
            up_of_p2 = Point(self.point_2.x, self.point_2.y - 1)  # type: ignore
            box_up_p1 = point_box_map.get(up_of_p1)
            box_up_p2 = point_box_map.get(up_of_p2)

            if box_up_p1 or box_up_p2:
                if grid.get(up_of_p1) == "#" or grid.get(up_of_p2) == "#":
                    return False
                if box_up_p1 == box_up_p2:
                    if box_up_p1.check_vertical_push(point_box_map, dir, grid):
                        return True
                    return False
                else:
                    if all(
                        i.check_vertical_push(point_box_map, dir, grid)
                        for i in [box_up_p1, box_up_p2]
                        if i
                    ):
                        return True
                    return False
            else:
                if grid[up_of_p1] == "." and grid[up_of_p2] == ".":
                    return True
                if grid[up_of_p1] == "#" or grid[up_of_p2] == "#":
                    return False

        if dir.icon == "v":
            down_of_p1 = Point(self.point_1.x, self.point_1.y + 1)  # type: ignore
            down_of_p2 = Point(self.point_2.x, self.point_2.y + 1)  # type: ignore
            box_down_p1 = point_box_map.get(down_of_p1)
            box_down_p2 = point_box_map.get(down_of_p2)

            if box_down_p1 or box_down_p2:
                if grid.get(down_of_p1) == "#" or grid.get(down_of_p2) == "#":
                    return False
                if box_down_p1 == box_down_p2:
                    if box_down_p1.check_vertical_push(point_box_map, dir, grid):
                        return True
                    return False
                else:
                    if all(
                        i.check_vertical_push(point_box_map, dir, grid)
                        for i in [box_down_p1, box_down_p2]
                        if i
                    ):
                        return True
                    return False
            else:
                if grid[down_of_p1] == "." and grid[down_of_p2] == ".":
                    return True
                if grid[down_of_p1] == "#" or grid[down_of_p2] == "#":
                    return False

        raise Exception()

    def try_vertical_push(self, point_box_map, dir: Direction, grid) -> bool:
        if dir.icon == "^":
            up_of_p1 = Point(self.point_1.x, self.point_1.y - 1)  # type: ignore
            up_of_p2 = Point(self.point_2.x, self.point_2.y - 1)  # type: ignore
            box_up_p1 = point_box_map.get(up_of_p1)
            box_up_p2 = point_box_map.get(up_of_p2)

            if box_up_p1 or box_up_p2:
                if box_up_p1 == box_up_p2:
                    if box_up_p1.try_vertical_push(point_box_map, dir, grid):
                        point_box_map[self.point_1] = None
                        point_box_map[self.point_2] = None
                        grid[self.point_1] = "."
                        grid[self.point_2] = "."
                        self.point_1, self.point_2 = up_of_p1, up_of_p2
                        grid[self.point_1] = "["
                        grid[self.point_2] = "]"
                        point_box_map[up_of_p1] = self
                        point_box_map[up_of_p2] = self
                        return True
                else:
                    if all(
                        i.try_vertical_push(point_box_map, dir, grid)
                        for i in [box_up_p1, box_up_p2]
                        if i
                    ):
                        point_box_map[self.point_1] = None
                        point_box_map[self.point_2] = None
                        grid[self.point_1] = "."
                        grid[self.point_2] = "."
                        self.point_1, self.point_2 = up_of_p1, up_of_p2
                        grid[self.point_1] = "["
                        grid[self.point_2] = "]"
                        point_box_map[up_of_p1] = self
                        point_box_map[up_of_p2] = self
                        return True
                return False
            else:
                if grid[up_of_p1] == "." and grid[up_of_p2] == ".":
                    point_box_map[self.point_1] = None
                    point_box_map[self.point_2] = None
                    grid[self.point_1] = "."
                    grid[self.point_2] = "."
                    self.point_1, self.point_2 = up_of_p1, up_of_p2
                    grid[self.point_1] = "["
                    grid[self.point_2] = "]"
                    point_box_map[up_of_p1] = self
                    point_box_map[up_of_p2] = self
                    return True
                if grid[up_of_p1] == "#" or grid[up_of_p2] == "#":
                    return False

        if dir.icon == "v":
            down_of_p1 = Point(self.point_1.x, self.point_1.y + 1)  # type: ignore
            down_of_p2 = Point(self.point_2.x, self.point_2.y + 1)  # type: ignore
            box_down_p1 = point_box_map.get(down_of_p1)
            box_down_p2 = point_box_map.get(down_of_p2)

            if box_down_p1 or box_down_p2:
                if box_down_p1 == box_down_p2:
                    if box_down_p1.try_vertical_push(point_box_map, dir, grid):
                        point_box_map[self.point_1] = None
                        point_box_map[self.point_2] = None
                        grid[self.point_1] = "."
                        grid[self.point_2] = "."
                        self.point_1, self.point_2 = down_of_p1, down_of_p2
                        grid[self.point_1] = "["
                        grid[self.point_2] = "]"
                        point_box_map[down_of_p1] = self
                        point_box_map[down_of_p2] = self
                        return True
                else:
                    if all(
                        i.try_vertical_push(point_box_map, dir, grid)
                        for i in [box_down_p1, box_down_p2]
                        if i
                    ):
                        point_box_map[self.point_1] = None
                        point_box_map[self.point_2] = None
                        grid[self.point_1] = "."
                        grid[self.point_2] = "."
                        self.point_1, self.point_2 = down_of_p1, down_of_p2
                        grid[self.point_1] = "["
                        grid[self.point_2] = "]"
                        point_box_map[down_of_p1] = self
                        point_box_map[down_of_p2] = self
                        return True
                return False
            else:
                if grid[down_of_p1] == "." and grid[down_of_p2] == ".":
                    point_box_map[self.point_1] = None
                    point_box_map[self.point_2] = None
                    grid[self.point_1] = "."
                    grid[self.point_2] = "."
                    self.point_1, self.point_2 = down_of_p1, down_of_p2
                    grid[self.point_1] = "["
                    grid[self.point_2] = "]"
                    point_box_map[down_of_p1] = self
                    point_box_map[down_of_p2] = self
                    return True
                if grid[down_of_p1] == "#" or grid[down_of_p2] == "#":
                    return False

        # print(f"{grid[down_of_p1]=}, {grid[down_of_p2]=}")

        raise Exception()


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__, test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        # print(f"{len(self._input_data)=}")
        # print(f"{len(self._input_data[0])=}")
        # print(f"{len(self._input_data[1])=}")
        self.grid = Grid.from_input([self._input_data[0]])
        self.grid.display()
        self.__input_data = [Row(i) for i in self._input_data[1]]
        # for x in self.__input_data:
        #     print(f"{x}, {len(self.__input_data)}")

    def _calculate_1(self):
        return 0
        result = 0
        current_pos = self.grid.values["@"][0]
        print(current_pos)
        for x in self.__input_data:
            for i in x.processed:
                # print(i)
                c = Cursor(current_pos, Direction.from_symbol(i))
                # print(c, self.grid.grid[c.ahead()])
                if self.grid.grid[c.ahead()] == ".":
                    self.grid.grid[c.ahead()] = "@"
                    self.grid.grid[c.pos] = "."
                    current_pos = c.ahead()
                elif self.grid.grid[c.ahead()] == "O":
                    #
                    # prev = c.pos
                    while True:
                        n = c.all_ahead()
                        #
                        # print(n, c.ahead())
                        if self.grid.grid[n] == "#":
                            break
                        if self.grid.grid[n] == ".":
                            self.grid.grid[n] = "O"
                            self.grid.grid[c.ahead()] = "@"
                            self.grid.grid[c.pos] = "."
                            current_pos = c.ahead()
                            break
                        # prev = n

                    # c1 = Cursor(c.ahead(), c.dir)
                    #
                    #     self.grid.grid[c1.ahead()] = 'O'
                    #     # self.grid.grid[c1.pos] = '.'
                    #     self.grid.grid[c.ahead()] = '@'
                    #     self.grid.grid[c.pos] = '.'
                    #     current_pos = c.ahead()
                # self.grid.display()
                # input()

        self.grid.display()
        self.grid.recalculate_values()
        result = 0
        for i in self.grid.values["O"]:
            # print(i, (i.y+1)*100+(i.x+1))
            result += (i.y) * 100 + (i.x)
            # print(result)

        return result

    def _calculate_2(self):  # 1442890 too low
        result = 0
        new_grid = []
        boxes = {}
        box_n = 0
        point_box_map = {}
        for i in self._input_data[0]:
            t = []
            for x in i:
                if x == "@":
                    t.append("@.")
                elif x == "O":
                    t.append("[]")
                    boxes[box_n] = Box(box_n)
                    box_n += 1
                else:
                    t.append(2 * x)
            new_grid.append("".join(t))

        self.grid = Grid.from_input([new_grid])
        self.grid.display()
        # print(box_n)

        for c, box in enumerate(self.grid.values["["]):
            # print(c, box)
            # print(boxes[c])
            boxes[c].point_1 = box
            boxes[c].point_2 = Point(box.x + 1, box.y)
            point_box_map[boxes[c].point_1] = boxes[c]
            point_box_map[boxes[c].point_2] = boxes[c]
        # print(f"{boxes=}")
        # print(f"{len(point_box_map)=}")
        # return

        current_pos = self.grid.values["@"][0]
        # print(f"{current_pos=}")
        # return
        cc = 0
        for x in self.__input_data:
            for i in x.processed:
                # print(f"{i=}")
                cc += 1
                # input()

                c = Cursor(current_pos, Direction.from_symbol(i))
                # print(c, self.grid.grid[c.ahead()])
                # print(f"{id(self.grid.grid)=}")
                # return
                if c.dir.icon in ("<", ">"):
                    # orizontal move. only look haead
                    # print("orizontal move. only look haead")
                    if self.grid.grid[c.ahead()] == ".":
                        # all good
                        self.grid.grid[c.ahead()] = "@"
                        self.grid.grid[c.pos] = "."
                        current_pos = c.ahead()
                    # continue
                    elif self.grid.grid[c.ahead()] in ["[", "]"]:
                        box_ahead = point_box_map[c.ahead()]
                        rez = box_ahead.try_orizontal_push(
                            point_box_map,
                            c.dir,
                            self.grid.grid,
                        )
                        if rez:
                            self.grid.grid[c.ahead()] = "@"
                            self.grid.grid[c.pos] = "."
                            # point_box_map[c.pos] = None
                            current_pos = c.ahead()
                        # self.grid.display()
                        # print('here')
                if c.dir.icon in ("v", "^"):
                    # print("vertical move.")
                    if self.grid.grid[c.ahead()] == ".":
                        # all good
                        self.grid.grid[c.ahead()] = "@"
                        self.grid.grid[c.pos] = "."
                        current_pos = c.ahead()
                    # else:
                    #     print(c.ahead())
                    #     print(self.grid.grid[c.ahead()])
                    elif self.grid.grid[c.ahead()] in ["[", "]"]:
                        box_ahead = point_box_map[c.ahead()]
                        if box_ahead.check_vertical_push(
                            point_box_map,
                            c.dir,
                            self.grid.grid,
                        ):
                            rez = box_ahead.try_vertical_push(
                                point_box_map,
                                c.dir,
                                self.grid.grid,
                            )
                            # if rez:
                            self.grid.grid[c.ahead()] = "@"
                            self.grid.grid[c.pos] = "."
                            # point_box_map[c.pos] = None
                            current_pos = c.ahead()
                        # self.grid.display()
                        # print('here')
                        # # prev = c.pos
                        # while True:
                        #     n = c.all_ahead()

                        #     # print(n, c.ahead())
                        #     if self.grid.grid[n] == '#':
                        #     if self.grid.grid[n] == '.':
                        #         self.grid.grid[n] = 'O'
                        #         self.grid.grid[c.ahead()] = '@'
                        #         self.grid.grid[c.pos] = '.'
                        #         current_pos = c.ahead()
                        #         break
                        #     # prev = n

                    # c1 = Cursor(c.ahead(), c.dir)
                    #
                    #     self.grid.grid[c1.ahead()] = 'O'
                    #     # self.grid.grid[c1.pos] = '.'
                    #     self.grid.grid[c.ahead()] = '@'
                    #     self.grid.grid[c.pos] = '.'
                    #     current_pos = c.ahead()
                # self.grid.display()
                # time.sleep(.25)
                # input()
                boxes = {}
                box_n = 0
                point_box_map = {}
                self.grid.recalculate_values()
                for x in self.grid.grid.values():
                    # print(x)
                    if x == "[":
                        boxes[box_n] = Box(box_n)
                        box_n += 1
                for i, box in enumerate(self.grid.values["["]):
                    # print(c, box)
                    # print(boxes[c])
                    boxes[i].point_1 = box
                    boxes[i].point_2 = Point(box.x + 1, box.y)
                    point_box_map[boxes[i].point_1] = boxes[i]
                    point_box_map[boxes[i].point_2] = boxes[i]
                # print(f"{box_n=}")
                # print(f"{len(point_box_map)=}")
                #

        self.grid.display()
        self.grid.recalculate_values()
        result = 0
        for i in self.grid.values["["]:
            # print(i, (i.y+1)*100+(i.x+1))
            result += (i.y) * 100 + (i.x)
            # print(result)

        return result
