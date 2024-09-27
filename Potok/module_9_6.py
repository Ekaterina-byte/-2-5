#Домашнее задание по теме "Генераторы"

"""Задача:

Напишите функцию-генератор all_variants(text),которая принимает строку text и
возвращает объект-генератор, при каждой итерации которого будет возвращаться
подпоследовательности переданной строки."""

def all_variants(text):
    l = len(text)
    for i in range(l):
        for j in range(l - i):
            yield text[j: i+j+1]

a = all_variants("abc")
for i in a:
    print(i)