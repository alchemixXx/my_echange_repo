#INHERITANCE
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


class Dog(Animal):

    def __init__(self, spice, paws):
        self.spice = spice
        self.paws = paws
        Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("OOOOF")

    def __str__(self):
        return "The class is {}".format(self.spice)

    def __len__(self):
        return self.paws

    def __del__(self):
        print("DOG IS GONE")

mydog = Dog("murmmul", 4)
print(mydog)
print(len(mydog))
del mydog
