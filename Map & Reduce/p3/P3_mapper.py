import sys
import re

header = sys.stdin.readline()

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(",", line)
    fecha = words[0]
    close = words[4]

    print(fecha + "\t" + close)