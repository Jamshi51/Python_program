#list
# l=[23,24,3,5,45]
# # for k in list:
# #     # #print(k)  23
# #     #            24
# #     #            3
# #     #            5
# #     #            45
# #     # print(k,end=" ") #23,24,3,5,45
# print(list(enumerate(l,1))) #[(1, 23), (2, 24), (3, 3), (4, 5), (5, 45)]
# for c,k in enumerate(l,6):
#     print(c,k) #output->0 23
                        # 1 24
                        # 2 3
                        # 3 5
                        # 4 45

#sring
# s="jamshi"
# for m in s:
#     print(m,end=" ")

#dictionary
# d={"name":"jamshi","age":23,"hobby":["art","coding"]}
# # for w in d:
# #     print(d[w],end=" ") #jamshi 23 ['art', 'coding']
# # print(" ") #break the output
# # for w in d.items(): #('name', 'jamshi') ('age', 23) ('hobby', ['art', 'coding']) 
# #     print(w,end=" ")
# # for w in d.values(): # only values print ,jamshi 23 ['art', 'coding'] 
# #     print(w,end=" ")
# # for w in d.keys():  #only keys print
# #     print(w,end=" ")
# # for w,value in d.items(): # name jamshi
# #                             # age 23
# #                             # hobby ['art', 'coding']
# #     print(w,value)

#     #OR
# for w in d:
#     print(w,d[w]) # same output

# #tuple
t=(1,2 ,2,"jamshi","python")
for k in t:
    print(k,end=" ") #1 2 2 jamshi python

keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
result = dict(zip(keys, values))
print(result)

