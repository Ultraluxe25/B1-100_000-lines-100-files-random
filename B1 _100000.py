# Работа выполнена Каптуровым Александром

from random import randint, randrange
from datetime import datetime, timedelta
from string import ascii_lowercase, ascii_uppercase


def get_time():
    current_time = datetime.now() - timedelta(days=randint(1, 5 * 365))
    return str(current_time).replace('-', '.')[:10]


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


def paste_data_into_line(data):
    data.append(get_time())
    data.append(get_random_alphabet_combination(generate_alphabet))
    data.append(get_random_alphabet_combination(generate_russian_alphabet))
    data.append(str(get_integer_even_number_combination()))
    data.append(str(get_float_number_combination()).replace('.', ','))
    return data


def fulfill_file(file):
    for _ in range(100_000):
        message = []
        paste_data_into_line(message)
        result = '||'.join(message)
        file.write(f'{result}\n')


def files_creator() -> str:
    for name in range(1, 101):
        print(f'Заполняем данными файл {name}.txt')
        with open(f'{name}.txt', 'w', encoding='UTF-8') as file:
            fulfill_file(file)
    return 'All files are complete'


if __name__ == "__main__":
    files_creator()
