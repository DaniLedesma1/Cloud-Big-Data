import sys
from csv import reader

for line in reader(sys.stdin):
    tipo= line[3]
    masa = line[4]

    if len(masa) != 0 and len(tipo) != 0:
        print(tipo + "\t" + masa)
