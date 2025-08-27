'''
Operator overloading allows the same operator to have different
behavior depending on the type of operands.
'''
class myclass:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def __add__(self,other):
        #self=ob1
        #other=ob2
        return myclass(self.a+other.a,self.b+other.b)
ob1=myclass(43,3)
ob2=myclass(2,4)
v=ob1+ob2
print("a : ",v.a,"b : ",v.b)