#if prime or not
'''  
f=0
n=int(input("enter a numbre"))
for i in range(2,n):
    if n%i==0:
        f+=1
if f==0:
    print("it is a prime number")
else:
    print("it is not a prime number")     '''  
#in a proper way (positional prime number)
'''  
pos=11
num=2   #2 3 5 7 11 13 17 23 27
count=0 #
prime=0
while count<pos:
    factors=0
    for i in range(2,num):
        if num%i==0:
            factors+=1
            break
    if factors==0: 
        prime=num
        count+=1 
    num+=1
print(f"{prime} is a {pos}th position prime number")            '''
# prime num under n
num=10
for n in range(2,num+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
