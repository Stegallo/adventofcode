from .common import AoCDay


class Day(AoCDay):
    def __init__(self, test=0):
        super().__init__(__name__.split(".")[1].replace("day", ""), test)

    def _preprocess_input(self):
        # self.__input_data = [[int(i) for i in chunk] for chunk in self._input_data]
        # print(f"{self._input_data=}")
        self.__input_data = self._input_data[0]
        self.grid = {}
        # print(f"{x=}")
        x = self.__input_data
        for c, i in enumerate(x):
            # print(i)
            for d, j in enumerate(i):
                self.grid[(c, d)] = j
        self.max_w = len(x)
        self.max_h = len(x[0])
        # print(f"{self.max_w=}")
        # print(f"{self.max_h=}")
        # print(f"{self.grid=}")

    def is_visible(self, i):
        # return True
        if i[0] in [0, self.max_w - 1]:
            return True
        if i[1] in [0, self.max_h - 1]:
            return True
        # visible from Top
        # print(f"{i},{self.grid[(i)]}")
        visible_Top = True
        for j in range(0, i[0]):
            # print(f"vado in range {(0, i[0])}; {i=}, {self.grid[(j, i[1])]=}, {self.grid[(i)]}")
            if self.grid[(j, i[1])] >= self.grid[(i)]:
                visible_Top = False

        # visible from Left
        visible_Left = True
        for j in range(0, i[1]):
            #     # print(f"{i}, {(i[1], j)=},{self.grid[(i[1], j)]=}, {self.grid[(i)]}")
            if self.grid[(i[0], j)] >= self.grid[(i)]:
                visible_Left = False

        # visible from Bottom
        visible_Bottom = True
        for j in range(i[0] + 1, self.max_h):
            # print(f"vado in range {(i[0]+1, self.max_h)}; {i=}, {self.grid[(j, i[1])]=}, {self.grid[(i)]}")
            if self.grid[(j, i[1])] >= self.grid[(i)]:
                visible_Bottom = False

        # visible from Right
        visible_Right = True
        for j in range(i[1] + 1, self.max_w):
            # print(f"{i}, {(i[1], j)=},{self.grid[(i[1], j)]=}, {self.grid[(i)]}")
            if self.grid[(i[0], j)] >= self.grid[(i)]:
                visible_Right = False
        # for j in []
        # return visible_Bottom
        is_visible = visible_Top or visible_Left or visible_Bottom or visible_Right
        # print(is_visible)
        return is_visible
        # return False

    def viewing_score(self, i):
        if i[0] in [0, self.max_w - 1]:
            return 0
        if i[1] in [0, self.max_h - 1]:
            return 0
        print(f"{i=}, {self.grid[(i)]}")

        score_Top = 0
        for j in range(0, i[0]):
            print(f"{j=}")
            if i in [(1, 2), (3, 2)]:
                # print(
                #     f"{i}vado in range {(0, i[0])}; {i=}, {self.grid[(j, i[1])]=}, {self.grid[(i)]}"
                # )
                ...
                # breakpoint()
            if self.grid[(j, i[1])] >= self.grid[(i)]:
                score_Top += 1
                break
            else:
                score_Top += 1
            #     break
        # if score_Top > 1:
        #     score_Top -= 1
        print(f"{score_Top=}")

        score_Left = 0
        for j in range(0, i[1]):
            print(f"{j=}")
            #     #     # print(f"{i}, {(i[1], j)=},{self.grid[(i[1], j)]=}, {self.grid[(i)]}")
            if self.grid[(i[0], i[1] - 1 - j)] >= self.grid[(i)]:
                score_Left += 1
                break
            else:
                score_Left += 1
        #         break
        # if score_Left > 1:
        #     score_Left -= 1
        print(f"{score_Left=}")

        # visible from Bottom
        score_Bottom = 1
        for j in range(i[0] + 1, self.max_h):
            print(f"{j=}")
            #     # print(
            #     #     f"vado in range {(i[0]+1, self.max_h)}; {i=}, {self.grid[(j, i[1])]=}, {self.grid[(i)]}"
            #     # )
            if self.grid[(j, i[1])] >= self.grid[(i)]:
                score_Bottom += 1
                break
            else:
                score_Bottom += 1

        #         break
        # if score_Bottom > 1:
        #     score_Bottom -= 1
        print(f"{score_Bottom=}")

        # visible from Right
        score_Right = 1
        for j in range(i[1] + 1, self.max_w):
            print(f"{j=}")
            #     # print(f"{i}, {(i[1], j)=},{self.grid[(i[1], j)]=}, {self.grid[(i)]}")
            if self.grid[(i[0], j)] >= self.grid[(i)]:
                score_Right += 1
                break
            else:
                score_Right += 1
        #     else:
        #         break
        # if score_Right > 1:
        #     score_Right -= 1
        print(f"{score_Right=}")

        print(score_Top, score_Left, score_Bottom, score_Right)
        return score_Top * score_Left * score_Bottom * score_Right

    def _calculate_1(self):
        x = self.__input_data

        t = 0
        for i in self.grid:
            # print(f"{i}, {self.grid[(i)]}, {self.is_visible(i)=}\n")
            if self.is_visible(i):
                t += 1
        return t

    def _calculate_2(self):
        x = self.__input_data
        # print(f"{x=}")
        t = 0
        for i in self.grid:
            x = self.viewing_score(i)
            # print(f"{i}, {self.grid[(i)]}, {x=}\n")
            if x > t:
                t = x
        return t
