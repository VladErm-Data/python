# 1. Зарплата сотрудника
from sys import argv

def salary(work_time,mph,prize):
    return work_time*mph + prize

try:
    script_name, arg1, arg2, arg3 = argv
    print(salary(int(arg1),int(arg2),int(arg3)))
except :
    print('Запуск не из терминала')

# 2. элементы исходного списка, значения которых больше предыдущего элемента.

source_list= [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list=[source_list[i] for i in range(1,len(source_list)) if source_list[i]>source_list[i-1]]
print(res_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.

my_list=[i for i in range(20,241) if i%20==0 or i%21==0]
print(my_list)

# 4. Определить элементы списка, не имеющие повторений.

source_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_list=[el for el in source_list if source_list.count(el)==1]
print(res_list)

# 5. Результат вычисления произведения всех элементов списка.
from functools import reduce

source_list=[i for i in range(100,1001) if i%2==0]
print(reduce(lambda a,b:a*b,source_list))

# 6. а) итератор, генерирующий целые числа, начиная с указанного.
import itertools as it
def gen_nums(num, n):
    block=0
    for i in it.count(num):
        if block==n:
            break
        else:
            yield i
            block+=1

# 6. б) итератор, повторяющий элементы некоторого списка, определенного заранее.
def gen_cycle(source_list,n):
    block = 0
    for i in it.cycle(source_list):
        if block == n:
            break
        else:
            yield i
            block += 1

# 7. Генератор факториалов
import math
def fact(n):
    for i in range(1,n+1):
        yield math.factorial(i)

n=int(input('ВВедите число N: '))
for el in fact(n):
    print(el)