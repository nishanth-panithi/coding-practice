s=input("enter")
i=0
res=""
while i<len(s):
    r=""
    count=1
    for j in range(i,len(s)-1):
        if s[j+1]==s[j]:
            count+=1
        elif count==1:
            res+=s[i]
        res+=s[i]+str(count)
    i+=count
print(res)


    
# s = input("Enter string: ")
# result = ""
# count = 1
# for i in range(len(s)):
#     if s[i].isdigit(): #s[i].isdigit():
#         result += s[i]
#     else:
#         if i < len(s) - 1 and s[i] == s[i + 1]:
#             count += 1
#         else:
#             if count > 1:
#                 result += s[i] + str(count)
#             else:
#                 result += s[i]
#             count = 1
# print(result)