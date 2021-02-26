import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(" ", line)
    url = words[0]

    print(url + "\t" + "1")