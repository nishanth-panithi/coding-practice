''' for i in range(10,0,-1):
    print(i) '''
    
mob=int(input("enter your mobile number:"))
count=0
while mob!=0:
    mob//=10  # mob=mob//10
    count+=1
if count==10:
    print("valid")
else:
    print("number not valid")

    