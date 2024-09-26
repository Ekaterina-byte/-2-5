#Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

L = lambda first, second: True if first == second else False
print(list(map(L, first, second)))

#Замыкание
from pprint import pprint


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__
from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        words = choice(self.words)
        return words

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())