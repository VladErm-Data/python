# 1. Работа с переменными
f_var=0
s_var=5
print('Первая переменная: ', f_var, '\nВторая переменная: ',s_var)
user_int=input('Введите число:')
user_str=input('Введите строку:')
print('Число: ',user_int,'\nСтрока: ', user_str)

# 2. Время в секундах -> 'hh:mm:ss'
user_time=int(input('Введите время в секундах: '))
if user_time<0:
    print('Неверное число.')
else:
    print('{:0>2}:{:0>2}:{:0>2}'.format(user_time//3600,user_time//60%60,user_time%60))

# 3. n+nn+nnn
print()
n=int(input('Введите n: '))
print('n+nn+nnn: ', n*123)

# 4. Самая большая цифра
num=int(input('Введите число: '))
temp=0
while num>0:
    if num%10>temp:
        temp=num%10
    num=num//10
print('Самая большая цифра: ',temp)

# 5. Фирма
revenue=int(input('ВВедите прибыль: '))
costs=int(input('ВВедите издержки: '))
if costs<revenue:
    print('Фирма в прибыли на {:.2%}'.format(revenue/costs -1))
    emp_cnt = int(input('ВВедите кол-во сотрудников: '))
    print('Прибыль на сотрудника составила {:.2}'.format((revenue-costs)/emp_cnt))
elif costs>revenue:
    print('Фирма в убытке')
else:
    print('Фирма в равновесии')

# 6. Спортсмен
a=float(input('Введите а: '))
b=float(input('Введите b: '))
i=1
while a<b:
   a=a*1.1
   i+=1
print('Спортсмен достиг результата на %d день' % i)
=======
# 1. Работа с переменными
f_var=0
s_var=5
print('Первая переменная: ', f_var, '\nВторая переменная: ',s_var)
user_int=input('Введите число:')
user_str=input('Введите строку:')
print('Число: ',user_int,'\nСтрока: ', user_str)

# 2. Время в секундах -> 'hh:mm:ss'
user_time=int(input('Введите время в секундах: '))
if user_time<0:
    print('Неверное число.')
else:
    print('{:0>2}:{:0>2}:{:0>2}'.format(user_time//3600,user_time//60%60,user_time%60))

# 3. n+nn+nnn
print()
n=int(input('Введите n: '))
print('n+nn+nnn: ', n*123)

# 4. Самая большая цифра
num=int(input('Введите число: '))
temp=0
while num>0:
    if num%10>temp:
        temp=num%10
    num=num//10
print('Самая большая цифра: ',temp)

# 5. Фирма
revenue=int(input('ВВедите прибыль: '))
costs=int(input('ВВедите издержки: '))
if costs<revenue:
    print('Фирма в прибыли на {:.2%}'.format(revenue/costs -1))
    emp_cnt = int(input('ВВедите кол-во сотрудников: '))
    print('Прибыль на сотрудника составила {:.2}'.format((revenue-costs)/emp_cnt))
elif costs>revenue:
    print('Фирма в убытке')
else:
    print('Фирма в равновесии')

# 6. Спортсмен
a=float(input('Введите а: '))
b=float(input('Введите b: '))
i=1
while a<b:
   a=a*1.1
   i+=1
print('Спортсмен достиг результата на %d день' % i)
>>>>>>> Stashed changes
