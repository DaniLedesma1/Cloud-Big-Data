import sys
import re

header = sys.stdin.readline()

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(",", line)
    ids = words[1]
    rating = words[2]

    print(ids + "\t" + rating)