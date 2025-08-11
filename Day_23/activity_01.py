#activity_01


class Car:
    brand = "Honda"
    def num_plate(self, number_plate):
        self.number_plate = number_plate  
        return number_plate

car_1 = Car()
print(car_1.brand)
print(car_1.num_plate("AD1239"))


