#Aggregation= A relationship where one object (the whole) contains references to one or more 
#             other INDEPANDENT objects (the part) "has a" relationship

#.  Aggregation

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}"for book in self.books]

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

library=Library("new york public library")

book1=Book("Harry Potter","J.K.Rowling")
book2=Book("The Hobbit","J.R.R. Tolkein")
book3=Book("The color of Magic","Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
for book in library.list_books():
    print(book)
print(library.list_books())

#####################################################

#Composition= The composed object directly owns its components, 
#             which cannot exist indepandentely "owns a" relationship

#.  Composition

class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power

class Wheel:
    def __init__(self,wheel_size):
        self.wheel_size=wheel_size

class Car:
    def __init__(self,maker,model,horse_power,wheel_size):
        self.maker=maker
        self.model=model
        self.engine=Engine(horse_power)
        self.wheels=[Wheel(wheel_size) for wheel in range(4)] # this will create 4 wheels
    def display_car(self):
        return f"{self.maker} {self.model} {self.engine.horse_power}HP {self.wheels[0].wheel_size}inch wheel"

car=Car(maker="ford",model="mustang",horse_power="500",wheel_size=18)

print(car.display_car())