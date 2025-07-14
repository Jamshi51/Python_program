#while loop
"""
while condition:
     stmt
"""
# count=1
# while count<=10:
#     print("hello")
#     count+=1     

#multiplication table
# n=int(input("enter the number : "))
# a=1
# while a<=10:
#     print(f"{a}*{n}={a*n}")
#     a+=1

#factorial
# n=int(input("enter the number : "))
# a=1
# b=1
# while b<=n:
#     a=a*b
#     print(a)
#     b+=1

#or
# n=int(input("enter the number : "))
# f=count=1
# while count<=n:
#     f=f*count
#     count+=1
# print(f)

#

while True:
    a=int(input("Enter the number : "))
    b=int(input("Enter the number : "))
    c=int(input("please enter your choice :\n1.addition \n2.subtraction\n3.multiplication\n4.division \nEnter your choice : "))
    if c==1:
     print(a+b)
    elif c==2:
     print(a-b)
    elif c==3:
     print(a*b)
    else:
     print(a/b)
    d=input("do you continue with this ?")
    if d=="yes":
      continue
    else:
      break
  
  



    


    