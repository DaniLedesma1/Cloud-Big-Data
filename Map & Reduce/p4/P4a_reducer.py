import sys
import re

previousId = None
suma = 0
cont = 0

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    id, rating = re.split("\t", line)

    if previousId != id:
        if previousId is not None:
            print(previousId + "\t" + str(suma/cont))
        previousId = id
        suma = float(rating)
        cont = 1
    else:
        suma += float(rating)
        cont += 1

print(previousId + "\t" + str(suma/cont))