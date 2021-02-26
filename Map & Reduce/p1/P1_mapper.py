import sys
import re

word = sys.argv[1]

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)

    if word in words:
        print(line)


