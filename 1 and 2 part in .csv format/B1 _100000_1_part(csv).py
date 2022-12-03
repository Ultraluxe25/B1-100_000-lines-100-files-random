"""
Generate 100 text files with the following structure, each containing 100,000 lines
random date for the last 5 years || random set of 10 Latin characters ||
random set of 10 Russian characters || random positive even integer between 1 and 100,000,000 ||
random positive number with 8 decimal places in the range from 1 to 20

Output sample:
03.03.2015||ZAwRbpGUiK||мДМЮаНкуКД||14152932||7,87742021||
23.01.2015||vgHKThbgrP||ЛДКХысХшЗЦ||35085588||8,49822372||
17.10.2017||AuTVNvaGRB||мЧепрИецрА||34259646||17,7248118||
24.09.2014||ArIAASwOnE||ЧпЙМдШлыфУ||23252734||14,6239438||
16.10.2017||eUkiAhUWmZ||ЗэЖЫзЯШАэШ||27831190||8,10838026||

Developed by Kapturov Alexander
"""

from random import randint, randrange
from datetime import datetime, timedelta
from string import ascii_lowercase, ascii_uppercase
from time import time


def get_time() -> str:
    """
    Function for finding random day in last 5 years
    :return: random day
    """
    current_time = datetime.now() - timedelta(days=randint(1, 5 * 365))
    return str(current_time).replace('-', '.')[:10]


def generate_alphabet() -> str:
    """
    Function represents latin alphabet in upper and lower cases
    :return: latin alphabet in two cases
    """
    return ascii_lowercase + ascii_uppercase


def generate_russian_alphabet() -> str:
    """
    Function represents russian alphabet in upper and lower cases
    :return: russian alphabet in two cases
    """
    upper_case = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    return upper_case.lower() + upper_case


def get_random_alphabet_combination(alphabet) -> str:
    """
    Function generate 10 chars random text
    :param alphabet: function which callback alphabet
    :return: 10 chars random text from particular alphabet
    """
    phrase = [alphabet()[randint(0, len(alphabet()) - 1)] for _ in range(10)]
    return "".join(phrase)


def get_integer_even_number_combination() -> int:
    """
    Function generate random even number from range
    :return: random even number
    """
    return randrange(2, 100_000_000, 2)


def get_float_number_combination() -> float:
    """
    Function generate random float number from integer range between 1 and 20
    :return: random float number in range between 1 and 20
    """
    return randint(100_000_000, 2_000_000_000) / 100_000_000


def paste_data_into_line(data: list) -> list:
    """
    Function which append five elements into temporary list
    :param data: empty list which append five elements
    :return: temporary list with 5 elements
    """
    data.append(get_time())
    data.append(get_random_alphabet_combination(generate_alphabet))
    data.append(get_random_alphabet_combination(generate_russian_alphabet))
    data.append(str(get_integer_even_number_combination()))
    data.append(str(get_float_number_combination()).replace('.', ','))
    return data


def fulfill_file(file) -> None:
    """
    Function which creates temporary list, paste in with elements
    :param file: current file
    :return: None
    """
    for _ in range(100_000):
        message = []
        paste_data_into_line(message)
        result = '||'.join(message)
        file.write(f'{result}\n')


def files_creator() -> str:
    """
    Function create csv files and paste data into them
    :return: final phrase that shows time for execution
    """
    start_time = time()
    for name in range(1, 2):
        print(f'Заполняем данными файл {name}.csv')
        with open(f'{name}.csv', 'w', encoding='UTF-8') as file:
            fulfill_file(file)
    end_time = time()
    execution_time = end_time - start_time
    return f'{execution_time / 60:.2f}'


if __name__ == "__main__":
    print(f'All files are completed in {files_creator()} minutes')
# pylint score is 10.00/10
