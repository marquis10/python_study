"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def result(n):
    if n == 1:
        return 1
    else:
        return n + result(n - 1)


n = int(input('Введите любое натуральное число: '))
temp = n + 1
sum2 = n * temp / 2
if result(n) == sum2:
    print(f'Для n = {n}\nВыполняется равенство 1 + 2 + 3 + ... + n = n (n + 1) / 2\n{result(n)} = {sum2}')
else:
    print(f'Для n = {n}\nНе выполняется равенство 1 + 2 + 3 + ... + n = n (n + 1) / 2\n{result(n)} = {sum2}')