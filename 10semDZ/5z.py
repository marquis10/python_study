"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ARGS_YANDEX = ['ping', 'yandex.ru']

YA_PING = subprocess.Popen(ARGS_YANDEX, stdout=subprocess.PIPE)

for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

ARGS_YOUTUBE = ['ping', 'youtube.com']
YOUTUBE_PING = subprocess.Popen(ARGS_YOUTUBE, stdout=subprocess.PIPE)

for line in YOUTUBE_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))