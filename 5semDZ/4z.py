"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

def numbers(n, num = 1.0, summa = 1.0, i = 1):
    if i == n:
        return print(f'Количество элементов - {n}, их сумма = {summa}')
    else:
        if i % 2 != 0:
            num = num / 2
            summa = summa - num
        else:
            num = num / 2
            summa = summa + num
    return numbers(n, num, summa, i + 1)


n = int(input('Введите число элементов: '))
numbers(n)