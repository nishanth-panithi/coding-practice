
# #list

# num=[1,2,3,4,5,6,7,8,9]
# out=[o for o in num if o%2==1]
# print(out)
'''
[1, 3, 5, 7, 9]
'''
# #

# name=["NIShanth"]
# sen="this is a sentance in python"
# upper=[a.upper() for a in name]
# lower=[a.lower() for a in name]
# title={a.title() for a in sen.split(" ")}
# print(lower)
# print(upper)
# print(title)
'''
['nishanth']
['NISHANTH']
{'In', 'This', 'A', 'Sentance', 'Is', 'Python'}
'''
# #

# li=[[1,2],[3,4]]
# out=[j for i in li for j in i]
# print(out)
'''
[1, 2, 3, 4]
'''
# #dict

# num=[1,2,3,4,5,6,7,8,9,10]
# out={i:i**2 for i in num if i%2==0}
# print(out)
'''
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
'''
# ######

# str="python programming"
# out={x:str.count(x) for x in str if x!=" "}
# print(out)
# max=0
# char=" "
# for i in out:
#     if out[i]>max:
#         max=out[i]
#         char=i
# print(max,char)
'''
{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}
2 p
'''

# dict={"a":"apple","b":"ball","c":"cat"}
# out={dict[x]:x for x in dict} 
# print(out)
'''
{'apple': 'a', 'ball': 'b', 'cat': 'c'}
'''
# #

# val={"a":10,
#      "b":20,
#      "c":30}
# out={k:v for k,v in val.items() if v>20}
# print(out)
'''
{'c': 30}
'''
# #

# str="python programming"
# vowel={x for x in str if x in "aeiou"}
# print(vowel) 
'''
{'o', 'a', 'i'}
'''
# #

# mul_5={x for x in range(1,101) if x%5==0}
# print(mul_5)
'''
{5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100}
'''

# #

# tech=["java","aws","ubantu","php","excel","python"]
# vowel={x for x in tech if x[0] in "aeiou"}
# print(vowel)
'''
{'aws', 'ubantu', 'excel'}
'''
# #
