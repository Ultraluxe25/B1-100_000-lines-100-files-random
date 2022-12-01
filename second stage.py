"""
Implement merging of 100 files with 100K lines each into one.
When merging, it should be possible to delete lines with a given combination of characters
from all files, for example, "abc" with information about the number of deleted lines

Developed by Kapturov Alexander
"""


def show_quantity_of_pattern_match() -> str:
    """
    Function for building 1 big file from 100 small (10M lines)
    with opportunity for removing pattern

    :return: Quantity of patterns were found and removed (replaced into empty line)
    """
    with open('second stage.txt', 'w', encoding='UTF-8') as big_file:
        pattern = 'abc'  # U can also use pattern = input() for other patterns
        pattern_match = 0

        for file in range(1, 101):
            with open(f'{file}.txt', 'r', encoding='UTF-8') as current_file:
                info = current_file.read()

                pattern_match += info.count(pattern)
                info.replace(pattern, '')

                big_file.write(info)

    return f'Quantity of matches: {pattern_match}'


print(show_quantity_of_pattern_match())

# pylint score is 10.00/10
