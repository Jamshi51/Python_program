# evens=[k for k in range(1,17) if k%2==0]
# print(evens) #[2, 4, 6, 8, 10, 12, 14, 16]
#List comprehension is a short and elegant way to create a list from an iterable (like a list, range, or string) using a single line of code.


# sqrs using list comprehension
# sqr=[a**2 for a in range(1,11)]
# print(sqr)


# text="Python Programming is fun!"
# vowels="AEIOUaeiou"
# vowel_list=[c for c in text if c in vowels]
# print(vowel_list)

# filter even numbers from 1 to 20
filter_even=[n for n in range(1,21) if n%2==0]
print(filter_even)