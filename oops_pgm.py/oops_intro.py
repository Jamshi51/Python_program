'''
Object-Oriented Programming System (OOPs) is a programming approach that organizes software design around objects, rather than functions or logic.
It uses classes and objects to model real-world things and their interactions, promoting modularity, reusability, and scalability in code.
class is a keyword

'''
# class laptops:
#     def display(self): #    self inside the method refers to lap1 (the current object)
#         print("welcome")
# lap1=laptops()  # Create an object (instance) of class 'laptops'
# lap1.display() # Call the display() method


class laptop:
  owner="oneteam"    #class attribute ,common attribute 
  def specs(self,n,r):
        self.name=n #instance attribute
        self.RAM=r
lap1=laptop()
lap2=laptop()
lap1.specs("Dell","8GB")
lap2.specs("Hp","16GB")
laptop.owner="user"  # modify class variable
lap1.name="acer"
print(lap1.name,laptop.owner)
print(laptop.owner)


# class laptop:  
#     def __init__(self,n,r):   #constructor: it automatically call object.no need to call method.
#                               #A constructor is a special method used to initialize an object when it is created. automatically called when a new object is created. It initializes the attributes of the class.
#          self.name=n #attributes
#          self.RAM=r
# lap1=laptop("Dell","8GB")
# lap2=laptop("Hp","16GB")
# print(lap1.RAM,lap1.name)
# print(lap2.name,lap2.RAM)
