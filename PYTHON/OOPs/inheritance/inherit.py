#Inheritance=Allows a class to inherit attributes and methods from another class.
#            Helps with code reusabulity and extansibility.
#            class child(parent)
class Animal:
    def __init__(self,name):
        self.name=name 
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def __init__(self, name,sound):
        super().__init__(name)     #correct way
        self.sound=sound
        super().eat()
    def Sound(self):
        print(f"Dog makes {self.sound} sounds")
        
class Cat(Animal):
    def __init__(self, name, sound):
        Animal.__init__(self,name)    #not so healthy
        self.sound=sound
        Animal.sleep(self)
    def Sound(self):
        print(f"Cat makes {self.sound} sounds")

dog=Dog(name="scooby",sound="woof!")
cat=Cat(name="tommy",sound="meaw!")
dog.eat()
cat.sleep()
cat.Sound()
dog.Sound()