import time
import dis

# list comprehantion
a = [i for in range(100)]

# to check how many resourses used to make a result "DIS" is used (need to compare with other variants)
print(dis.dis(a))