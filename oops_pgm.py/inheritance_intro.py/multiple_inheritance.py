#multiple inheritance
#A class inherits from more than one parent class.


# class Father:
#     def skills(self):
#         print("Gardening")

# class Mother:
#     def skills(self):
#         print("Cooking")

# class Child(Father, Mother):
#     def show(self):
#         print("Child skills")

# c = Child()
# c.skills()  # Uses Father's method by default (method resolution order)


#2

# class father:
#     def skill1(self):
#         print("painter")
# class mother:
#     def skill2(self):
#         print("sawing")
# class son(father,mother):
#     def son_skills(self):
#         print("engineer")
# c=son()
# c.son_skills()
# c.skill2()
# c.skill1()


#3
# class Father:
#     def speak(self):
#         print("Speaks Hindi")

# class Mother:
#     def speak(self):
#         print("Speaks English")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.speak()  # MRO will call Father's speak() because Father is listed first

#4

class father:
    def __init__(self,n,a,mother_name,mother_age):
        self.father_name=n
        self.father_age=a
        super().__init__(mother_name,mother_age)
class mother:
    def __init__(self,n,a):
        self.mother_name=n
        self.mother_age=a
class son(father,mother):
    def __init__(self,school,father_name,father_age,mother_name,mother_age):
        self.son_school=school
        # father.__init__(self,father_name,father_age) # not need  parent class variable name in son method
        # mother.__init__(self,mother_name,mother_age)
        super().__init__(father_name,father_age,mother_name,mother_age)
c=son("GMLPS","Ram","60","Sita","45")
print("school :",c.son_school)
print("father :",c.father_name)
print("mother : ",c.mother_name)




