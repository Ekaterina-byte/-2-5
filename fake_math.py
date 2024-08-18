def divide(fisrt, second):
    try:
        result = fisrt / second
    except ZeroDivisionError:
        result = 0

    if second != 0:
        print(f"Результат деления - {result}")
    else:
        print("Результат деления - 'Ошибка'")

