#1
'''
rows=5
col=5
for i in range(1,rows+1):
    pattran=""
    for j in range(1,col+1):
        pattran+="*"+" "
    print(pattran)  '''
''' 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
#2
'''
rows=5
for i in range(1,rows+1):
    ptrn=""
    for j in range(1,i+1):
        ptrn+="*"+" "
    print(ptrn)    '''
'''
* 
* * 
* * * 
* * * * 
* * * * *  '''
#3
'''
ows=5
for i in range(1,rows+1):
    ptrn=""
    for j in range(1,i+1):
        ptrn+=str(j)+" "
    print(ptrn) '''
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''
#4
'''
rows=4
num=2
for i in range(rows):#0,1,2,3,4
    res="" 
    for j in range(i+1):
        res+=str(num)+" "
        num+=2
    print(res)  ''' 
'''
2 
4 6 
8 10 12 
14 16 18 20 '''
#5
'''
rows=5
for i in range(rows):#01234
    res=""
    for j in range(i+1):
        res+=str(rows)+" "
    rows=rows-1
    print(res)'''
'''
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1  '''
#6
'''
rows=5
for i in range(rows,0,-1):#54321
    res="" 
    for j in range(i):
        res+=str(rows)+" "
    rows-=1
    print(res)'''
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 '''
#7
'''
rows=5
for i in range(1,rows+1):#12345
    res=""
    for j in range(1,rows+1):
       if i==1 or i==rows or j==1 or j==rows:
        res+="*"+" "
       else:
          res+=" "+" "  
    print(res)      '''
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * '''
#8
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows):
        if i==1 or i==rows or j==1:
            res+="*"+" "
    print(res)    '''
'''
* * * * 
* 
* 
* 
* * * * '''
#9
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows):
        if i==1 or i==rows or i==(rows//2)+1 or j==1:
            res+="*"+" "
    print(res)    '''
'''
* * * * 
* 
* * * * 
* 
* * * * '''
#10
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res) '''
'''
* * * * * 
    *     
    *     
    *     
* * * * * '''
#11
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==j or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)         '''
'''
*       * 
  *   *   
    *     
  *   *   
*       *  '''
#12
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)            '''
'''
*       * 
*       * 
* * * * * 
*       * 
*       * '''
#13
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or j==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res) '''
'''
* * * * * 
    *     
    *     
    *     
    *        '''
#14
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res) '''
'''
*       * 
* *     * 
*   *   * 
*     * * 
*       *     '''
#15
'''
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)'''
'''
* * * * * 
      *   
    *     
  *       
* * * * * '''
#16
'''
rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=mid:
            if i==1 or i==mid or j==1:
                res+="*"+" "
            else:
                res+=" "+" "    
        else:
            if i==rows or j==rows:
               res+="*"+" "
            else:
               res+=" "+" "   
    print(res) '''
'''
* * * * * 
*         
* * * * * 
        * 
* * * * * '''
#17
'''
rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=mid:
            if i==1 or i==mid or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "    
        else:
            if i==rows or j==1:
               res+="*"+" "
            else:
               res+=" "+" "   
    print(res)'''
'''
* * * * * 
        * 
* * * * * 
*         
* * * * * '''
#18
'''
rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==mid or i==rows or j==rows:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)'''
'''
* * * * * 
        * 
* * * * * 
        * 
* * * * *'''
#19
'''
rows=5
for i in range(1,rows+1):
    res=""
    for s in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)'''
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * '''
#20
'''
rows=5
for i in range(rows,0,-1):
    res=""
    for s in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)'''
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * '''
#21
'''
rows=5
for i in range(1,rows+1):
    res=""
    for space in range(rows-i):
        res+=" "
    for j in range(1,i+1):
        if i==j or i==rows or j==1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)'''
'''
    * 
   * * 
  *   * 
 *     * 
* * * * * '''
#22
'''
rows=5
for i in range(1,rows):
    res=""
    for s in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)
for i in range(rows,0,-1):
    res=""
    for s in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)

# row=5
# for i in range(1,2*row):
#     res=""
#     spa=row-i if i<=row else i-row
#     col=i if i<=row else 2*row-i
#     for s in range(spa):
#         res+=" "
#     for j in range(col):
#         res+="*"+" "
#     print(res)

# row=5
# for i in range(1,2*row):
#     res=""
#     spa=row-i if i<=row else i-row
#     col=i if i<=row else 2*row-i
#     res+=(" "*spa)+("* "*col)
#     print(res)'''
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * '''
#23
'''
rows=5
for i in range(rows,0,-1):
    res=""
    for s in range(rows-i):
        res+=" "
    for j in range(i):
        res+="*"+" "
    print(res)    
for i in range(2,rows+1):
    res=""
    for s in range(rows-i):
        res+=" "
    for j in range(i):
        res+="*"+" "
    print(res)
# rows=5
# for i in range(rows,0,-1):
#     res=""
#     for s in range(rows-i):
#         res+=" "
#     for j in range(i):
#         res+="*"+" "
#     print(res)
# for i in range(1,rows):
#     res=""
#     for s in range(1,rows-i):
#         res+=" "
#     for j in range(i+1):
#         res+="*"+" "
#     print(res)

# row=5
# for i in range(1,2*row):
#     res=""
#     spa=i-1 if i<=row else 2*row-i-1
#     col=row-spa
#     res=(" "*spa+"* "*col)
#     print(res)'''
'''
* * * * *
 * * * * 
  * * * 
   * * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * '''
#24

row=5
code=97
for i in range(1,2*row):
    res=""
    spa=row-i if i<=row else i-row
    col=i if i<=row else 2*row-i
    res+=" "*spa
    for j in range(col):
        res+=chr(code)+" "
        code+=1
    print(res)
'''
    a 
   b c 
  d e f 
 g h i j 
k l m n o 
 p q r s 
  t u v 
   w x 
    y '''