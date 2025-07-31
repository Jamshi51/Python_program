#  class method
#  Used when you need to access or modify class state, or to define factory methods.
#  Not use self ,only use cls.
#  It does not need object creation.we can call class name directly

#  class Person():
#         name='jamshi'
#         @classmethod
#         def show(cls):
#            print("name : ",cls.name)
# Person.show()


#2
class Employee():
      department="software engineer"
      def __init__(self,n):
            self.name=n
      @classmethod
      def change_dpt(cls,ch_n):
            cls.change_name=ch_n
Employee.change_dpt("data analyst")
print(Employee.department)
print(Employee.change_name)

#static method
# A method that does not depend on class or instance. 
# It's just namespaced inside the class.
#does not take self or cls.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

# Usage:
result = Math.add(5, 3)
print(result)
