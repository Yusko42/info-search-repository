import sys
import argparse
from pathlib import Path


ALPHABETS = {
    "ru": ("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
           "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),  # 33, с ё
    "en": ("abcdefghijklmnopqrstuvwxyz",
           "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
}

def caesar(text: str, shift: int, lang: str) -> str:
    if lang not in ALPHABETS:
        raise ValueError(f"Ошибка: словарь для языка {lang} не обнаружен.")

    alphabet_lower, alphabet_upper = ALPHABETS[lang]

    dict_len = len(alphabet_lower)
    shift %= dict_len

    # Создадим исходный и сдвинутый словари
    full_dict = alphabet_lower + alphabet_upper
    shifted_dict = alphabet_lower[shift:] + alphabet_lower[:shift] \
                + alphabet_upper[shift:] + alphabet_upper[:shift]
    
    # Создадим далее таблицу соответствия символов
    table = str.maketrans(full_dict, shifted_dict)  

    # Применяем таблицу к тексту
    return text.translate(table)


def parse_args():
    p = argparse.ArgumentParser(description="Шифр Цезаря")
    p.add_argument("-i", "--input", required=True, type=Path, 
                   help="путь к исходному файлу")
    p.add_argument("-s", "--shift", required=True, type=int, 
                   help="сдвиг (целое число)")
    p.add_argument("-l", "--lang", required=True, choices=["ru", "en"], 
                   help="язык текста")
    p.add_argument("-o", "--output", type=Path, 
                   help="путь к результату")
    return p.parse_args()

def main():
    print("=== Шифр Цезаря ===")

    args = parse_args()

    src = args.input
    shift = args.shift
    lang = args.lang

    if not src.is_file():
        sys.exit(f"Ошибка: файл не найден: {src}")

    dst = args.output if args.output is not None else Path("./result.txt")

    text = src.read_text(encoding="utf-8")
    dst.write_text(caesar(text, shift, lang), encoding="utf-8")
    print(f"Результат в файле: {dst}")
    

if __name__ == '__main__':
    main()