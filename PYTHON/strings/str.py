'''check whether the character is num upp low'''

def check(char):
    asc=ord(char)
    if asc>=97 and asc<=122:
        print(f"given {char} is in lowercase")
    elif asc>=65 and asc<=90:
        print(f"given {char} is in uppercase")
    elif asc>=47 and asc<=58:
        print(f"given {char} is a number")
    else:
        print("enter a valid character")
check("A") 
''' replace vowel with next letter'''

def vowel(str):
    res=""
    for i in range(len(str)):
        asc=ord(str[i])
        if str[i] in "aeiouAEIOU":
        #if str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u" or str[i]=="A" or str[i]=="E" or str[i]=="I" or str[i]=="O" or str[i]=="U":
            res+=chr(asc+1)
        else:
            res+=str[i]
    print(res)
vowel("aehkio")
'''position of vowels'''

def vowelposition(str):
    for i in range(len(str)):
        if str[i] in "aeiouAEIOU":
            print(f"{str[i]} is in the index of {i+1}")
vowelposition("nishanth")

'''no of consonents'''

def consonents(str):
    count=0
    for i in range(len(str)):
        if str[i] not in "aeiouAEIOU":
            count+=1
    print(f"number of consonents in the string is {count}" )
consonents("nishanth")
'''add 2 strings alternatively'''

string1="acegik"
string2="bdfhjl"
res=""
for i in range(len(string1)):
    res+=string1[i]+string2[i]
print(res)   
''' with different length of strings'''

s1="13579"
s2="24688888"
res=""
big=s1
itr=len(s1)
if len(s2)>len(s1):
    itr=len(s2)
    big=s2
for i in range(itr):
    if i<len(s1) and i<len(s2):
        res+=s1[i]+s2[i]
    else:
        res+=big[i]
print (res)    
'''split'''

str="nishanth,nani"
print(str.split(","))
'''join'''

_list=["my","name","is","nishanth"]
print(" ".join(_list))    
'''return the longest word in the string'''

str="pythin is a high level programming language"
word=str.split(" ")
long=""
for i in range (len(word)):
    if len(long)<len(word[i]):
        long=word[i]
print (long, "is the longest word in the string")   
print (str.replace(long,"something"))  
'''position of a letter in a string'''

str="nishanth"
ltr="a"
for i in range(len(str)):
    if str[i]==ltr:
        print(ltr,"is in the index of",i)    
'''non repeated letters in a string'''

str="nishanth"
for i in range(len(str)):
    if str.count(str[i])==1:
        print(str[i]) 
'''UC->LC,LC->UC'''

str="NishantH"
for i in range(len(str)):
    if str[i]==str[i].upper():
        print(str[i].lower())
    else:
        str[i]==str[i].lower
        print(str[i].upper())  

'''filling 0 at the end'''

str="nishu"
print(str.zfill(10))

length=10
ascal=""
req=length-len(str)
for i in range(req):
    ascal+="0"
print(ascal+str)
'''count the upper case in the string'''

str="NishAntH"
count=0
for i in range(len(str)):
    ltr=ord(str[i]) 
    if ltr>=65 and ltr<=90:
        count+=1
print(f"there are {count} upper case letters in the string")
'''secreat'''

str="naniz"
src=""
for i in range(len(str)):
    ltr=ord(str[i])
    src+=chr(ltr+1)
print(src) 
'''ascd sub string'''

str="mahishmathi"
sub="hish"
word=False
for i in range(len(str)):
    sublen=len(sub)
    word=str[i:i+sublen]
    if (word==sub):
        print(sub,"is in str") 
        break
if word!=sub:
    print(sub,"is not in str")
'''ascd palindrome in a sentance'''

sen="my mom makes lunch"
word=sen.split(" ")
palindrome=False
for i in range(len(word)):
   if word[i]==word[i][::-1]:
      palindrome=True
      print(word[i],"palindrome")
if palindrome==False:
   print("no palindrome ")
'''sub palindrome'''

str="malayalam"
l=len(str)
for i in range(l):
    word=""
    for j in range(i,l):
        word+=str[j]
        if word==word[::-1] and len(word)>1:
            print(f"{word} is palindrome of {str} and it is present at {i}-{i+j-1}")
           
'''print longest palindrome'''

str="malayalai"
longest=""
i=0
while len(str)>i and len(str[i::])>len(longest):
    temp=""
    for j in range(i,len(str)):
        temp+=str[j]
        if temp==temp[::-1] and len(temp)>len(longest):
            longest=temp
    i+=1
print(longest)        

'''all in 1'''

str="malayalam"
l=len(str)
pal=[]
for i in range(l):
    word=""
    for j in range(i,l):
        word+=str[j]
        if word==word[::-1] and len(word)>1:
            pal.append(word)
            print(f"-{word}- is palindrome of {str} and it is present at {i}-{i+j-1}")
print("with duplicate",pal)
print("with out duplicate",set(pal))
short=min(pal)
long=max(pal)
print(f"-{long}- longest palindrome")
print(f"-{short}- shortest palindrome")
'''smallest palindrome'''

str="aabcdee"
spal=str
for i in range(len(str)):
    word=""
    for j in range(i,len(str)):
        word+=str[j]
        print(word)
        if (word==word[::-1]) and (1<len(word)) and (len(word)<len(spal)):
            spal=word
if spal!=str:
    print(spal,"is the smallest palindrome in this string")
else:
    print("there is no palindrome in this string")
'''count palindrome'''

str="malayalam"
count_pal=i=0
list=[]
while i<len(str):
    word=""
    for j in range(i,len(str)):
        word+=str[j]
        if word==word[::-1] and len(word)>1 and (word not in list):
            list.append(word)
            count_pal+=1
    i+=1
print(count_pal,list)
'''longest non repeative lettered word'''

word="abcdeasd"
longest=""
for i in range(len(word)):
    temp=""
    for j in range(i,len(word)):
        if word[j] in temp:
            break
        else:
            temp+=word[j]
            if len(temp)>len(longest):
                longest=temp
print(longest)
'''aabbcccddddd-->2a2b3c4d'''

word="aabbccccdddddd"
i=0
while i<len(word):
    count=1
    temp=""
    for j in range(i,len(word)-1):
        if word[j+1]==word[j]:
            count+=1
            temp+=word[j]
        else:
            break
    i+=count
    print(word[j],count)   

#  a 2
#  s 1
#  d 2
#  f 3
#  e 4

word="aasddfffeeee"
i=0
res=""
while i<len(word):
    count=1
    for j in range(i,len(word)-1):
        if word[j+1]==word[j]:
            count+=1
        else:
            break
    i+=count
    # print(word[j],str(count))
    # o/p
    # a 2
    # s 1
    # d 2
    # f 3
    # e 4
    res+=(word[j]+str(count))
print(res)