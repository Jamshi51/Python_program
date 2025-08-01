'''
Abstraction means hiding the internal implementation details and 
showing only the essential features to the user.

'''
from abc import ABC,abstractmethod # Importing for abstract class
class Parent(ABC): # Abstract class
    @abstractmethod
    def fun(self):
        pass
class child(Parent):
    def display(self):
        print("Hiii")
    def fun(self):    # Must be implemented
        print("Helllooooooooooooooo")
c=child()
c.display()
c.fun()