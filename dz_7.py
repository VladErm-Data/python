# 1. Реализовать матрицы
# Перегрузка __init__ : принимает список списков
# Перегрузка __add__: выполняет сложение матриц
# Перегрузка __str__: выводит матрицы в привычном виде.
from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, in_list):
        self.data = in_list

    def __str__(self):
        res_str = ''
        for i in self.data:
            for j in i:
                res_str += str(j) + '\t'
            res_str += '\n'
        return res_str

    def __add__(self, other):
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            res_list = [[self.data[i][j]+other.data[i][j] for j in range(len(self.data[0]))]
                        for i in range(len(self.data))]
            return Matrix(res_list)
        else:
            return 'Сложение невозможно'


my_list = [[1, 2, 3, 4], [5, 26, 7, 8]]
add_list = [[12, 13, 14, 16], [0, 0, 0, 0]]
a = Matrix(my_list)
b = Matrix(add_list)
print(a+b)

# 2. Для пальто и костюма реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора
# @property.


class Clothes(ABC):
    @abstractmethod
    def __init__(self, par):
        pass

    @abstractmethod
    def get_cloth_square(self):
        pass


class Suit(Clothes):
    def __init__(self, par):
        self.H = par

    @property
    def get_cloth_square(self):
        return 2 * self.H + 0.3


class Coat(Clothes):
    def __init__(self, par):
        self.V = par

    @property
    def get_cloth_square(self):
        return self.V/6.5 + 0.5


ex_1 = Coat(113)
ex_2 = Suit(182)
print(ex_1.get_cloth_square, ex_2.get_cloth_square)

# 3. Программа работы с органическими клетками


class CellInitError(Exception):
    def __init__(self, cells, message='Количество клеток меньше или равно 0'):
        self.cells = cells
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.cells} -> {self.message}'


class CellSubError(Exception):
    def __init__(self, message='Вычитание создает отрицательную клетку'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class Cell:
    def __init__(self, par):
        if par <= 0:
            raise CellInitError(par)
        else:
            self.cells = par

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            raise CellSubError

    def __mul__(self, other):
        return Cell(self.cells*other.cells)

    def __truediv__(self, other):
        return Cell(round(self.cells/other.cells))

    def make_order(self, n):
        res_str = list('*' * self.cells + '*' * (self.cells // n))
        for i in range(self.cells // n):
            res_str[(i + 1) * n + i] = '\n'
        return ''.join(res_str)


cell_1 = Cell(6)
cell_2 = Cell(10)

print(cell_1/cell_2)
print(cell_2.make_order(4))
