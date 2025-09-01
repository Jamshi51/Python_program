#Use logical operators to check if a number is between 1 and 100
n=1001
if n>=1 and n<=100:
    print(f"{n} b/w 1 and 100")
else:
    print("Not b/w 1 and 100")

#Find common elements in two lists using in
n1=[1,3,2,4]
n2=[2,4,7,8]
common=[]
for i in n1:
    if i in n2:
        common.append(i)
print(common)
