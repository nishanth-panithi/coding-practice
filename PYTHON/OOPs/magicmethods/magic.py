# Magic Methods= Dunder Method (Double underscore) __init__,__str__,__eq__,__lt__,__gt__,__add__,__contains__,__getitem__
#                Thay are autonatically called by many of python's built-in operations. 
#                Thay allow developers to define or customize the behavior of objects
#
class Student:
    def __init__(self,name,department,gpa):
        self.name=name
        self.department=department
        self.gpa=gpa

    def __str__(self):
        return f"Name: {self.name} Department: {self.department} GPA: {self.gpa}"
    
    def __eq__(self,other):
       return f"Equal: {self.name==other.name and self.department==other.department}"

    def __lt__(self,other):
        return f"Lessthan: {self.gpa < other.gpa}"
    
    def __gt__(self,other):
        return f"Greaterthan: {self.gpa > other.gpa}"
    
    def __add__(self,other):
        return f"Added GPA: {self.gpa + other.gpa}"
    
    def __contains__(self,keyword):
        return  keyword in self.name or keyword in self.department
    
    def __getitem__(self,key):
        if key=="name":
            return f"Name: {self.name}"
        elif key=="department":
            return f"Department: {self.department}"
        elif key=="gpa":
            return f"GPA: {self.gpa}"
        else:
            return f"Key '{key}' not found"
    
std1=Student("Nishanth","CSE",8.0)
std2=Student("Nishanth","CSE",7.0)
std3=Student("Nishu","IT",9.0)
std4=Student("Zezu","IT",9.0)
print(std1)
print(std1==std2)
print(std1<std2)
print(std1>std2)
print(std1+std2)
print("z" in std4)
print(std1["name"])
