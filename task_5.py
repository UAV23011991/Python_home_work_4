# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

import random

def write_file(name,st):
    with open(name, 'w') as data:   # запись в файл
        data.write(st)

def rnd():
    return random.randint(0,101)    # создание случайного числа от 0 до 100

def create_mn(k):
    lst = [rnd() for i in range(k+1)]   # создание коэффициентов многочлена
    return lst
 
def create_str(sp): 
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2: # создание многочлена в виде строки
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k): # получение степени многочлена
        num = 1
    else:
        num = -1
    return num

def k_mn(k):
    if 'x' in k:
        i = k.find('x') 
        num = int(k[:i])    # получение коэффицента члена многочлена
    return num

def calc_mn(st):
    st = st[0].replace(' ', '').split('=')  # разбор многочлена и получение его коэффициентов
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1   # степень
    ii = l-1    # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst


k1 = int(input('Введите натуральную степень для первого многочлена k: '))   # создание двух файлов
k2 = int(input('Введите натуральную степень для второго многочлена k: '))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file('Файл для 1-го многочлена.txt', create_str(koef1))
write_file('Файл для 2-го многочлена.txt', create_str(koef2))


with open('Файл для 1-го многочлена.txt', 'r') as data: # нахождение суммы многочлена
    st1 = data.readlines()
with open('Файл для 2-го многочлена.txt', 'r') as data:
    st2 = data.readlines()
print(f'Первый многочлен: {st1}.')
print(f'Второй многочлен: {st2}.')
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file('Файл с результатом.txt', create_str(lst_new))
with open('Файл с результатом.txt', 'r') as data:
    st3 = data.readlines()
print(f'Результирующий многочлен: {st3}.')
