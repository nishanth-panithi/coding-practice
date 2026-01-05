'''
mob=9550230488
rev_num=0
while mob!=0:
    last_num=mob%10
    rev_num=(rev_num*10)+last_num
    mob=mob//10
print(rev_num)    '''
#same but easy to undestand
num=int(input("enter number"))
rev=0
while num!=0:
    last=num%10
    rev=rev*10+last
    num=num//10
print(rev)