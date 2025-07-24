'''
class is a keyword

'''
# class laptops:
#     def display(self): #    self inside the method refers to lap1 (the current object)
#         print("welcome")
# lap1=laptops()  # Create an object (instance) of class 'laptops'
# lap1.display() # Call the display() method


# class laptop:
#     def specs(self,n,r):
#         self.name=n
#         self.RAM=r
# lap1=laptop()
# lap2=laptop()
# lap1.specs("Dell","8GB")
# lap2.specs("Hp","16GB")

# print(lap1.name)


class laptop:  
    def __init__(self,n,r):   #constructor: it runs when a new object is created.
         self.name=n
         self.RAM=r
lap1=laptop("Dell","8GB")
lap2=laptop("Hp","16GB")
print(lap2.RAM)
