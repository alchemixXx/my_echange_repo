#!/usr/bin/env python

import os

file_path = input("Enter file name: ")
name = file_path.split(".")
file = open(file_path, "r", errors = "ignore")


final_file = open(name[0]+"_cor.rep", "w")

counter = False
for line in file:
    if counter == True:
        final_file.write("\n")
    if line.startswith("W"):
        final_file.write(line[:-1])
        counter = True
    elif line.endswith("0"):
        index = line.find("S")
        final_file.write(line[index-1:-1])
        counter = True
    else:
        counter = False
        continue
file.close()
final_file.close()

os.remove(file_path)


# l2181225.dat