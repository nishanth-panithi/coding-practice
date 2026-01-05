'''
string=input("enter")
rev=string[::-1]
if string==rev:
    print("palindrom")
else:
    ("not palindrom") '''

#without usiing string slicing

str=input("enter a string to check if it is a palindrom or not...!:")
rev=""
last=len(str)-1
for i in range(last,-1,-1):
    rev+=str[i]
if  rev==str:
    print("palindrome")
else:
    print("not a palindrome")  