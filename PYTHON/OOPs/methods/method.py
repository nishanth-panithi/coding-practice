#Types of methods
# Instance methods= Best for opperations on instances of the class (objects)
# Static Methods= Best for utility functions that do not need access the class data
# Class Methods= Best for class-level data or requires to the class itself
#
#Static Methods= A method that belong to a class rather than any object from the class (instance)
#                Usually used to geneal utility functions

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions=["manager","analyst","trainer","developer"]
        return position in valid_positions

pos=Employee.is_valid_position("manager")
print(pos)

print(Employee.is_valid_position("cook"))

employee1=Employee("nani","manager")
employee2=Employee("tony","analyst")
employee3=Employee("nishu","developer")
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

##########################################################

#Class Method= Allows operations related to the class itself
#              Take (cls) as the first parameter, which represents the class itself.

class Student:

    count=0
    total_marks=0 

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        Student.count+=1
        Student.total_marks+=mark

    def get_indfo(self):
        return f"Name:{self.name} mark:{self.mark}"
    
    @classmethod
    def std_count(cls):
        return f"total no of students:{cls.count}"
    
    @classmethod
    def average_marks(cls):
        if cls.count==0:
            return "average_marks:0"
        else:
            return f"average_marks: {cls.total_marks/cls.count:.2f}"


std1=Student("nani",8)
std2=Student("zezu",7)
std3=Student("nishu",9)

print(Student.std_count())
print(Student.average_marks())
