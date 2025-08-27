#Reverse words in a sentence → "I love Python" → "Python love I".
s="I love Python"
print(" ".join(s.split()[::-1]))

#Count number of digits, letters, spaces in a string.
# s="Hello  123"
# letter=0
# digit=0
# space=0
# for ch in s:
#     if ch.isalpha():
#         letter+=1
#     elif ch.isdigit():
#         digit+=1
#     else:
#         space+=1
# print("letters : ",letter)
# print("Digits : ",digit)
# print("Spaces : ",space)

s1="hello"
s2="earth"
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not anagram")
    
#Find the first non-repeating character in a string
s="hhellloooot"
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break

#Find the largest and smallest number in a list
l=[56,78,90,20]
larg=l[1]
small=l[0]
for n in l:
    if n>larg:
        print("largest : ",n)
    elif n<small:
        print("smallest" ,n)
 