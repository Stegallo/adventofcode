from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]
        self.__grid = {}
        x = self.__input_data
        for c, i in enumerate(x):
            for d, j in enumerate(i):
                self.__grid[(c, d)] = j
        self.max_w = len(x)
        self.max_h = len(x[0])

    def is_visible(self, i):
        if i[0] in [0, self.max_w - 1]:
            return True
        if i[1] in [0, self.max_h - 1]:
            return True

        visible_Top = all(
            self.__grid[(j, i[1])] < self.__grid[(i)] for j in range(i[0])
        )
        visible_Left = all(
            self.__grid[(i[0], j)] < self.__grid[(i)] for j in range(i[1])
        )
        visible_Bottom = all(
            self.__grid[(j, i[1])] < self.__grid[(i)]
            for j in range(i[0] + 1, self.max_h)
        )
        visible_Right = all(
            self.__grid[(i[0], j)] < self.__grid[(i)]
            for j in range(i[1] + 1, self.max_w)
        )
        return visible_Top or visible_Left or visible_Bottom or visible_Right

    def viewing_score(self, i):
        if i[0] in [0, self.max_w - 1]:
            return 0
        if i[1] in [0, self.max_h - 1]:
            return 0

        # visible top
        score_Top = 0
        for j in range(i[0] - 1, -1, -1):
            score_Top += 1
            if self.__grid[(j, i[1])] >= self.__grid[i]:
                break

        # visible left
        score_Left = 0
        for j in range(i[1] - 1, -1, -1):
            score_Left += 1
            if self.__grid[(i[0], j)] >= self.__grid[(i)]:
                break

        # visible from Bottom
        score_Bottom = 0
        for j in range(i[0] + 1, self.max_h):
            score_Bottom += 1
            if self.__grid[(j, i[1])] >= self.__grid[i]:
                break

        # visible from Right
        score_Right = 0
        for j in range(i[1] + 1, self.max_w):
            score_Right += 1
            if self.__grid[(i[0], j)] >= self.__grid[(i)]:
                break

        return score_Top * score_Left * score_Bottom * score_Right

    def _calculate_1(self):
        return sum(bool(self.is_visible(i)) for i in self.__grid)

    def _calculate_2(self):
        t = 0
        for i in self.__grid:
            x = self.viewing_score(i)
            if x > t:
                t = x
        return t
