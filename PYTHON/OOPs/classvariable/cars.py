
from car import Car # import files

car1=Car("virtus","2021","red",20,False) #class instances , creating instences , (objects) 
car2=Car("be6","2023","black",400,False)
car3=Car("bmw_m40i","2023","red",12,False)

# object = A "bundle" of related attributes (varables) and methods (functions).
#          Using a "class" we can create many objects
#          ex: "car1" with data some (attributes)--car1=car("virtus","2021","red",20,False)
#              "phone" with data some (attributes)--("iphone","black",256)

print(car1.model) # instance varable
print(car2.model)
print(car3.model)
 
print(Car.number_of_cars) # class varable

# .(dot) = is attribute acces operator

car1.start() # methods are actions that objects can perform.
car1.stop()
car1.describe()
