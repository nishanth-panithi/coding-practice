#armstrong,ex: 153 => 1³+5³+3³ = 1+125+27 = 153

num3,num2,num=int(input("enter num here :"))
#find number of digites.
count=0
while num!=0:
    num=num//10
    count+=1
# seperate last digit and perform roots and, remove last digit.
total=0
while num2!=0:
    last=num2%10
    total+=last**count
    num2=num2//10
if total==num3:
    print("armstrong")
else:
    print("not an armstrong")
