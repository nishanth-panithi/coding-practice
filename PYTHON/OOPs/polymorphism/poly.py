# polymorphism= greek word that means to say "many forms or faces"
#               poly = many
#               morphe = form
#               TWO WAYS TO ACTIVATE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2. Duck Typing = objects must have necessary attributes/methods

#   1. Inheritance

# class Dog():
#     def sound(self):
#         print("woof!")
# class Cat():
#     def sound(self):
#         print("meaw!")

# for animal in (Dog(),Cat()):
#     animal.sound()

####################################################  

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area():
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class pizza(circle):
    def __init__(self,radius):
        super().__init__(radius)
shapes=[circle(5),pizza(2)]
for shape in shapes:
    print(f"{shape.area()}cm²")

####################################################  

#2. Duck Typing= Anotherd way to achieve polymorphism besides Inheritence
#                objectes must have the minimum necessary attributes/methods
#                "if it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive=True
class Dog(Animal):
    def speak(self):
        print("woof!")
class Cat(Animal):
    def speak(self):
        print("meaw!")

class Car: # "if it looks like a duck and quacks like a duck, it must be a duck"
    alive=True
    def speak(self):
        print("honk!")

animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)



