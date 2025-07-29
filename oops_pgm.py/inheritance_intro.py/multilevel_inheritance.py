#multilevel inheritance
#A class inherits from a child class which in turn inherits from another class (like a chain).


# class Grandfather:
#     def land(self):
#         print("Grandfather's land")

# class Father(Grandfather):
#     def house(self):
#         print("Father's house")

# class Son(Father):
#     def car(self):
#         print("Son's car")

# s = Son()
# s.land()
# s.house()
# s.car()

#2
class Person:
    def __init__(self,pn):
        self.pname=pn
        # super().__init__(pn,id,dpt)
    def show_name(self):
        print("name : ",self.pname)
class Employee(Person):
    def __init__(self,pn,id):
        self.emp_id=id
        super().__init__(pn)
    def show_id(self):
        print("emp_id : ",self.emp_id)
class Manager(Employee):
    def __init__(self,pn,id,dpt):
        super().__init__(pn,id)
        self.dpt_name=dpt
    def show_dpt(self):
        print("department : ",self.dpt_name)
m=Manager("jamshi","10123","IT")
m.show_name()
m.show_id()
m.show_dpt()




