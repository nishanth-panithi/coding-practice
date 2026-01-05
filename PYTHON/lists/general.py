'''
list=[1,"A","B",2,"a","z"]
uc=[]
lc=[]
rem=0
for i in list:
    s=str(i)
    acs=ord(s)
    if acs>=97 and acs<=122:
        lc.append(s)
    elif acs>=65 and acs<=90:
       uc.append(s)  
    else:
        rem+=int(s)
l="".join(lc)   
u="".join(uc)     
print(f"{rem} is sum of num in list. {u} are in uc. {l} are in lc")     ''' 
#matrix multiplication 
'''
# mat1=[[5,8],
#       [1,2]]       #5x4+8x9  5x3+8x7
# mat2=[[4,3],
#       [9,7]]       #1x4+2x9  1x3+2x7
mat1=[[5,8,2],
      [1,2,4]]
mat2=[[4,3],
      [9,7],
      [2,3]]
posible=True
for x in mat1:
    if len(x)!=len(mat2):
        posible=False
for y in mat2:
    if len(y)!=len(mat1):
        posible=False
if posible:
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            s = 0
            for k in range(len(mat2)):  # or len(mat1[0])
                s += mat1[i][k] * mat2[k][j]
            row.append(s)
        print(row)
else:
    print("not posible to perfome")'''
#matrix add condition check
'''
m1=[[1,2],
    [3,4]]
m2=[[5,6],
    [7,8]]
cond=True
if len(m1)==len(m2):
    for i in range(len(m1)):
        if len(m1[i])!=len(m2[i]):
            cond=False
            break
else:
    cond=False
if cond:
    print("both are in same dimentoins")
else:
    print("both are not in same dimentoins")'''
#square
'''
m=[[1,2],
   [3,4]]
sqr=True
for i in m:
    if len(m)==len(i):
        pass
    else:
        sqr=False
        break
if sqr:
    print("given matrix is sqr")
else:
    print("given matrix is not sqr")
'''
#
'''
mat=[[1,2],
     [3,4],
     [5,6]]
res=[]
for i in range(len(mat[0])):
    row=[]
    for j in range(len(mat)):
        row.append(mat[j][i])
    res.append(row)
print(res)'''
