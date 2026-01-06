'''*** second largest number in a list with using a max method'''

# list=[79,100,12,78,34,44]
# max1=max2=0
# for i in list:
#     if i>max1:
#       max1=i
# for j in list:
#     if j>max2 and j!=max1:
#       max2=j
# print(max2)

'''nth largest num using max method'''

# def highest(num,pos):
#     if len(num)<pos:
#         return "not possible"
#     else:
#         for i in range(1,pos):
#             num.remove(max(num))
#         return max(num)
# print(highest([34,44,45,87,57,67,23,49,24],5))

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

#----------------------------------------------------------

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
# word='swiss'
# count=0
# pos=2
# while count<pos:
#     for i in range(len(word)):
#         repeate=False 
#         for j in range(len(word)):
#             if i!=j and word[i]==word[j]:
#                 repeate=True
#                 break
#         if not repeate:
#             count+=1
#             if count==pos:
#                 print(word[i])
#                 break

#matrix multiplication 

# # mat1=[[5,8],
# #       [1,2]]       #5x4+8x9  5x3+8x7
# # mat2=[[4,3],
# #       [9,7]]       #1x4+2x9  1x3+2x7
# mat1=[[5,8,2],
#       [1,2,4]]
# mat2=[[4,3],
#       [9,7],
#       [2,3]]
# posible=True
# for x in mat1:
#     if len(x)!=len(mat2):
#         posible=False
# for y in mat2:
#     if len(y)!=len(mat1):
#         posible=False
# if posible:
#     res=[]
#     for i in range(len(mat1)):
#         row = []
#         for j in range(len(mat2[0])):
#             sum = 0
#             for k in range(len(mat2)):  # or len(mat1[0])
#                 sum += mat1[i][k] * mat2[k][j]
#             row.append(sum)
#         res.append(row)
#     print(res)
# else:
#     print("not posible to perfome")

# #

