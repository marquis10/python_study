"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
lst = ["разработка", "администрирование", "protocol", "standard"]
for i in lst:
    print(i)
    enc_str = i.encode("utf-8")
    print(f" {i} преобразовано в байтовое представление: {enc_str}")
    dec_str = enc_str.decode("utf-8")
    print(f" {i} преобразовано обратно в строковое представление: {dec_str}")