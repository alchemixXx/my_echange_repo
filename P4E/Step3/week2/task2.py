#!/usr/bin/env python
summ = 0
counter = 0
import re
name = open("real_file.txt")
for line in name:
    line = line.rstrip()
    numbs = re.findall('[0-9]+', line)

    if len(numbs) >= 1:
        for numb in numbs:
            summ += float(numb)
            counter += 1

name.close()

print(summ)
print(counter)