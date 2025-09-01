#Find the largest element
arr = [10, 20, 4, 45, 99]
print(max(arr))

#smallest element
print(min(arr))

#2nd largest
arr = [10, 20, 4, 45, 99]
li=list(set(arr))
li.sort()


print("2nd largest numer is",li[-2])


#revrese:
print(arr[ : :-1])

#sort
arr.sort()
print(arr)

#sorting revrse
arr.sort(reverse=True)
print(arr)

#frequency count
arr = [10, 20, 4,10, 45, 99,99]
d={}
for num in arr:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
print(d)


#missing number in array
arr=[1,2,4,5,6]
n=max(arr)
ex_sum=n*(n+1)//2
act_sum=sum(arr)
print(ex_sum-act_sum)