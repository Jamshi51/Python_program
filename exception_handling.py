# a,b=10,0
# try:
#     c=a/b
#     print(c)
# #except Exception: #to handle exception
# except Exception as e:  
#     print(e)
#     print("not valid")
# print("program executed")

# a,b=10,0
# try:
#     c=a/j
#     print(c)
# # except NameError:
# #     print("value not found")

# except Exception as e:
#     print("error",e)

# a,b=map(int,input("enter 2 numbers : ").split()) #
# try:
#      c=a/b
#      print(c)
# #except Exception: #to handle exception
# except Exception as e:  
#      print(e)
#      print("not valid")
#finally:  #always work if error occured
#   print("program executed")
# else: # work only condition is true
#     print("program executed")


# a,b=map(int,input("enter 2 numbers : ").split()) #enter the value in one line
# print(a+b)
while True:
    a,b=map(int,input("enter 2 numbers : ").split())
    try:
      c=a/b
      print(c)
    except exception as e:
      print("error",e)
    



