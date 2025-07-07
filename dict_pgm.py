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


d={"name":"jamshi","age":23,"hobby":["art","coding"]}
print(d.get(5,"default")) # index 5 is not exist,so print the dafault
