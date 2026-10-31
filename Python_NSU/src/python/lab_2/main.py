import re
import sys


def is_correct(input_sequence: str) -> bool:
    parenthesis_difference = 0
    for parenthesis in input_sequence:
        if (parenthesis=='('):
            parenthesis_difference += 1
        elif (parenthesis==')'):
            parenthesis_difference -= 1
        if parenthesis_difference < 0:
            return False
    
    return (parenthesis_difference == 0)

def parse_args() -> str:
    arg = sys.argv[1]
    try:
        with open(arg, encoding='utf-8') as file:
            return file.read().strip()
    except OSError:
        print("Введённый аргумент не распознан как корректный путь. " \
            "Аргумент будет разобран как скобочная последовательность.")
        return arg

def parse_from_console() -> str | None:
    while True:
        try:
            input_sequence = input("Введите скобочную последовательность: ")
        except (EOFError, KeyboardInterrupt):
            print("\nВвод прерван.")
            return None
        if not input_sequence.strip():
            print("Ошибка: пустой ввод.")
            continue
        if not re.fullmatch(r'[()]+', input_sequence):
            print("Ошибка: строка содержит лишние символы. \n" \
            "Пожалуйста, введите скобочную последовательность без лишних символов.")
            continue
        return input_sequence

def main():
    # Заголовок
    print("===   Проверка скобочной последовательности   ===")

    if len(sys.argv) > 1:
        input_sequence = parse_args()

    else:
        input_sequence = parse_from_console()
        if input_sequence is None: 
            return None
        
    print("Правильная последовательность" if is_correct(input_sequence) 
          else "Неправильная последовательность")

if __name__ == '__main__':
    main()