# 1. Создание списка
my_list=['hi',[1,2,3],228,True,(1,2,3),{'1':2}]
for i in my_list:
    print(i,type(i))

# 2. Обмен элементов списка
user_list=list(input('Введите список элементов через пробел:').split())
temp=0
for i in range(len(user_list)):
    if i%2!=0:
        temp=user_list[i-1]
        user_list[i-1]=user_list[i]
        user_list[i]=temp
print(user_list)

# 3. Месяц -> время года
month_num=int(input('Введите номер месяца: '))
mon_list=['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
mon_dict={1:'зима',2:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',9:'осень',10:'осень',11:'осень',12:'зима'}
print('Список: ',mon_list[month_num-1])
print('Словарь: ',mon_dict.get(month_num))

# 4. Вывод слов
user_str=input('Введите строку: ')
temp_list=user_str.split()
for i in range(len(temp_list)):
    print(i+1,' ',temp_list[i][:10])

# 5. Рейтинг
reit = [7, 5, 3, 3, 2]
temp=int(input('Введите элемент: '))
reit.sort(reverse=True)
for i in reit:
    if i<=temp:
        reit.insert(reit.index(i),temp)
        break
    elif reit.index(i)+1==len(reit):
        reit.append(temp)
        break
print(reit)

# 6. Товары
structure=[]
n=int(input('Кол-во элементов структуры: '))
temp_dict={'название': '', 'цена': 0, 'количество': 0, 'eд':''}
for i in range(n):
    temp_dict['название']=input('Название: ')
    temp_dict['цена'] = int(input('Цена: '))
    temp_dict['количество'] = int(input('Количество: '))
    temp_dict['eд'] = input('Ед.: ')
    structure.append(tuple([i+1,dict(temp_dict)]))

analyse={'название': list(set([i[1].get('название') for i in structure])),
         'цена': list(set([i[1].get('цена') for i in structure])),
         'количество': list(set([i[1].get('количество') for i in structure])),
         'eд':list(set([i[1].get('eд') for i in structure]))}
print('Анализ: ',analyse)
