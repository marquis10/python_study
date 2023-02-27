"""
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""

class Road:
    weight = 25
    thickness = 0.05

    def __init__(self, *args):
        self.lst = []
        for el in args:
            self.lst.append(el)
        self._length = self.lst[0]
        self._width = self.lst[1]

    def weight_asphalt(self):
        return int(self._length * self._width * self.weight * self.thickness)

    def __getitem__(self, item):
        return self.lst[item]

asphalt = Road(5000, 20)
print(f'Масса асфальта = {asphalt[1]}м * {asphalt[0]}м * {Road.weight}кг * {Road.thickness}м = '
      f'{asphalt.weight_asphalt()}кг = {int(asphalt.weight_asphalt()/1000)}т')