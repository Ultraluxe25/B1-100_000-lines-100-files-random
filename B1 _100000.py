# Работа выполнена Каптуровым Александром

import random
import datetime
from string import ascii_lowercase, ascii_uppercase


def generate_alphabet():
    return ascii_lowercase + ascii_uppercase


def generate_russian_alphabet():
    upper_case = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    return upper_case.lower() + upper_case


def get_random_alphabet_combination(alphabet):
    phrase = [alphabet()[random.randint(0, len(alphabet()) - 1)] for _ in range(10)]
    return "".join(phrase)


def file_creator():
    for name in range(1, 101):
        with open(f'{name}.txt', 'w', encoding='UTF-8') as file:
            for _ in range(100_000):
                message = list()
                message.append(get_random_alphabet_combination(generate_alphabet))
                message.append(get_random_alphabet_combination(generate_russian_alphabet))
                message = '||'.join(message)
                file.write(f'{message}\n')


file_creator()
# print(get_random_latin_combination())
# print(get_random_alphabet_combination(generate_russian_alphabet))
