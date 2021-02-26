import sys
import re

anioanterior = None
suma = 0
cont = 0

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    fecha, closePrice = re.split("\t", line)
    anio = re.split("-", fecha)[0]

    if anioanterior != anio:
        if anioanterior is not None:
            print(anioanterior + "\t" + str(suma/cont))
        anioanterior = anio
        suma = float(closePrice)
        cont = 1
    else:
        suma += float(closePrice)
        cont += 1

print(anioanterior + "\t" + str(suma/cont))