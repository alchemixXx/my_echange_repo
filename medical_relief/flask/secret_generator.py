import random
import string

# x = [string.random(string.ascii_letters, string.digits) for _ in range(15)]
# secret = ''
# for i in range(15):
#     secret += random.choice(string.ascii_lowercase) + random.choice(string.digits)
# print(secret)


x = "".join([random.choice(string.ascii_lowercase) + random.choice(string.digits) for _ in range(15)])
print(x)