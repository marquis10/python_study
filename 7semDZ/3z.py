"""
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker:
    def __init__(self, position, name, surname, wage, bonus):
        self.position = position
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f'{self.position}, {self.name}, {self.surname}, {self._income.get("wage")}, {self._income.get("bonus")}'


Personal_1 = Position('Инженер', 'Александр', 'Кузьмин', 35000, 20000)
print(f'Через str: {Personal_1}. Полный доход = {Personal_1.get_total_income()}')
print(f'{Personal_1.position} - {Personal_1.get_full_name()} - Полный доход = {Personal_1.get_total_income()}')

Personal_2 = Position('Программист', 'Василий', 'Васильев', 45000, 30000)
print(f'Через str: {Personal_2}. Полный доход = {Personal_2.get_total_income()}')
print(f'{Personal_2.position} - {Personal_2.get_full_name()} - Полный доход = {Personal_2.get_total_income()}')