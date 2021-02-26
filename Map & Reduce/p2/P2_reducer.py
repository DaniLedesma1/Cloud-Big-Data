import sys
import re

urlanterior= None
cont = 0

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    url, quantity = re.split("\t", line)

    if urlanterior != url:
        if urlanterior is not None:
            print(urlanterior + "\t" + str(cont))
        urlanterior = url
        cont = int(quantity)
    else:
        cont += int(quantity)

print(urlanterior + "\t" + str(cont))