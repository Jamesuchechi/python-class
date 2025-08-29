class Dog:
    def bark(self):
        print("barks like a lion")

#creating an object (instance)
myvar = Dog()
myvar.bark()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks like a lion")

myvar = Dog("spark", 4)
print(myvar.name)
print(myvar.age)

class Animal:
    species = "Homo sapian"

    def __init__(self, name):
        self.name = name

hum1 = Animal("Jerry")
hum2 = Animal("James")
hum3 = Animal("Emmanuel")
hum4 = Animal("Chidimma")
print(hum1.species)
print(hum2.species)
print(hum3.species)
print(hum4.species)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self):
        self.age += 1
        print(f"{self.name} is now{self.age} years old")

myvar = Human("kamsy", 14)
myvar.get_older()


# INHERITANCE

class James:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("i speak so well")

class Son(James): #inherits the class

    def speak(self): # overides the parent method

        print("I have a nice voice and i am eloquent too")

myvar = Son("Eden")
myvar.speak()