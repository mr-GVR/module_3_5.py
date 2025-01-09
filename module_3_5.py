# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
    # Создайте переменную str_number и запишите строковое представление(str) числа number в нее
    str_number = str(number)

    # если длина строки равна 1, возвращаем цифру как число
    if len(str_number) == 1:
        return int(str_number) if int(str_number) != 0 else 1

    # Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ
    # из str_number в числовом представлении(int).
    first = int(str_number[0])

    # Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
    # Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    # Рекурсивно вычисляем произведение цифр оставшейся части числа
    return first * get_multiplied_digits(int(str_number[1:]))

# Пример 40203
result = get_multiplied_digits(40203)
print(result)  # Ожидается: 24
# Пример 402030
result2 = get_multiplied_digits(402030)
print(result2)  # Ожидается: 24