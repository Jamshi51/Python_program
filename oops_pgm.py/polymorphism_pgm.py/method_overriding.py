'''
A child class defines a method with the same name and signature as a method in its parent class,
 thereby replacing the parent's version.

 '''
class Parent():
    def fun(self):
        print("parent : hii")
class Child(Parent):
    def fun(self):
        print("Child : Hellooo") # replace with parent's version
c=Child()
c.fun()