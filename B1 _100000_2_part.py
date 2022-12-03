"""
Implement merging of 100 files with 100K lines each into one.
When merging, it should be possible to delete lines with a given combination of characters
from all files, for example, "abc" with information about the number of deleted lines

Developed by Kapturov Alexander
"""

from time import time


def show_quantity_of_pattern_match(pattern='abc') -> tuple:
    """
    Function for building 1 big file from 100 small (10M lines)
    with opportunity for removing lines which have pattern

    :return: Quantity of patterns were found and moved lines
    """
    pattern_match = 0
    lines_moved = 0
    with open('second_stage.txt', 'w', encoding='UTF-8') as big_file:
        for file in range(1, 101):
            with open(f'{file}.txt', 'r', encoding='UTF-8') as current_file:
                data = current_file.readlines()
                for line in data:
                    if pattern not in line:
                        big_file.write(line)
                        lines_moved += 1
                    else:
                        pattern_match += 1

    return pattern_match, lines_moved


if __name__ == "__main__":
    start_time = time()
    patterns_found, moved_lines = show_quantity_of_pattern_match('EY')
    print(f'Patterns found: {patterns_found}')
    print(f'Lines moved: {moved_lines}')

    end_time = time()
    execution_time = end_time - start_time
    print(f'execution_time: {execution_time:.2f} seconds')
# pylint score is 10.00/10


# print('Do you wanna to use your own pattern? ')
# user_response = input()
#
# if user_response.lower() == 'yes':
#     pattern = input('Set your own pattern: ')
#     print(show_quantity_of_pattern_match(pattern))
# else:
#     print(show_quantity_of_pattern_match())
