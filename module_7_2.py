'''Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.'''


def custom_write(file_name, strings):
    string_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    new_tuple = enumerate(strings, start=1)
    for text, string in new_tuple:
        byte = file.tell()
        file.write(string + '\n')
        string_position[(text, byte)]=string
    return string_position




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)