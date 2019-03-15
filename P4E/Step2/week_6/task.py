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
         adress = new_list[5]
         time = new_list[5].split(":")
         hours = time[0]
         final_dict[hours] = final_dict.get(hours, 0) + 1
file.close()

# temp = list()
# for k, v in final_dict.items():
#     temp.append((k,v))
# temp.sort()
x = sorted([(k, v) for k,v in final_dict.items()])

for k, v in x:
    print(k, v)

# print(x)


# print(final_dict)
