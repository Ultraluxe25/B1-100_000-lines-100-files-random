# Данный код разработал Каптуров Александр для собеседования в B1 (бывыший EY)

class GeneralFileWithPatternRemover:
    @staticmethod
    def show_quantity_of_pattern_match() -> str:
        with open('second stage.txt', 'w', encoding='UTF-8') as big_file:
            pattern = 'abc'  # U can also use pattern = input() for other patterns
            pattern_match = 0

            for file in range(1, 101):
                with open(f'{file}.txt', 'r', encoding='UTF-8') as current_file:
                    info = current_file.read()

                    pattern_match += info.count(pattern)
                    info.replace(pattern, '')

                    big_file.write(info)

        return f'Найдено совпадений: {pattern_match}'


new_file = GeneralFileWithPatternRemover()
print(new_file.show_quantity_of_pattern_match())
