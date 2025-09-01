'''
Inheritance allows a class (child class) to acquire properties and methods of another
 class (parent class). It supports hierarchical classification and promotes code reuse.

 '''
#single inheritance
#A child class inherits from only one parent class.


# class Vehicles: #parent class
#     def details(self,make,model): #it is not use init 
#         self.make=make
#         self.model=model
# class car(Vehicles): #child class,it inherit parent class
#     def __init__(self, color,power):
#         self.color=color
#         self.power=power

# c1=car("red","151 Bhp")
# c1.details("2003","Benz") 
# print(c1.color,c1.power)
# #You can use __init__() in both classes, but in your current code, the parent class Vehicles does not need automatic initialization, so:

    # You use a regular method details() in Vehicles to assign values manually

    # You use __init__() in the child car class to initialize color and power automatically

#use __init__ in both

# class Vehicles: #parent class
#     def __init__(self,make,model): #it is not use init 
#         self.make=make
#         self.model=model
# class car(Vehicles): #child class,it inherit parent class
#     def __init__(self, color,power,make,model):
#         self.color=color
#         self.power=power
#         super().__init__(make,model)

# c1=car("red","151 Bhp","2003","Benz")
# print(c1.color,c1.power)


class parent:
   def __init__(self,n,a):
    self.name=n
    self.age=a
class child(parent):
  def __init__(self,place,add,n,a):
    self.place=place
    self.address=add
    super().__init__(n,a)
c=child("th","anj","jam","21")
print(c.name)