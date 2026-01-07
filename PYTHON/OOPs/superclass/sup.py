#super class is parent class
#super()=Function used in a child class to call methods from a parent class called "superclass".
        #Allows you to extands the functionality of the inherited methods.
class shape:
    def __init__(self,color,is_filled):
       self.color=color
       self.is_filled=is_filled
    def discribe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")
class Circle(shape):
    def __init__(self,color,is_filled,radius):
        self.radius=radius
        super().__init__(color,is_filled) #or shape.__init__(self,color,is_filled) 
        super().discribe()
    def discribe(self):
        print(f"it is a circle with area of {3.24*self.radius*self.radius}cm")
class Square(shape):
    def __init__(self,color,is_filled,side):
        super().__init__(color,is_filled)
        self.side=side
    def discribe(self):
        print(f"it is a square with area of {2*self.side}cm")
        super().discribe()
class Triangle(shape):
    def __init__(self,color,is_filled,hight,base):
        super().__init__(color,is_filled)
        self.hight=hight
        self.base=base
    def discribe(self):
        print(f"it is a triangle with area of {0.5*self.base*self.hight}cm")
        super().discribe()

circle=Circle(color="red",is_filled=True,radius=5)
square=Square(color="blue",is_filled=False,side=3)
triangel=Triangle(color="green",is_filled=True,hight=3,base=5)

print(circle.color)

circle.discribe()
square.discribe()
triangel.discribe()

