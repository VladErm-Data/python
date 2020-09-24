# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.
def num_division(num_1,num_2):
    try :
        return num_1 / num_2
    except ZeroDivisionError:
        return 'ZeroDivisionError'

num_1, num_2 = map(int,input('Введите 2 числа через пробел: ').split())
print(num_division(num_1,num_2))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
def print_udata(name,surname,birthday,city,email,phone_num):
    print(f'{surname} {name} {birthday} Город:{city} Мэйл:{email} Телефон:{phone_num}')

print_udata(email='sobaka@.mail.ru',city='Gorod',name='Evkakiy',surname='Zeleniy',phone_num='+72283221488', birthday='01.01.1900')

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(arg1,arg2,arg3):
    temp_arr=list([arg1,arg2,arg3])
    temp_arr.sort(reverse=True)
    return temp_arr[0]+temp_arr[1]

# 4. Возведение числа в степень
def power_func_operator(arg1,arg2):
    return arg1**arg2

def power_func_cycle(arg1,arg2):
    temp=1
    for i in range(1,abs(arg2)+1):
        temp*=arg1
    return 1/temp

num_1, num_2 = map(int,input('Введите 2 числа через пробел: ').split())
print('Возведение через оператор: ',power_func_operator(num_1,num_2))
print('Возведение через цикл: ',power_func_cycle(num_1,num_2))

# 5. Cумма чисел через пробел
def is_digit(char_num):
    """Проверка является ли строка числом"""
    try:
        float(char_num)
        return True
    except:
        return False

def number_sum(num_str):
    """Сумма чисел до первого символа не являющегося числом
        Возвращает False если строка содержит спецсимвол, иначе возвращает True
    """
    try:
        return True,sum(list(map(float, num_str.split())))
    except:
        temp_arr=num_str.split()
        i=0
        summ=0
        while is_digit(temp_arr[i]):
            summ+=float(temp_arr[i])
            i += 1
        return False,summ

cycle_cond=True
cur_sum=0
temp=0
while cycle_cond:
    cycle_cond,temp = number_sum(input('Введите числа через пробел: '))
    cur_sum+=temp
    print(cur_sum)

# 6. Превращаем слова в Слова С Заглавной Буквы
def int_func(word):
    word=word[0].upper()+word[1:]
    return word
in_str=input('Введите слова: ')
print(' '.join(list(map(int_func,in_str.split()))))
