# Работа выполнена Каптуровым Александром

from random import randint, randrange
import datetime
from string import ascii_lowercase, ascii_uppercase


def generate_alphabet():
    return ascii_lowercase + ascii_uppercase


def generate_russian_alphabet():
    upper_case = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    return upper_case.lower() + upper_case


def get_random_alphabet_combination(alphabet):
    phrase = [alphabet()[randint(0, len(alphabet()) - 1)] for _ in range(10)]
    return "".join(phrase)


def get_integer_even_number_combination():
    return randrange(2, 100_000_000, 2)


def get_float_number_combination():
    return randint(100_000_000, 2_000_000_000) / 100_000_000


def files_creator():
    for name in range(1, 101):
        with open(f'{name}.txt', 'w', encoding='UTF-8') as file:
            for _ in range(100_000):
                message = list()
                message.append(get_random_alphabet_combination(generate_alphabet))
                message.append(get_random_alphabet_combination(generate_russian_alphabet))
                message.append(str(get_integer_even_number_combination()))
                message.append(str(get_float_number_combination()).replace('.', ','))
                result = '||'.join(message)
                file.write(f'{result}\n')


if __name__ == "__main__":
    files_creator()
    

# print(get_random_latin_combination())
# print(get_random_alphabet_combination(generate_russian_alphabet))
# print(get_float_number_combination())
