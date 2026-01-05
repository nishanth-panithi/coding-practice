
class car: #class

    # class = (blueprint) used to design the structure and layout of object.

    type="GT car"     #class varables
    number_of_cars=0

    #class varable = * shared class varable among all instances (objects) of a class.
    #                * define out-side of the constructor.
    #                * allows you to share data among all objects created from that class.

    #   __init__(self,paramaeter1,paramaeter2,paramaeter3,....)
    def __init__(self,model,year,color,milage,for_sale):# __init__ it is a constructor

        # __init__ = this constructor is auto-maticilly going to be called, but we need to pass some arguments, we are provided with "self".
        # self = refers to the objects that are we currently working with.
        #        ex: car1,car2,car3,phone,..........., can be any object that we are currently in.

        self.model=model  # attributes (varables) or "instance varable" that are defined in-side the constructor.
        self.year=year
        self.color=color
        self.milage=milage
        self.for_sale=for_sale
        car.number_of_cars+=1  #class varables using inside the constructor.
        # attributes = * is a "varables" that are defined in class.
        #         v *  attributes are actions that are objects can perform.

    def start(self): # methods (functions)
        print(f"you are start a {self.color} {self.model} {car.type}")
    def stop(self):
        print(f"you are stop a {self.color} {self.model} {car.type}")
    def describe(self):
        #  instance varable, instance varable,        class varable
        print(f"{self.color} {self.model} {self.year} {car.type}")

    # method = * is a "functoin" that are defined in class.
    #          *  methods are actions that objects can perform.