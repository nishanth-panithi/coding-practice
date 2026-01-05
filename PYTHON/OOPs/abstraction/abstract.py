#Abstrct class=A class that cannot be instantiated on its own; Meant to be subclassd.
#              Thay can contain abstract methods,which are decleared but have no implimentation.
#              Abstract classes benfites :
#              1. prevents instentations of the class itself
#              2. Requires children to use inherited abstrsct methods
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("car is going")
    def stop(self):
        print("car is stoped")
car=Car()
car.go()
car.stop()
class Motercycle(Vehicle):
    def go(self):
        print("Bike is going")
    def stop(self):
        print("Bike is stoped")
bike=Motercycle()
bike.go()
bike.stop()