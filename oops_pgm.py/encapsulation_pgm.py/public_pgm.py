class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    # public method
    def show_brand(self):
        print("Car brand is:", self.brand)

# Create object
c = Car("Toyota")

# Access public method from outside the class (✅ allowed)
c.show_brand()