# numbers=[56,2,4,6,2,1,10,3]
# length=len(numbers)
# for k in range(length):
#     for j in range(length-k-1):
#         if numbers[j]>numbers[j+1]:
#             numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
#     print(numbers)
# print(numbers)

n=[3,2,7,1,4]
length=len(n)
for i in range(length):
    for j in range(length-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)