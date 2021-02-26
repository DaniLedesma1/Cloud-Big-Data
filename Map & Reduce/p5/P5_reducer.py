import sys
import re

anterior = None
suma = 0
cont = 0

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    tipo, masa = re.split("\t", line)

    if anterior != tipo:
        if anterior is not None:
            print(anterior + "\t" + str(suma/cont))
        anterior = tipo
        suma = float(masa)
        cont = 1
    else:
        suma += float(masa)
        cont += 1

print(anterior + "\t" + str(suma/cont))