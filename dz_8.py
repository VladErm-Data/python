# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В нем 2 метода: 1 извлекает число месяц и год, 2 - валидирует полученные данные.
CALENDAR_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


class Data:
    def __init__(self, r_str):
        self.input_ = r_str

    @classmethod
    def get_data_attr(cls, input_):
        params = dict(zip(['day', 'month', 'year'], [int(i) for i in input_.split('-')]))
        return params

    @staticmethod
    def validate_attrs(params):
        if 0 < params['month'] < 13:
            if (0 < params['day'] < CALENDAR_DAYS[params['month']]) or (params['year'] % 4 == 0 and params['month'] == 2
                                                                        and params['day'] == 29):
                return True
        return False


ex1 = Data('40-05-2020')
print(Data.get_data_attr(ex1.input_))
print(Data.validate_attrs(ex1.get_data_attr(ex1.input_)))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise OwnError("Делитель не может быть 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваш делитель: {inp_data}")

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.


class NotIntError(Exception):
    def __init__(self, text):
        self.text = text


def is_num(inp):
    try:
        int(inp)
    except ValueError:
        return False
    return True


res_list = []
in_str = ''
while True:
    in_str = input('element: ')
    if in_str == 'stop':
        break
    try:
        if is_num(in_str):
            res_list.append(int(in_str))
        else:
            raise NotIntError('Вы ввели некорректные данные')
    except NotIntError as err:
        print(err)

print(res_list)

# 4, 5, 6. Склад оргтехники


class Storage:
    def __init__(self, types, cnt):
        self.tech = dict(zip(types, cnt))

    def get_new_tech(self, type_, cnt):
        try:
            int(cnt)
        except ValueError:
            return 'Введено некорректное количество'

        if type_ in self.tech.keys():
            self.tech[type_] = self.tech[type_] + cnt
        else:
            self.tech[type_] = cnt
        return f'Теперь на складе {self.tech[type_]} единиц {type_}'

    def loss_tech(self, type_, cnt):
        try:
            int(cnt)
        except ValueError:
            return 'Введено некорректное количество'

        if self.tech[type_] - cnt > 0:
            self.tech[type_] = self.tech[type_] - cnt
            return f'Теперь на складе {self.tech[type_]} единиц {type_}'
        elif self.tech[type_] - cnt == 0:
            self.tech.pop(type_)
            return f'На складе закончилась техника {type_}'
        else:
            return 'На складе нет столько техники'


class OrgTech:
    def __init__(self, mass, height):
        self.mass = mass
        self.height = height
        self.is_broken = False

    def get_break(self):
        self.is_broken = True


class Printer(OrgTech):
    def __init__(self, mass, height, pages):
        super().__init__(mass, height)
        self.pages = pages


class Scanner(OrgTech):
    def __init__(self, mass, height, width):
        super().__init__(mass, height)
        self.width = width


class Xerox(OrgTech):
    def __init__(self, mass, height, dpi):
        super().__init__(mass, height)
        self.dpi = dpi


stor_1 = Storage(['Принтер', 'Сканер'], [3, 2])
stor_1.get_new_tech('Сканер', 2)
print(stor_1.loss_tech('Сканер', 4))

# 7. Реализовать проект «Операции с комплексными числами».


class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y > 0:
            return f'{self.x}+{self.y}i'
        else:
            return f'{self.x}{self.y}i'

    def __add__(self, other):
        return ComplexNum(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return ComplexNum(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)


a = ComplexNum(3, 2)
b = ComplexNum(4, -7)
print(a + b)
print(a * b)