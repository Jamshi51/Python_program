'''
A decorator in Python is a function that modifies the behavior of another function
without changing its code.

'''
# def dec(fun): #decorated fun
#     def wrapper(msg):  #wrapper function
#         a=msg.upper()  #convert input to upper case
#         fun(a)      #call original function with modified input
#     return wrapper   #return wrapper function
# @dec     #apply decorator
# def say_hello(m):  #original function
#     print(m)
# say_hello("hello...")  # call the decorated fun



#2
#subtraction
# def dec(fun):
#     def wrapper(a,b):
#         if a<b:
#           a,b=b,a
#         fun(a,b)
#     return wrapper
# @dec
# #instead
# # g=dec(greeting)
# # print(g)
# # g("helloo...)
# def subtract(a,b):
#     print(f"subtracted result : {a}-{b} = {a-b}")
# subtract(60,50)

def login_required(fun):
    def wrapper(args):
        if args.get("is _authenticated"):
            fun(args)
        else:
            print("Permission denied \nPlease login")
    return wrapper
@login_required
def Home(user):
    print("welcome",user.get("name"))
Home({"name":"jamshi","is_authenticated":False})
    