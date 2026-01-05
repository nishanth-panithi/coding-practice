#own
'''
year=int(input("enter year"))
if (year%100==0 and year%400!=0):
    print(year," is not a leap year")
elif (year%4==0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")      '''
#another way using nested loop
'''
year=int(input("enter year"))
if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year")
        else:
             print("not a leap year") 
    else:
         print("leap year")             
else:
    print("not a leap year")  '''      
# using calender.isleap()
'''
import calendar
year=int(input("enter year"))
if calendar.isleap(year):
    print("leap year")
else:
    print("not a leap year")       '''
#using lambda

year=int(input("enter year"))
test=lambda year: (year%4==0 and year%100!=0)or(year%400==0)
if test(year):
    print("leap year")
else:
    print("not a leap")      
#using single condition
'''
year=int(input("enter year"))
if (year%4==0 and year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("not leap year")'''