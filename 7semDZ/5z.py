"""
1) Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
 работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
  Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""
class My_Exception(Exception):
    def __init__(self, txt):
        self.txt = txt

def creation(nums, lst=None):
    if lst is None:
        lst = []
    if nums == 'stop':
        print(lst)
        return
    lst.append(nums)
    return creation(validation(input('Введите число или stop для завершения программы: ')), lst)

def validation(nums):
    if nums == 'stop':
        return nums
    try:
        try:
            nums = int(nums)
        except ValueError:
            raise My_Exception('Вы ввели не число! Введите число или stop для завершения программы: ')
    except My_Exception as err:
        return validation(input(err))
    else:
        return nums


nums = validation(input('Введите число: '))
(creation(nums))