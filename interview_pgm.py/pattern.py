# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#or
# for i in range(0,6):
#     print("* "*i)
# '''
# *  
# *  *  
# *  *  *  
# *  *  *  *  
# *  *  *  *  *  
# ''' 

# n=5
# k=1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     k=k+2
#     print()
# '''
# * 
# * * * 
# * * * * * 
# * * * * * * * 
# * * * * * * * * * 
# '''

# for i in range(0,6):
#     print(" "*(5-i),"* "*i)
# '''
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# '''
# for i in range(0,8):
#     print(" "*(7-i),"* "*i)
# for j in range(6,0,-1):
#     print(" "*(7-j),"* "*j)

'''
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
  * * * * * * 
   * * * * * 
    * * * * 
     * * * 
      * * 
       *
'''
# for i in range(6,0,-1):
#     print("* "*i)
'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
# for i in range(5,0,-1):
#   print(" "*(5-i),"*"*i)

'''
   *****
    ****
     ***
      **
       *
'''
# for i in range(1,6):
#   for j in range(1,i+1):
#    print(i,end=" ")
#   print()
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

# for i in range(1,6):
#   for j in range(1,i+1):
#    print(j,end=" ")
#   print()
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

# for i in range(5,0,-1):
#   for j in range(1,i+1):
#    print(j,end=" ")
#   print()

'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
'''

# for i in range(1,6):
#   print(" "*(5-i),end=" ")
#   for j in range(1,i+1):
#     print(j,end=" ")
#   print()

# n = 10
# num = 1
# for i in range(1, n+1):
#     c=1
#     while c<=i:
#         if num % 2 == 0:
#             print(num, end=" ")
#             c+=1
#         num += 1   # always increase num
#     print()


# n=6
# num=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=2
#     print()

'''
2 
4 6 
8 10 12
14 16 18 20
22 24 26 28 30
32 34 36 38 40 42
'''

# n=6
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=2
#     print()
'''
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
31 33 35 37 39 41
'''


# n=6
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num*5,end=" ")
#         num+=2
#     print()
'''
5 
10 15 
20 25 30
35 40 45 50
55 60 65 70 75
80 85 90 95 100 105

'''
# n=6
# num=1
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=2
#     print()
'''   1
     3 5
    7 9 11
   13 15 17 19
  21 23 25 27 29
 31 33 35 37 39 41'''

# ch=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1

#     print()
'''
A
B C
D E F
G H I J
K L M N O'''

# ch=65
# for i in range(1,6):
#     print(" "*(5-i),end=" ")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1

#     print()
'''
     A
    B C
   D E F
  G H I J
 K L M N O'''

for row in range(7):
    for col in range(5):
        if (col==2) or ((row==0)and(col!=2))or ((row==6) and(col<2) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

''' * * * * * 
    *     
    *
    *
    *
    *
* * *
'''





