# v=lambda a,b:a+b #lambda arguments: expression
# print(v(23,30)) 

# # odd or even
# is_even=lambda n:True if n%2==0 else False
# print(is_even(4))
# #or
# is_even=lambda n:f"{n}is even"if n%2==0 else f"{n} is odd"
# n=int(input("enter the number : "))
# print(is_even(n))

# def squares(num):
#     return num**2

# number=[2,3,4,5]
# print(list(map(squares,number))) #iterable: A list, tuple, string, etc.
# #we can write this using lambda
# number=[3,2,4,5]
# # print(list(map(lambda a:a**2,number)))
# print(tuple(map(lambda a:a**2,range(1,11)))) # (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
#                                              # output will be in tuplre

# print(list(map(lambda a:True if a%2==0 else False,number))) #it only return true or false
#                                                             #[False, True, True, False]
# print(list(filter(lambda a:True if a%2==0 else False,number)))  #It returns only those elements for which the function returns True.
#                                                                 #[2,4]

# from functools import reduce #reduce() is part of the functools module.
# s=reduce(lambda a,b:a*b,range(1,6))
# print(s)

#sqr of numbers

sqr=lambda a:a**2
print(sqr(8))

# filter even numbers from 1 to 20