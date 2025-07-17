# def fun():
#     print("hello")
#     fun()  #repeat like a loop
# fun()

def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print(fact(5))