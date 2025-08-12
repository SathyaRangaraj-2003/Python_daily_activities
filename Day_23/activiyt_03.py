#activity_03


# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def engine(self):
        return f"{self.brand} : Engine started"

# Subclass 1
class Car(Vehicle):
    def engine(self):
        return f"{self.brand} : Car engine started"

# Subclass 2
class Bike(Vehicle):
    def engine(self):
        return f"{self.brand} : Motorcycle engine started"


car = Car("Honda")
bike = Bike("Yamaha")

print(car.engine())       
print(bike.engine())      