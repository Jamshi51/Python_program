#reverse list
a=[1,2,3]
a.reverse()
print(a)
print(a[::-1])
print(list(reversed(a)))

#reverse a string
s="hello"
print(s[::-1])
print(" ".join(reversed(s)))
rev=" "
for ch in s:
    rev=ch+rev
print(rev)

#using integer
n=1234
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)