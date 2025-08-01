# Cannot be accessed directly from outside the class.
# Can only be called from within the class itself.

class employee():
    def __init__(self,slry):
        self.__salary=slry
    def show(self):
        return self.__salary
s=employee("30000")
# print("salary : ",s.__salary)  # Not work,Raises AttributeError
print("salary : ",s.show())