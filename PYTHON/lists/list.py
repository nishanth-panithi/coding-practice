#*** second largest number in a list with using a max method
'''
list=[79,100,12,78,34,44]
max1=max2=0
for i in list:
    if i>max1:
      max1=i
for j in list:
    if j>max2 and j!=max1:
      max2=j
print(max2)'''
#nth largest num using max method
'''
def highest(num,pos):
    if len(num)<pos:
        return "not possible"
    else:
        for i in range(1,pos):
            num.remove(max(num))
        return max(num)
print(highest([34,44,45,87,57,67,23,49,24],5))'''
#in a simple way
'''
pos=2
num=[3,6,2,8,3,7,3,4,5,3,5,4]
for i in range(pos-1):
    num.remove(max(num))
print(max(num))'''
#remove dublicates numbers
'''
num=[3,6,2,8,3,7,3,4,5,3,5,4,4,7,7,6,5,3,3,4,5,6,8,0,5,3,3,0,9]
unq=[]
for i in num:
    if i not in unq:
        unq.append(i)
print(unq)'''
#max num with out using a max method
'''
num=[3,6,2,3,7,3,4,5,3,5,4]
temp=0
for i in num:
   if temp<i:
      temp=i
print(temp)'''
#sum of all num in a list with out sum methods
'''
num=[3,6,2,3,7,3,4,5,3,5,4]
temp=0
for i in num:
      temp+=i
print(temp)'''
##count the repeated numbres
# n=[3,5,4,4,7,7,7,6,5,3,3,]
# count=1
# res=""
# for i in range(len(n)):
#     if n[i+1]==n[i]:
#         count+=1
#     else:
#         if count==1:
#             res+="one"+n[i]+" "
#         elif count==2:
#             res+="double"+n[i]+" "
#         elif count==3:
#             res+="tripple"+n[i]+" "
#             break
#     i+=count
# print(res)
#nestedlists ,sum of all nums in lists and nested lists
'''
nested=[1,[2,3]]
sum=0
for i in nested:
    if isinstance(i,list):
        for j in i:
            sum+=j
    else:
        sum+=i
print(sum)'''
#max val
'''
nested=[[1,20],[3,4],[4,50]]
max=0
for i in nested:
    for j in i:
        if max<j:
            max=j
print(max)'''   

#max sum val and max list from a list
'''
nested=[[1,20],[3,4],[4,5]]
maxlist=0
maxval=0
for i in nested:
    temp=0
    for j in i:
        temp+=j
    if temp>maxval:
        maxval=temp
        maxlist=i
print(maxval,maxlist)'''
