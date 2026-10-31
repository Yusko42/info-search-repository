import math


def binomialCoeff(n: int, m: int):
    return int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m)))


if __name__ == '__main__':
    # Заголовок
    print("===   Треугольник Паскаля   ===")

    # Обработка числа
    while True:
        input_number = input("Введите число: ")
        try:
            number = int(input_number)
        except ValueError:
            print("Ошибка: невозможно преобразовать введённое значение в целое число." \
            "\n Пожалуйста, введите целое положительное число.")
            continue
        if (number > 0):
            break
        else:
            print("Ошибка: число не является положительным."
            "\n Пожалуйста, введите целое положительное число.")

    # Вывод результата
    print(f"===  Результат (первые {number} строк) ===")
    for string_index in range(0, number):
        for number_index in range(0, string_index+1):
            print(binomialCoeff(string_index, number_index), end=" ")
        print("")