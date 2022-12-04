"""
Implement a stored procedure in the database (or a script with an external sql query)
that calculates the sum of all integers and the median of all fractional numbers

Developed by Kapturov Alexander
"""

import sqlite3
import numpy as np


def fulfill_database():
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

    for name in range(1, 2):
        print(f'Записывается {name} файл')
        with open(f'{name}.txt', 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for line in data:
                record = line[:-1].split('||')
                col1, col2, col3, col4, col5 = record
                col4 = int(col4)
                col5 = float(col5.replace(',', '.'))
                cur.execute(f"""INSERT INTO B1_data(calendar, english_alphabet, russian_alphabet, \
                integer_number, float_number)
                VALUES ('{col1}', '{col2}', '{col3}', '{col4}', '{col5}')""")
                # # print(line[:-1].split('||'))
                # print(col1, col2, col3, col4, col5)
        con.commit()


def get_int_sum(data_base='B1.db'):
    with sqlite3.connect(data_base) as con:
        cur = con.cursor()
        for value in cur.execute('SELECT SUM(integer_number) FROM B1_data'):
            return value[0]


def getfloat_median(data_base='B1.db'):
    with sqlite3.connect(data_base) as con:
        cur = con.cursor()
        float_numbers_list = []
        for value in cur.execute(f'SELECT float_number FROM B1_data'):
            float_numbers_list.append(value[0])
        return np.mean(float_numbers_list)


if __name__ == "__main__":
    fulfill_database()
    print(f'Integer number\'s sum value is: {get_int_sum()}')
    print(f'Float number\'s median value is: {getfloat_median()}')
