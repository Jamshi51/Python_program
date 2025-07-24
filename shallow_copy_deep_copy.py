#shalllow copy
#Changes affect both copies
import copy
my_list=[[1,2,3],["jamshi","jaas"]]
g=copy.copy(my_list)
g[0][0]=21
print(g)       #[[21, 2, 3], ['jamshi', 'jaas']]
print(my_list) #[[21, 2, 3], ['jamshi', 'jaas']]

#deep copy
#Changes only affect deep copy
import copy
my_list=[[1,2,3],["jamshi","jaas"]]
g=copy.deepcopy(my_list)
g[0][0]=21
print(g)      #only update changed g ,[[21, 2, 3], ['jamshi', 'jaas']]
print(my_list) #[[1, 2, 3], ['jamshi', 'jaas']]
