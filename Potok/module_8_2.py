def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i #сумма чисел
        except TypeError as exc:
            incorrect_data += 1 #кол-во нкорректных данных
            print(f'Некорректный тип данных для подсчета суммы {i} ')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        sum_, x = personal_sum(numbers)
        itog = sum_ / (len(numbers) - x)
        return itog
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных')
        if isinstance(numbers, int):
            return None




if __name__=="__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
