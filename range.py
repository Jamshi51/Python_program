# print(list(range(1,34,2))) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
# for k in range(1,10):
#     print(k)

#multiplication table
# n=int(input("enter the nymber :"))
# for k in range(1,11):
#     #print(f"{k}*{n}={k*n}")  #multiplication of 5
#     print(k*n) # 3,6,9,12,15,18,21,24,27,30

# write a program to write even number from 1 to 16
# for num in range(1,17):
#     if num%2==0:
#         print(num)

#print fruits name with starting letter  A from the list 
# list=["Apple","Banana","Mosambi","Plums","Avocado"]
# for k in list:
#     s=k.capitalize()
#     if(s.startswith("A")):
#             print(k)

#  print starting with wovels words from list
# w=["Apple","ball","eat","wolf"]
# for word in w:
#     if word[0].lower() in ["a","e","i","o","u"]:
#          print(word)

#print the count of every letters in a string
# s="java"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
     
#factorial of a number
# n=int(input("enter the number :"))
# k=1
# for num in range(1,n+1):
#     k=k*num
# print(k)

#
# for num in range(1,11):
#        if num==3:
#               continue
#        print(num)

# #
# for num in range(1,11):
#         if num==7:
#               break
#         print(num)

#
# for r in range(1,4):
#     for j in range(1,r+1):
#         print(j,end=" ") 

n=int(input("enter the number : "))
f=count=1
while count<=n:
    f=f*count

    