# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open('output.txt',mode='w') as f:
    line='something'
    while line!='':
        line=input('[]: ')
        print(line,file=f)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('input.txt',mode='r') as f:
    file_analyse={}
    i,cnt=1,0
    for line in f:
        file_analyse[str(i)]=len(line.split())
        i+=1
print(file_analyse)

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('salary.txt',mode='r') as f:
    salary_dict={line.split()[0]:int(line.split()[1]) for line in f}
print('Меньше рынка: ',[i for i,j in salary_dict.items() if j<20000])
print('Средняя з/п: ', sum([j for i,j in salary_dict.items()])/len(salary_dict))

# 4. Поменять в файле английские числительные на русские, записать данные в новый файл.
with open('numbers.txt',mode='r') as f_in:
    with open('numbers_new.txt',mode='w') as f_out:
        num_dict={1:'Один',2:'Два',3:'Три',4:'Четыре'}
        for line in f_in:
            new_line=line.split()
            new_line[0]=num_dict.get(int(new_line[2]))
            print(' '.join(new_line),file=f_out)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('number_row.txt',mode='w') as f:
    print(' '.join(map(str,range(100))),file=f)
with open('number_row.txt',mode='r') as f:
    print('сумма чисел в файле',sum(map(int,f.read().split())))

# 6. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
import io
import re

with io.open('subjects.txt',encoding='utf-8',mode='r') as f:
    file_analyse={}
    for line in f:
        temp=line.split()
        file_analyse[temp[0]]=sum(map(int,re.findall('(\d+)',line)))
print(file_analyse)

# 7. Создать словарь с фирмами и их прибылями, а также словарь со средней прибылью, сохранить как json.
import json
with open('firms.txt',mode='r') as f:
    firm_analyse={}
    for line in f:
        temp=line.split()
        firm_analyse[temp[0]]=int(temp[2])-int(temp[3])
profit=[j for i,j in firm_analyse.items() if j>=0]
js_list=[firm_analyse,{'average_profit':sum(profit)/len(profit)}]
with open('firms_out.txt',mode='w') as f:
    json.dump(js_list,f)
