"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3
Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
lst = input('Введите целые числа через пробел: ').split(' ')
if len(lst) % 2 == 0:
    r = len(lst)
else:
    r = len(lst) - 1
temp = 0
i = 0
while i < r:
    temp = lst[i]
    lst[i], lst[i + 1] = lst[i + 1], temp
    i += 2
print(lst)