#The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding numbers, starting from 0 and 1.
# The series begins as 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and continues infinitely.
# fib with times,

a=0
b=1
for i in range(10):
    print(a) #starts from 0, good
    c=a+b
    a=b
    b=c

#fib wiht times limits

a=0
b=1
limit=10
for i in range (limit):
    c=a+b
    a=b
    b=c
    print(a) #starts from 1 ,bad

#fib with number limit

a=0
b=1
while a<14:
    print(a)
    c=a+b
    a,b=b,c
