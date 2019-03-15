#!/usr/bin/env python

#welcome section

# x = 108
# y = 105
# z = 115
# f = 116
# print(chr(x),chr(y),chr(z),chr(f))

#Week1 section

#building my own class

class AnimalParty:  # give the name of new class
    attend = 0  #atribute equal to my age
    name = ""

    def __init__(self, name):
        self.name = name  # add the new atrubute to the class
        print(self.name, "is constructed!")

    def party(self):  # make a method of new class
        self.attend += 1  # increese the atribute by one
        print(self.name, "joins the party, total count of members: ", self.attend)  # print out the result

    def __del__(self):
        print("Party destructed at", self.attend, "members  ")


x = AnimalParty("Doggy")  # asign "x" to class "aclemixxx"

x.party()  # launch the method of class
print(type(AnimalParty))
