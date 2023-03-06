"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv, re, os

def get_data(*args):
    for i in os.listdir(directory):
        files = os.path.join(directory, i)
        if os.path.isfile(files) and i.endswith('.txt'):
            file_obj = open(i, 'r', encoding='utf-8')
            data = file_obj.read()
            file_obj.close()
            temp = []
            os_prod_reg = re.compile(r'Изготовитель системы: \s*\S*')
            os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
            os_prod_reg = re.compile(r'Название ОС: \s*\S*\s*\S*\s*\S*\s*\S*')
            temp.append(os_prod_reg.findall(data)[0].split()[3])
            temp.append(os_prod_reg.findall(data)[0].split()[4])
            str_temp = ' '.join(temp)
            os_name_list.append(str_temp)
            os_prod_reg = re.compile(r'Код продукта: \s*\S*')
            os_code_list.append(os_prod_reg.findall(data)[0].split()[2])
            os_prod_reg = re.compile(r'Тип системы: \s*\S*')
            os_type_list.append(os_prod_reg.findall(data)[0].split()[2])
    print(header, os_prod_list, os_name_list, os_code_list, os_type_list)
    main_data.insert(0, header)
    return (os_prod_list, os_name_list, os_code_list, os_type_list, main_data)

def write_to_csv(main_data, final_file, j = 0):
    for i in range(3):
        lst = [j + 1]
        main_data.append(lst)
        main_data[i + 1].append(os_prod_list[j])
        main_data[i + 1].append(os_name_list[j])
        main_data[i + 1].append(os_code_list[j])
        main_data[i + 1].append(os_type_list[j])
        j += 1
        print(main_data)
    print(f'2 {main_data}')

    with open(final_file, 'w', encoding='utf-8') as out_f:
        f_writer = csv.writer(out_f)
        for i in main_data:
            f_writer.writerow(i)


os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
main_data = []
directory = 'E:/GeekBrains Сетевой инженер/Пакет разработчик/Пакет - Программист/Знакомство с языком Python' \
                '/python_study/8semDZ/task_1'
final_file = 'E:/GeekBrains Сетевой инженер/Пакет разработчик/Пакет - Программист/Знакомство с языком Python' \
                '/python_study/8semDZ/task_1/data_report.csv'
get_data(os_prod_list, os_name_list, os_code_list, os_type_list, main_data, header, directory)
print(f'1 {main_data}')
write_to_csv(main_data, final_file)