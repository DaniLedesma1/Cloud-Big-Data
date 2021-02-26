import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    id, media = re.split("\t", line)

    print(media + "\t" + id)