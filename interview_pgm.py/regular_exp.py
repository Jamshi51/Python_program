# import re

# # p=r'[A-Z0-9]'
# # s='Jam67shi89'

# # print(re.findall(p,s))

# p=r"[A-Za-z0-9]+@[A-Za-z]+\.(com|in)"
# email=input("Ente your mail : ")

# if re.match(p,email):
#     print('Valid')
# else:
#     print('Not valid')




# import re
# text="hello world"
# result=re.match("hello",text)
# print("match found",result.end())



#search
# import re
# text="hello world"
# result=re.search(" ",text)
# print("search found : ",result.start())


#findall
# import re
# text="hello world"
# result=re.findall("hello",text)
# print(result)

#sub
# import re
# text="hello world"
# result=re.sub("hello","hiii",text)
# print(result)


#split
# import re
# text="apple banana;orange grapes"
# result=re.split("[ ;]",text)
# print(result)


#password validation
import re
password=input("Enter your password : ")
p=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^+=!])[A-Za-z0-9@#$%^+=!]{8,}$"
if re.match(p,password):
    print("Strong password")
else:
    print("Week password")



