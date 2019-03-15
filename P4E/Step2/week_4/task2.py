#!/usr/bin/env python

opened = open("mbox-short.txt", "r")
final = list()
counter = 0
for line in opened:
    if line.startswith("From "):
        temp_list = line.split()
        final.append(temp_list[1])
        counter += 1
    else:
        continue
opened.close()

for adress in final:
    print(adress)
print("There were", counter, "lines in the file with From as the first word")


