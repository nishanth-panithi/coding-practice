
#list
'''
num=[1,2,3,4,5,6,7,8,9]
out=[e for e in num if e%2==1]
print(out)'''
#
'''
name=["NIShanth"]
sen="this is a sentance in python"
upper=[a.upper() for a in name]
lower=[a.lower() for a in name]
title={a.title() for a in sen.split(" ")}
print(lower)
print(upper)
print(title)'''
#
'''
li=[[1,2],[3,4]]
out=[j for i in li for j in i]
print(out)'''
#dict
'''
num=[1,2,3,4,5,6,7,8,9,10]
out={i:i**2 for i in num if i%2==0}
print(out)'''
######
'''
str="python programming"
out={x:str.count(x) for x in str if x!=" "}
print(out)
max=0
char=" "
for i in out:
    if out[i]>max:
        max=out[i]
        char=i
print(max,char)'''
#
'''
dict={"a":"apple","b":"ball","c":"cat"}
out={dict[x]:x for x in dict} 
print(out)'''
#
'''
val={"a":10,
     "b":20,
     "c":30}
out={k:v for k,v in val.items() if v>20}
print(out)'''
#
'''
str="python programming"
vowel={x for x in str if x in "aeiou"}
print(vowel)''' 
#
'''
mul_5={x for x in range(1,101) if x%5==0}
print(mul_5)'''
#
'''
tech=["java","aws","ubantu","php","excel","python"]
vowel={x for x in tech if x[0] in "aeiou"}
print(vowel)'''
#
