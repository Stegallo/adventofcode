from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        self.__input_data = self._input_data[0]
        self.grid = {}
        x = self.__input_data
        for c, i in enumerate(x):
            for d, j in enumerate(i):
                self.grid[(c, d)] = j
        self.max_w = len(x)
        self.max_h = len(x[0])

    def is_visible(self, i):
        if i[0] in [0, self.max_w - 1]:
            return True
        if i[1] in [0, self.max_h - 1]:
            return True

        # visible from Top
        visible_Top = True
        for j in range(0, i[0]):
            if self.grid[(j, i[1])] >= self.grid[(i)]:
                visible_Top = False

        # visible from Left
        visible_Left = True
        for j in range(0, i[1]):
            if self.grid[(i[0], j)] >= self.grid[(i)]:
                visible_Left = False

        # visible from Bottom
        visible_Bottom = True
        for j in range(i[0] + 1, self.max_h):
            if self.grid[(j, i[1])] >= self.grid[(i)]:
                visible_Bottom = False

        # visible from Right
        visible_Right = True
        for j in range(i[1] + 1, self.max_w):
            if self.grid[(i[0], j)] >= self.grid[(i)]:
                visible_Right = False

        is_visible = visible_Top or visible_Left or visible_Bottom or visible_Right
        return is_visible

    def viewing_score(self, i):
        if i[0] in [0, self.max_w - 1]:
            return 0
        if i[1] in [0, self.max_h - 1]:
            return 0

        # visible top
        score_Top = 0
        for j in range(i[0] - 1, -1, -1):
            score_Top += 1
            if self.grid[(j, i[1])] >= self.grid[i]:
                break

        # visible left
        score_Left = 0
        for j in range(i[1] - 1, -1, -1):
            score_Left += 1
            if self.grid[(i[0], j)] >= self.grid[(i)]:
                break

        # visible from Bottom
        score_Bottom = 0
        for j in range(i[0] + 1, self.max_h):
            score_Bottom += 1
            if self.grid[(j, i[1])] >= self.grid[i]:
                break

        # visible from Right
        score_Right = 0
        for j in range(i[1] + 1, self.max_w):
            score_Right += 1
            if self.grid[(i[0], j)] >= self.grid[(i)]:
                break

        return score_Top * score_Left * score_Bottom * score_Right

    def _calculate_1(self):
        x = self.__input_data

        t = 0
        for i in self.grid:
            if self.is_visible(i):
                t += 1
        return t

    def _calculate_2(self):
        x = self.__input_data
        t = 0
        for i in self.grid:
            x = self.viewing_score(i)
            if x > t:
                t = x
        return t
