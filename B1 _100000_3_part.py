"""
Create a procedure for importing files with such a set of fields into a table in the DBMS.
When importing, the progress of the process should be displayed
(how many lines are imported, how many are left)

Developed by Kapturov Alexander
"""

import sqlite3
from time import time, sleep


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


def fill_database_with_file(file, data_loaded) -> None:
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
            data_loaded += 1
            print(f'{data_loaded} data has been loaded already into the database \
            {10_000_000 - data_loaded} data will be loaded into the database')


def fill_database_with_all_files(database='B1.db') -> None:
    """
    Function for fill database with data from all 100 files
    :param database: Current database which is being filled
    :return: None
    """
    data_loaded = 0
    with sqlite3.connect(database) as con:
        for name in range(1, 101):
            with open(f'{name}.txt', 'r', encoding='UTF-8') as file:
                fill_database_with_file(file, data_loaded)
            con.commit()

            print(f'\n{name}/100 files are written to the database\n')
            data_loaded += 100_000
            sleep(3)


if __name__ == "__main__":
    start_time = time()

    create_database()
    fill_database_with_all_files('B1.db')

    end_time = time()
    execution_time = end_time - start_time
    print(f'execution_time: {execution_time:.2f} seconds')
# pylint score is 10.00/10
