# update
# d={"name":"jamshi","age":23,"hobby":["art","coding"]}
# d.update({"wt":"wd"})
# print(d) #{'name': 'jamshi', 'age': 23, 'hobby': ['art', 'coding'], 'wt': 'wd'}

# #pop
# d={"name":"jamshi","age":23,"hobby":["art","coding"]}
# print(d.pop("name")) #print deleted item ,jamshi
# #print(d) #{'age': 23, 'hobby': ['art', 'coding']}
# d.popitem() # print after deletion
# print(d)


# d={"name":"jamshi","age":23,"hobby":["art","coding"]}
# print(d.get(5,"default")) # index 5 is not exist,so print the dafault


#Create a dictionary mapping student names to their grades using zip().
# name=["jamshi","jasir","aysha"]
# grade=[90,95,100]
# display=dict(zip(name,grade))
# print(display)


# Combine two lists of numbers using zip() and calculate their sum.
# list1=[2,4,1,5]
# list2=[4,3,2,1]
# sum=[a+b for a,b in zip(list1,list2)]
# print(sum)

#Unzip a zipped object into individual lists.
zipped=[("jamshi",90),("jaas",96)]
name,grade=zip(*zipped)
name=list(name)
grade=list(grade)
print("name : ",name)
print("grade : ",grade)