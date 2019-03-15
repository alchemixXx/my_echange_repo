#!/usr/bin/env python

file_path = input("Enter file name: ")
file = open(file_path, "r", errors = "ignore")


name = file_path.split(".")

final_file = open(name[0]+"_rec.dat", "w")
for line in file:
    if line.startswith("W"):
        final_file.write(line)
    else:
        index = line.find("S")
        final_file.write(line[index-1:])
file.close()
final_file.close()


file_second = open(name[0]+"_rec.dat", "r")


result = open(name[0]+"_cor.rep", "w")


counter = False
for new_line in file_second:
    if counter == True:
        result.write("\n")
    if new_line.startswith("W"):
        result.write(new_line[:-1])
        counter = True
    else:
        continue

file_second.close()
result.close()


# l2181211.dat