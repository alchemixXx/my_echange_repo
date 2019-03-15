#!/usr/bin/env python

#var 1
file = open("mbox-short.txt", "r")
final_dict = dict()
for line in file:
    if not line.startswith("From "):
        continue
    else:
         new_line = line.strip()
         new_list = line.split()
         adress = new_list[1]
         final_dict[adress] = final_dict.get(adress, 0) + 1
file.close()

max_word = None
max_count = None
for name, count in final_dict.items():
    if max_count == None or max_count < count:
        max_word = name
        max_count = count
print(max_word, max_count)



# var for testing

# line = """From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# From: stephen.marquard@uct.ac.za
# From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008"""
#
# final_dict = dict()
#
# # for line in file:
# if line.startswith("From "):
#      new_line = line.strip()
#      print(new_line)
#      new_list = new_line.split()
#      final_dict[new_list[1]] = final_dict[new_list[1]].get(new_list[1], 0) + 1
#
# print(final_dict)


