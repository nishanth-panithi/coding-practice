'''nth largest num in a list with out using any method'''
# pos=4
# list=[79,100,55,34,64,25]
# count=0
# while count<pos:
#     newlist=[]
#     max=0
#     for i in list:
#         if max<i:
#             max=i
#     for j in list:
#         if j!=max:
#             newlist+=[j]
#     list=newlist
#     count+=1
# print(max)
'''same but in function'''
# def nmax(list,pos):
#     count=0
#     while count<pos:
#         newlist=[]
#         max=0
#         for i in list:
#             if max<i:
#                 max=i
#         for j in list:
#             if j!=max:
#                 newlist+=[j]
#         list=newlist
#         count+=1
#     return max
#     print(max)
# nmax([79,100,55,34,64,25],3)


'''aabbcccddddd-->2a2b3c4d'''

# word="abbccccd"
# i=0
# res=""
# while i<len(word):
#     count=1
#     for j in range(i,len(word)-1):
#         if word[j+1]==word[j]:
#             count+=1
#         else:
#             break
#     if i==len(word)-1 and word[i-1]!=word[i]:
#         res+=word[i]+str(count)
#     else: 
#         res+=word[j]+str(count) 
#     i+=count
# print(res)
##o/p
##a2b2c4d1


# word="aasddfffeeee"
# i=0
# res=""
# while i<len(word):
#     count=1
#     for j in range(i,len(word)-1):
#         if word[j+1]==word[j]:
#             count+=1
#         else:
#             break
#     i+=count
#     # #print(word[j],str(count))
#     # o/p
#     # a 2
#     # s 1 
#     # d 2
#     # f 3
#     # e 4
#     res+=(word[j]+str(count))
# print(res) 
#o/p
#a2b2c4d6

'''first non-repeative letter'''
# word='swiss'
# for i in range(len(word)):
#     res=True 
#     for j in range(len(word)):
#         if i!=j and word[i]==word[j]:
#             res=False
#             break
#     if res:
#         print(word[i])
#         break
'''same with a pos'''
word='swiss'
count=0
pos=2
while count<pos:
    for i in range(len(word)):
        repeate=False 
        for j in range(len(word)):
            if i!=j and word[i]==word[j]:
                repeate=True
                break
        if not repeate:
            count+=1
            if count==pos:
                print(word[i])
                break
