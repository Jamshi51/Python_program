# pattern printing
# row=int(input("enter the number : "))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
"""
#output
* 
* *
* * *
* * * *
* * * * *
"""

# for k in range(5,0,-1):
#     print("*"*k)
# """
# output

# *****
# ****
# ***
# **
# *
# """
# for r in range(1,6):
#      print(" "*int(5-r),"*"*r," "*int(5+r))
#or
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)
# """
# output

#      *
#     **
#    ***
#   ****
#  *****
# """
# print(list(range(5,0,-1))) #[5, 4, 3, 2, 1]

# for r in range(1,5):
#     num=r
#     for k in range(r):
#         print(num,end=" ")
#         num=num+r
#     print()
#     #or
# for r in range(1,5):
#     for k in range(1,r+1):
#         print(r*k,end=" ")
#     print()

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
        for j in range(i+1):
            print("*",end=" ")
    print()
    

#Create python code for displaying the following patterns 
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
# n=5
for r in range(5,0,-1):
    print(" "*int(5-r),"* "*r)

for i in range(0,6):
    print(" "*(5-i),"* "*i)
'''
    #output
     *
    * *
   * * *
  * * * *
 * * * * *

''' 
n=5
for i in range(0,6):
    print(" "*(5-i),"* "*i)       
for r in range(4,0,-1):
    print(" "*int(5-r),"* "*r)

'''

     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *       
'''
    


    

    
