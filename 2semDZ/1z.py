"""
Задание 1.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = int(input('Введите сколько км пробежал спортсмен в 1 день: '))
b = int(input('Введите необходимый результат: '))
day = 1
print(f'{day} день: {a} км')
while a <= b:
    a = round(a * 1.1, 2)
    day += 1
    print(f'{day} день: {a} км')
print(f'Ответ: на {day} день спортсмен достиг результата - не менее {b} км')