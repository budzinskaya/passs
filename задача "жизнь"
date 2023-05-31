import numpy as np
import time

from IPython.display import clear_output

class Life:
    def __init__(self, width=60, height=40, prob=0.3, time=0.1):
        self._prob = prob
        self._width = width
        self._height = height
        self._time = time

    def _initialize_field(self, randomly=True):
        if randomly:
            self._field = np.random.random((self._height, self._width)) < self._prob
        else:
            self._field = np.full((self._height, self._width), False)
            cx = self._width // 2
            cy = self._height // 2
            self._field[cy - 1, cx] = True
            self._field[cy - 1, cx + 1] = True
            self._field[cy, cx] = True
            self._field[cy, cx - 1] = True
            self._field[cy + 1, cx] = True
        
        # массив для подсчёта живых соседей с "рамкой"
        self._scores = np.zeros((self._height + 2, self._width + 2))

    def _one_step(self):
        self._scores.fill(0)
        # сместим field 8 раза в разных направлениях и прибавим к scores
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue

                self._scores[i: i + self._height, j: j + self._width] += self._field

        # мёртвые клетки с 3 живыми соседями
        condition1 = (~self._field) & (self._scores[1: self._height + 1, 1: self._width + 1] == 3)
        # живые клетки с 2 или 3 живими соседями
        condition2 = self._field & ((self._scores[1: self._height + 1, 1: self._width + 1] == 2) | (self._scores[1: self._height + 1, 1: self._width + 1] == 3))

        self._field = condition1 | condition2
        

    def _show_field(self):
        horizontal_line = u'\u2501'
        vertical_line = u'\u2503'
        top_left_corner = u'\u250F'
        top_right_corner = u'\u2513'
        bottom_left_corner = u'\u2517'
        bottom_right_corner = u'\u251B'

        result = top_left_corner + horizontal_line * self._width + top_right_corner + '\n'
        for i in range(self._height):
            result += vertical_line + ''.join('+' if x else ' ' for x in self._field[i]) + vertical_line + '\n'
        result += bottom_left_corner + horizontal_line * self._width + bottom_right_corner
        clear_output(wait=True)
        print(result)


    def run(self, randomly=True):
        self._initialize_field(randomly)
        while True: 
            self._show_field()
            time.sleep(self._time)
            self._one_step()
            
            
print("Введите через пробел ширину и высоту поля")
size = input().split()
width, height = int(size[0]), int(size[1])
print("Введите R, если хотите использовать в качестве начальной популяции R-pentomino (иначе любое другое значение)")
randomly = input() != "R"
if randomly:
    print("Введите вероятность появления жизни")
    prob = float(input())
    life = Life(width, height, prob)
else:
    life = Life(width, height)
life.run(randomly)
