# B1 100.000 lines

1.	Generate 100 text files with the following structure, each containing 100,000 lines
random date for the last 5 years || random set of 10 Latin characters ||
random set of 10 Russian characters || random positive even integer between 1 and 100,000,000 ||
random positive number with 8 decimal places in the range from 1 to 20

Output sample:
03.03.2015||ZAwRbpGUiK||мДМЮаНкуКД||14152932||7,87742021||
23.01.2015||vgHKThbgrP||ЛДКХысХшЗЦ||35085588||8,49822372||
17.10.2017||AuTVNvaGRB||мЧепрИецрА||34259646||17,7248118||
24.09.2014||ArIAASwOnE||ЧпЙМдШлыфУ||23252734||14,6239438||
16.10.2017||eUkiAhUWmZ||ЗэЖЫзЯШАэШ||27831190||8,10838026||

2.	Implement merging of 100 files with 100K lines each into one.
When merging, it should be possible to delete lines with a given combination of characters
from all files, for example, "abc" with information about the number of deleted lines

3.	Create a procedure for importing files with such a set of fields into a table in the DBMS.
When importing, the progress of the process should be displayed
(how many lines are imported, how many are left)
4.	Implement a stored procedure in the database (or a script with an external sql query)
that calculates the sum of all integers and the median of all fractional numbers

All scripts/procedures/requests from points 2-3-4 must be repeatable.
