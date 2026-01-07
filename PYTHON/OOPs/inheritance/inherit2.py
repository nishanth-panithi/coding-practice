#Multiple Inheritance=inherit from more than one parent
#                     C(A,B)
#Multilevel Inheritance=inherit from a parent which inherits from another parent
#                   A->B(A)->C(B)

class Vehicle():
    def __init__(self,name):
        self.name=name
    def go(self):
        print(f"{self.name} is going")
    def stop(self):
        print(f"{self.name} is stoped")

class Car(Vehicle):
    def wheels(self):
        print(f"{self.name} has 4 wheels") 
        
class Virtus(Car):
    pass

car=Virtus(name="virtus")
car.go() #Multilevel Inheritance