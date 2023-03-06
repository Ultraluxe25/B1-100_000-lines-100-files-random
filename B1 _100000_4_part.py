"""
Implement a stored procedure in the database (or a script with an external sql query)
that calculates the sum of all integers and the median of all fractional numbers

Developed by Kapturov Alexander
"""

import sqlite3
from time import time
import numpy as np  # For getting median. Use 'pip install numpy' to execute this file


def create_database() -> None:
    """
    Function creates database
    :return: None
    """
    with sqlite3.connect('B1.db') as con:
        cur = con.cursor()  # In order to execute SQL statements and fetch results from SQL queries

        cur.execute("""DROP TABLE IF EXISTS B1_data
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS B1_data (
            data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            calendar TEXT,
            english_alphabet TEXT,
            russian_alphabet TEXT,
            integer_number INTEGER,
            float_number REAL
            )""")


def fill_database_with_file(file) -> None:
    """
    Function fills database with data from current file
    :param file: The current file from which the data for the database is unloaded
    :return: None
    """
    with sqlite3.connect('B1.db') as con:
        cur = con.cursor()
        data = file.readlines()
        for line in data:
            record = line[:-1].split('||')
            col1, col2, col3, col4, col5 = record
            col4 = int(col4)
            col5 = float(col5.replace(',', '.'))
            cur.execute(f"""INSERT INTO B1_data(calendar, english_alphabet, russian_alphabet, \
                            integer_number, float_number)
                            VALUES ('{col1}', '{col2}', '{col3}', '{col4}', '{col5}')""")


def fill_database_with_all_files(database='B1.db') -> None:
    """
    Function for fill database with data from all 100 files
    :param database: Current database which is being filled
    :return: None
    """
    with sqlite3.connect(database) as con:
        for name in range(1, 101):
            print(f'The {name} file is written to the database')
            with open(f'{name}.txt', 'r', encoding='UTF-8') as file:
                fill_database_with_file(file)
            con.commit()


def get_int_sum(data_base='B1.db') -> int:
    """
    Function return total sum of all integer numbers from 'integer_number' column
    :param data_base: Database which used to get data
    :return: Integer number's sum value
    """
    with sqlite3.connect(data_base) as con:
        cur = con.cursor()
        for value in cur.execute('SELECT SUM(integer_number) FROM B1_data'):
            return value[0]


def get_float_median(data_base='B1.db') -> np.array:
    """
    Function return float number's median value from 'float_number' column
    :param data_base: Database which used to get data
    :return: Float number's median value
    """
    with sqlite3.connect(data_base) as con:
        cur = con.cursor()
        float_numbers_list = []
        for value in cur.execute('SELECT float_number FROM B1_data'):
            float_numbers_list.append(value[0])
        return np.median(float_numbers_list)


if __name__ == "__main__":
    start_time = time()

    create_database()
    fill_database_with_all_files('B1.db')
    print(f'\nInteger number\'s sum value is: {get_int_sum()}')
    print(f'Float number\'s median value is: {get_float_median()}')

    end_time = time()
    execution_time = end_time - start_time
    print(f'execution_time: {execution_time:.2f} seconds')
# pylint score is 10.00/10
