import sqlite3


def fulfill_database():
    with sqlite3.connect('B1.db') as con:
        cur = con.cursor()  # In order to execute SQL statements and fetch results from SQL queries

        cur.execute("""CREATE TABLE IF NOT EXISTS B1_data (
            data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            calendar TEXT,
            english_alphabet TEXT,
            russian_alphabet TEXT,
            integer_number INTEGER,
            float_number REAL
            )""")

        # cur.execute("""DROP TABLE IF EXISTS B1_data
        # """)

    for name in range(1, 101):
        print(f'Записывается {name} файл')
        with open(f'{name}.txt', 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for line in data:
                record = line[:-1].split('||')
                col1, col2, col3, col4, col5 = record
                cur.execute(f"""INSERT INTO B1_data(calendar, english_alphabet, russian_alphabet, integer_number, float_number)
                          VALUES ('{col1}', '{col2}', '{col3}', '{int(col4)}', '{float(col5.replace(',', '.'))}')""")
                # # print(line[:-1].split('||'))
                # print(col1, col2, col3, col4, col5)
        con.commit()


if __name__ == "__main__":
    fulfill_database()
