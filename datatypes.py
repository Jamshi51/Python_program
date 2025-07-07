#number


#int
age=23
print(type(27))  # which datatype used

#float
n=3.45
print(type(n))

#complex
a=1+1j
print(type(a))

#string
name='jamshi'
print(type(name))
print(name[1])
#name[2]='s' # it is not work because does not change the value ,so it is immutable
print(name)



#list
my_list=[1,2,3,'python',[12,22]]
print(type(my_list))

#list orderd
my_list=[1,2,3,'python',[12,22]]
print(my_list[4][1]) #the result is 22
print(my_list[0:2])

# list  mutable
my_list=[1,2,3,'python',[12,22]]
my_list[1]=4  # change he value of 1th index with 4
print(my_list)

#tuple ordered,immutable
n=(1,2,3,'python',[12,22])
print(n[2])
#n[2]=5  # it is not work because it is immutable,that means it cant change the value with other
print(n)
s='jamshi'#this is not tuple,it is string

#set unordered,immutable,
k={1,2,1,'python','jamshi'}
print(k)   #the result is unordered and unique value that means repeated values print only once

#dictionary
dict={"name":"jamshi","age":23,"hobby":["art","coding"]}
print(dict["name"])
print(dict["hobby"][1]) # result=coding
dict["name"]="jaas"  # mutable
print(dict)
