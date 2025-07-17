c=1
def sample():
    d=c+1 #if you're just reading the global variable, you don't need the global keyword.
    global c # You only need global if you want to modify the global variable
    c=d
    print(c)
sample()
# print(c)