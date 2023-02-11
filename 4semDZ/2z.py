"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""
def multupliers(n):
    i = 2
    lst = []
    while i <= n:
        if n % i == 0:
            lst.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return lst

n = int(input('Введите число: '))
print(multupliers(n))