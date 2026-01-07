#Nested Class= A class defines with in another class
#               classOuter:
#                   classInner:

#Benfites:Allows you to logically group clsses that are closely related 
#         Encapsulates private details that aren't related outside of the outer class
#         Keeps the namespace clean;reduses the possibility of naming conflicts

class employee:
    print("class 1")
class employee:
    print("class 2")    # this creates naming conflicts while importing from another files, we may not know there are 2 class

class company1:
    class employee:
        print("class 1")
class company2:
    class employee:
        print("class 2")     # Keeps the namespace clean, reduses the possibility of naming conflicts.


################################################################

class Company:
    class Employee:
        def __init__(self,name,position):
            self.name=name
            self.position=position   
        def get_details(self):
            return f"{self.name} {self.position}"
        
    def __init__(self,name):
        self.name=name
        self.employees=[]
    def add_emp(self,name,position):
        new_emp=self.Employee(name,position)
        self.employees.append(new_emp)
    def list_emoloyee(self):
        return [employee.get_details() for employee in self.employees]

company=Company("google")

print(company.name)

company.add_emp("nani","manager")
company.add_emp("nishu","ceo")

print(company.list_emoloyee())

for employee in company.employees:
    print(employee.get_details())