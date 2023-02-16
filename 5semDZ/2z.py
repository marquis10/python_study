"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
nums = input('Введите натуральное число: ')
num = int(nums)
count1 = 0
count2 = 0
temp = 0

def division(num, nums, temp, count1, count2):
    if temp >= len(nums):
        return count1, count2
    else:
        n = num % 10
        num = num // 10
        temp += 1

        if n % 2 == 0:
            count1 += 1
        else:
            count2 += 1

    return division(num, nums, temp, count1, count2)


print(f'Количество чётных и нечётных цифр в числе {num} = {division(num, nums, temp, count1, count2)}')