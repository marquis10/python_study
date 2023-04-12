class DocMeta(type):
    """Метакласс, проверяющий наличие строк
    в документации в подконтрольном классе"""

    def __init__(self, clsname, bases, clsdict):
        # К моменту начала работы метода __init__ метакласса
        # словарь атрибутов контролируемого класса уже сформирован
        for key, value in clsdict.item():
            # пропустить специальные и частые методы
            if key.startswith('__'):
                continue

            # Пропустить любые не вызываемые объекты
            if not hasattr(value, "__call__"):
                continue

            # Проверить наличие строки документирования
            if not getattr(value, "__doc__"):
                # print(value)
                raise TypeError(f"Метод {key} должен иметь строку документации")

        type.__init__(self, clsname, bases, clsdict)

# Дочерний класс получает метакласс "в нагрузку" от родительского класса
class MyClass(metaclass=DocMeta):
    """Прикладной пользовательский класс"""

    def method_1(self):
        pass

    def method_2(self):
        print('Небольшая проблема')

mc = MyClass()
print(MyClass.__dict__)