#@Property= Decorator used to define a method as a property (it can be accesed like attribute)
#           Benfites= Add additional logic when read, write, or delete attribute
#           Gives you getter, setter, and deleter method
# 

class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property   #getter method
    def width(self):
        return f"Width: {self._width}cm²"
    @property
    def height(self):
        return f"Height: {self._height}cm²"
    
    @width.setter     #setter method
    def width(self,new_width):
        if new_width > 0:
            self._width=new_width
        else:
            print ("width must be greater than 0")
    @height.setter    #deleter method
    def height(self,new_height):
        if new_height > 0:
            self._height=new_height
        else:
            print ("height must be greater than 0")
    
    @width.deleter    #deleter method
    def width(self):
        del self._width
        print("width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangel=Rectangle(4,5)
rectangel.width=0

print(rectangel.height)
print(rectangel.width)

del rectangel.height