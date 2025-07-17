# def total(*n):
#     print(n)
# total(1,2,3,4)

# def num(*n): 
#     print(sum(n))
# num(1,45,32,4) #multiple argument can take

# def greeting(**student):
#     print(f"my name is {student["name"]} and iam {student["age"]} years old")
# greeting(age=21,name="Jamshi") #using **name ,we can get in specific order if u not take arguments in randomly

def sample(a,b):
    return a,b
# print(sample(3,4)) #(3, 4)
c,b=sample(7,3) #unpacking,list can unpack
print(c,b) #7 3