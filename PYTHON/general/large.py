a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("a ig big")
elif b>a and b>c:
    print("b is big")
elif c>a and c>b:
    print("c is big")
elif a==b and a==c:
    print("a,b and c is equal")
elif a==c:
    print("a and c is equal and big")
elif b==c:
    print("b and c is equal and big")
else: 
    print("a and b is equal and big")