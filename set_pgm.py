#add()
# s={1,2 ,2,"jamshi","python"}
# s.add(3)
# print(s)
# #update()
# s={1,2 ,2,"jamshi","python"}
# s.update(("we",2))
# print(s)  #{1, 2, 'we', 'python', 'jamshi'}

# #remove()
# s={1,2 ,2,"jamshi","python"}



# Create a set of unique student names from a list. 
# Then perform union, intersection, and difference operations on two sets of numbers. 
# Finally, check if one set is a subset of another.

list=["jamshi","jasi","aysha","harsha"]
name=set(list)
print(name)

set1={1,4,3,2}
set2={1,4,3,2,6}
union=set1|set2
intersection=set1 & set2
difference=set2-set1 
print("Union : ",union)
print("intersection : ",intersection)
print("difference : ",difference)
print("set1 is subset of set2 ? True or False : ",set1.issubset(set2))
