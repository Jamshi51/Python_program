#read
# file=open("task_pgm.py","r")
# print(file.read())

# #write
# file=open("test_file.txt","w")
# file.write("onetm")

# #append
# file=open("test_file.txt","a")
# file.write(" jamshi \n")


# with open("test_file.txt","a") as file:
#    file.write(" jamshi \n")


# try:
#    with open("test_file.txt","r") as file:
#       print(file.read())
# except FileNotFoundError:
#    print("Invalid....")


# truncate
# with open("test_file.txt","w") as file:
#    file.truncate(0)

with open("test_file.txt","w") as file:
 file.write(" jamshi \n")
