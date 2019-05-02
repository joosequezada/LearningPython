#!/usr/bin/python3

"""
Mostrar en pantalla la cantidad de meses transcurridos
desde la fecha de nacimiento de un usuario.
"""
from datetime import datetime
import arrow

print("///Python3 Script - Meses de nacimiento///\n")
y 	= int(input("Type born year as 1900, 1960, 2010.\nYear: "))
m 	= int(input("Type born month as 4, 2, 10, 9.\nMonth: "))
d 	= int(input("Type born day as 1, 9, 10, 23.\nDay: "))

start = datetime(y, m, d)
end = datetime.today()


print("\n>>> Months Alived: [ %s ] <<<" % len(arrow.Arrow.range('month', start, end)))