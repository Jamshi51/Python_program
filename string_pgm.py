# language='PYthon'
# new=language.upper()
# print(new)
# # we can write as
# print(language.upper())#write into caps
# print(language.lower())#into small
# print(language.capitalize())#only 1st letter will be caps
# print(language.swapcase())#swap the letter into small
"""
n=input("enter the name")
a=int(input("enter ur age"))
print("my name is {} iam {} yrs old".format(n,a))
"""

# language=" python "
# # print(language.startswith("p"))
# # print(language.endswith("n"))
# # print(language.strip()) #avoid space after and before string
# # 

# s="helooooooo"
# print(s.count("o")) # count of letters



#Extract the first and last character of a string:
text="Programming"
print(text[0],text[10])

#Reverse a string: 
print(text[ : :-1])

#Count occurrences of a specific character: 
print(text.count("m"))

# Replace spaces with underscores: 
sentence = "Python is fun to learn" 
print(sentence.replace(" ","_"))

# Check if a string is a palindrome:
word="malayalam"
print(word==word[ : :-1])