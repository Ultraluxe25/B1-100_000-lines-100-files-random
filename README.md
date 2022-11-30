# B1 100.000 lines
> 1.	Сгенерировать 100 текстовых файлов со следующей структурой, каждый из которых содержит 100 000 строк
случайная дата за последние 5 лет || случайный набор 10 латинских символов || случайный набор 10 русских символов || случайное положительное четное целочисленное число в диапазоне от 1 до 100 000 000   || случайное положительное число с 8 знаками после запятой в диапазоне от 1 до 20
		
> Пример вывода:
03.03.2015||ZAwRbpGUiK||мДМЮаНкуКД||14152932||7,87742021||
23.01.2015||vgHKThbgrP||ЛДКХысХшЗЦ||35085588||8,49822372||
17.10.2017||AuTVNvaGRB||мЧепрИецрА||34259646||17,7248118||
24.09.2014||ArIAASwOnE||ЧпЙМдШлыфУ||23252734||14,6239438||
16.10.2017||eUkiAhUWmZ||ЗэЖЫзЯШАэШ||27831190||8,10838026||

> 2.	Реализовать объединение файлов в один. При объединении должна быть возможность удалить из всех файлов строки с заданным сочетанием символов, например, «abc» с выводом информации о количестве удаленных строк
> 3.	Создать процедуру импорта файлов с таким набором полей в таблицу в СУБД. При импорте должен выводится ход процесса (сколько строк импортировано, сколько осталось)
> 4.	Реализовать хранимую процедуру в БД (или скрипт с внешним sql-запросом), который считает сумму всех целых чисел и медиану всех дробных чисел
Все скрипты/процедуры/запросы из пунктов 2-3-4 должны быть повторяемыми.
