#!/usr/bin/env python

file_name = input("Enter file name: ")
# print(file_name)

file = open(file_name, "r", encoding="ASCII")
result = open("l2181211_cor.rep", "w", encoding="ASCII")
for line in file:
    result.write(line)


    # l2181211 - Copy.dat
    # l2181211.dat