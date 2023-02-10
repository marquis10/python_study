"""
4. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
n = int(input('Сколько товаров будет в списке? -  '))
lst = input('Введите через запятую характеристики товара: ').split(',')
names, prise, count, units = lst
product_lst = []
product_tpl = []
products = []
param = dict()
temp = []
lst1 = []
lst2 = []
lst3 = []
lst4 = []
for i in range(n):
    for j in range(len(lst)):
        param[lst[j]] = input(f'Введите {lst[j]} {i + 1} товара: ')
    product_lst.append(i + 1)
    product_lst.append(param.copy())
    product_lst = tuple(product_lst)
    product_tpl.append(product_lst)
    products.append(product_tpl[0])
    param.clear()
    product_tpl.clear()
    product_lst = list(product_lst)
    product_lst.clear()
print(f'Структура данных "Товары": {products}')
print('Собранная аналитика о товарах')
for j in range(n):
    product_tpl = products[j]
    product_tpl = list(product_tpl)
    product_lst = product_tpl[1]
    a = product_lst['название']
    b = product_lst['цена']
    c = product_lst['количество']
    d = product_lst['ед']
    lst1.append(a)
    lst2.append(b)
    lst3.append(c)
    lst4.append(d)
param[names] = lst1
param[prise] = lst2
param[count] = lst3
param[units] = lst4
print(param)