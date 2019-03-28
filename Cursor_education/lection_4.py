# # import time
# # import dis
# #
# # # list comprehantion
# # a = [i for in range(100)]
# #
# # # to check how many resourses used to make a result "DIS" is used (need to compare with other variants)
# # print(dis.dis(a))
#
#
#
#
# import random
# r_name_list = ['Pavel', 'Igor', 'Ostap', 'Evgen']
# r_age_list = [i for i in range(1,100)]
# class Student:
#     def __init__(self, name, age, gender='male'):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def __str__(self):
#         return "My name is {} and I am {} years old".format(self.name, self.age)
#
#
#
# "Запусти метод А, тільки коли Б менше 6." Перепиши цю умову (для абстрактної умови виконання), використовуючи if, else чи while чи інші зарезервовані слова. *
#
#
#     if Б < 6:
#         x.A()
#
#
# "Я маю 1 ручку. Я маю 5 яблук. Якщо Ручка-Яблуко (сума*) дорівнює 13, тоді я хочу показати будь-яке повідомлення."
# Перепишіть цю умову (для абстрактної умови виконання) використовуючи if, else, while чи інші зарезервовані слова.
#
# x = 1  # numb of pens
# y = 5  # numb of apples
#
# if (x + y) == 13:
#     #do something


one = False
two = False
three = False
x = [(i // (i - 0.37)) for i in range(0, 1589, 12)]
while one != True and two != True and three != True:
    age = int(input("How old are you? "))
    if age > 0:
        one = True
    else:
        print("Not a chance! Give me real age!")
    height = int(input("What is your heigh, cm? "))
    if height > 0:
        two = True
    elif height > 300:
        print("No way! I don't belive that you're giant! Give me real height, buddy!")
    else:
        print("Do not cheat! Give me real height, buddy!")
    date = int(input("On what date of month you were born? "))
    if date > 0:
        one = True
    else:
        print("No cheeting! Give me real date, please!")
    while True:
        numb = int(input("Enter number: "))
        if numb < len(x):
            print("Ok, now you will see the result")
            break
        else:
            print("Sorry, my friend! Please, choose other number. I know you are smart, but you better to choose smaller number :) ")

class Prediction():

    def __init__(self, age, height, date):
        self.age = age
        self.height = height
        self.date_of_born = date


    def clarify(self):
        approx_1 = ((self.height ** self.date_of_born) // self.age) // x[numb]
        return approx_1

test = Prediction(age, height, date)
rest = test.clarify()
if rest:
    print("Using VERY PRECISIVE approach, we defined that you are HUMAN! CONGRADS! Your result is {}".format(rest))
else:
    print("you are not a human, go for your plannet, alient!!! Your result is {}".format(rest))

