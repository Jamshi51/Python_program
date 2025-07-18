# def fun():
#     print("hello")
#     fun()  #repeat like a loop
# fun()

# def fact(num):
#     if num==1:
#         return num
#     else:
#         return num*fact(num-1)
# print(fact(5))

#reversing of string
def rev(s):
    if len(s)==0:
        return s
    else:
        return rev(s[1: ])+s[0]
print(rev("jamshi")) #ihsmaj