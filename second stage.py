# Данный код разработал Каптуров Александр для собеседования в B1 (бывыший EY)

with open('second stage.txt', 'w', encoding='UTF-8') as big_file:
    pattern = 'abc'  # U can also use pattern = input() for other patterns
    pattern_match = 0

    for file in range(1, 101):
        with open(f'{file}.txt', 'r', encoding='UTF-8') as current_file:
            info = current_file.read()

            pattern_match += info.count(pattern)
            info.replace(pattern, '')

            big_file.write(info)

print(pattern_match)
