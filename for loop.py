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
# t=(1,2 ,2,"jamshi","python")
# for k in t:
#     print(k,end=" ") #1 2 2 jamshi python

keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
result = dict(zip(keys, values))
print(result)

# sum of 1 to10
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print("sum : ",sum)

# print only even numbers
# numbers=[1,5,3,7,8,4,2]
# for i in numbers:
#     if i%2==0:
#         print(i)


# multiplication table for 1 to 5

# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{j}*{i}={i*j}")
#     print()

# find a number from list

# 


secret_code=7
guess=int(input("Enter your guessed number : "))
while guess==secret_code:
    print("correct...you guessed it..")
    break
else:
    print("sorry...wrong guessing..!")