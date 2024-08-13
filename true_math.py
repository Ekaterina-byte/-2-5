from math import inf
def divide(fisrt, second):
    try:
        result = fisrt / second
    except ZeroDivisionError:
        result = inf

    if result != 0:
        print(f"Результат деления - {result}")
    else:
        return inf

