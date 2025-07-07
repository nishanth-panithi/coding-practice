#add 2 numbers using function
#return, defalt args
'''
def add (a=10,b=20):
   return a+b
print(add())  '''

#positional args
'''
def add(a,b):
    print(a+b)
add(10,20)   '''

#keyword args
'''
def add(a,b):
    print(a+b)
add(b=20,a=10)
'''
#factorial
'''
def fac(n):
    for i in range(1,n+1):
       f=n*i
    print(f)
fac(5)
'''
#square of a number
'''
def sq(n):
    print(n**2)
sq(5)
'''
#largest of 2 
'''
def lar(a,b):
    if a>b:
        print(a,"is larger than",b)
    elif b>a:
        print(b,"is larger than",a)
    else:
        print("both are")        
lar(10,20)'''
#find even or odd
'''
def eo(num):
    if num>0:
      if num%2==0:
        print(num,"is a even number")
      else:
        print(num,"is a odd number")  
    else:
     print("enter a valid number")
eo(3)'''
#find prime or not
'''
def prime(num):
    count=0
    for i in range(1,num+1):
        num%i==0
        count+=1
    if count==2:
        print(num,"is a prime")
    else:
        print(num,"is not a prime")    
prime(11)  '''
#sum of n natural num
'''
def natural(n):
    sum=0
    for i in range(1,n+1):
       sum+=i
    print(sum)
natural(5) '''
# return larges of 3
'''
def big(a,b,c):
 if a>b and a>c:
   return a
 elif b>a and b>c:
   return b
 elif c>a and c>b:
   return c
 else:
   return 
print(big(10,15,5))    '''
#reverse a number
'''
def rev(num):
    res=0
    while num!=0:
       last=num%10
       res=res*10+last
       num//=10
    print(res)
rev(123)     '''
#count digits in a num
def cou(num):
    count=0
    while num!=0:
        count+=1
        num//=10
    print(count)
cou(94004)    