"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ
{
    "orders": [
        {
            "item": "принтер",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}
вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
Исходный orders.json
{
    "orders": []
}
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        obj = json.load(f_n)
        obj.get("orders").append({'item': item,
                                  'quantity': quantity,
                                  'price': price,
                                  'buyer': buyer,
                                  'date': date})

    with open('orders.json', 'w') as f_m:
        json.dump(obj, f_m, sort_keys=True, indent=4)


write_order_to_json("printer", "10", "6700", "Ivanov I.I.", "24.09.2017")
write_order_to_json("scaner", "20", "5500", "Petrov P.P.", "11.01.2018")
write_order_to_json("PC", "30", "40000", "Sidorov A.V.", "21.04.2018")
write_order_to_json("Monitor", "30", "5000", "Fedorov D.K.", "31.02.2018")