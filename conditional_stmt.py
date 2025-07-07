"""
# if

syntax
if :
   stmt

"""
# if
# age=18
# if age>=18:
#     print("eligible to vote")

# a=4
# if a>0:
#     print("positive")

# #if else
# n=int(input("Enter the number :"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

#if_elif_else
# n=int(input("Enter the number :"))
# if n>=90:
#     print("Grade=A")
# elif n>=80:
#     print("Grade=B")
# elif n>=70:
#     print("Grade=C")
# elif n>=60:
#     print("Grade=D")
# else:
#     print("Grade=F")


# nested_if
age=int(input("Enter ur age :"))
ctz=(input("Enter the city :"))
if age>=18:
    if ctz=="india":
       print("Eligible for vote")
    else:
        print("you are not a citizen ,not eligible")
else:
    print("Not eligible")



