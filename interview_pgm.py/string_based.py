#Reverse words in a sentence → "I love Python" → "Python love I".
s="I love Python"
print(" ".join(s.split()[::-1]))

#Count number of digits, letters, spaces in a string.
# s="Hello  123"
# letter=0
# digit=0
# space=0
# for ch in s:
#     if ch.isalpha():
#         letter+=1
#     elif ch.isdigit():
#         digit+=1
#     else:
#         space+=1
# print("letters : ",letter)
# print("Digits : ",digit)
# print("Spaces : ",space)

# s1="hello"
# s2="earth"
# if sorted(s1)==sorted(s2):
#     print("Anagram")
# else:
#     print("Not anagram")
    
# #Find the first non-repeating character in a string
# s="hhellloooot"
# for ch in s:
#     if s.count(ch)==1:
#         print(ch)
#         break

#Find the largest and smallest number in a list
l=[56,78,90,20]
# larg=l[1]
# small=l[0]
# for n in l:
#     if n>larg:
#         print("largest : ",n)
#     elif n<small:
#         print("smallest" ,n)
# print(max(l))
 
#  find out common letter
# a="NAINA"
# b="ALEENA"
# list1=set(a)
# list2=set(b)
# print(list1.intersection(list2))

#frequency count
# n="sheena loves eating apple and mango.her sister also loves eating apple and mango"
# li=n.split()
# d={}
# for i in li:
#     if i not in d.keys():
#        d[i]=0
#     d[i]+=1
# print(d)

# str="Hello"
# freq={}
# for char in str:
#     if char in freq:
#         freq[char]+=1
#     else:
#         freq[char]=1
# print(freq)

# n="sheena loves eating apple and mango.her sister also loves eating apple and mango"
# li=n.split()
# d={}
# for char in li:
#     if char in d:
#         d[char]+=1
#     else:
#         d[char]=1
# print(d)

#2 list into dictionary
# l1=["jamshi","jasir","aysha"]
# l2=[90,95,100]
# dic=dict(zip(l1,l2))
# print(dic)

#palindrome with slicing
# def pal(n):
#     if n[:]==n[::-1]:
#         print("palindrome")
#     else:
#         print("not" )
# pal("malayalam")



# def is_palindrome(s):
#     rev = ""
#     for ch in s:
#         rev = ch + rev   # build reversed string
#     if s==rev:
#         print("palidrome")
#     else:
#         print("not")
# is_palindrome("racecar")
# is_palindrome("python")

#prime or not
# def prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime")
                
#             else:
#                 print("prime")
#             break
#     else:
#         print("not prime")
# prime(4)
  

  #factorial using for
# n=int(input("enter the number"))
# k=1
# for i in range(1,n+1):
#     k=k*i
# print("factorial : ",k)

#using while
# n=int(input("enter the number"))
# k=1
# i=1
# while i<=n:
#     k=k*i
#     i+=1
# print(k)


# #using recursion

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))


#amstrong number
# n=153
# s=str(n)
# l=len(s)
# a=0
# for i in s:
#     a=a+int(i)**l
# print(a)

#fibonacci
# a,b=0,1
# for i in range(10):
#     print(a,end=" ")
#     a,b=b,a+b

#vowels
# s="hellooo jamshi"
# v="aeiou"
# s.lower()
# l=[]
# for i in s:
#     if i not in v:
#        l.append(i)
# print("consonents : ",l)
    
#count
# s="hellooo jamshi"
# v="aeiou"
# v_count=0
# c_count=0
# for i in s:
#     if i in v:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)


#perfect number
# def pr(num):
#     sum=0
#     for i in range(1,num):
#         if num % i==0:
#             sum+=i
#     if sum==num:
#             print("perfect number")
#     else:
#             print("not perfect")
# pr(6)

#digit sum
# n=1234
# s=str(n)
# l=len(s)
# total=0
# for i in range(l):
#      total=total+int(i)
#      total+=1
# print(total)      