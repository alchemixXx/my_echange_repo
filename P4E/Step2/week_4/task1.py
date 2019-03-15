#!/usr/bin/env python

reads = open("romeo.txt", "r")
final = list()
for line in reads:
    splited = line.split()
    for word in splited:
        if word in final:
            continue
        else:
            final.append(word)
else:
    final.sort()

print(final)
reads.close()
