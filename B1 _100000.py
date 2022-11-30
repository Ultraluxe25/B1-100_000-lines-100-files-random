# Работа выполнена Каптуровым Александром

import random
import datetime
from string import ascii_lowercase, ascii_uppercase


def generate_alphabet():
    return ascii_lowercase + ascii_uppercase


def get_random_latin_combination():
    phrase = [generate_alphabet()[random.randint(0, len(generate_alphabet()) - 1)] for _ in range(10)]
    return "".join(phrase)


def file_creator():
    for name in range(1, 101):
        with open(f'{name}.txt', 'w') as file:
            for _ in range(100_000):
                message = get_random_latin_combination()
                file.write(f'{message}\n')


file_creator()
# print(get_random_latin_combination())
