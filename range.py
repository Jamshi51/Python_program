# print(list(range(1,34,2))) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
# for k in range(1,10):
#     print(k)

#multiplication table
# n=int(input("enter the nymber :"))
# for k in range(1,11):
#     #print(f"{k}*{n}={k*n}")  #multiplication of 5
#     print(k*n) # 3,6,9,12,15,18,21,24,27,30

# write a program to write even number from 1 to 16
# for num in range(1,17):
#     if num%2==0:
#         print(num)

#print fruits name with starting letter  A from the list 
list=["Apple","Banana","Mosambi","Plums","Avocado"]
for k in list:
    s=k.capitalize()
    if(s.startswith("A")):
            print(k)


    