class Car:
    def __init__(self, weight, color, brand_name):
        self.weight = weight
        self.color = color
        self.brand_name = brand_name

car1 = Car(1500, "Red", "Toyota")
car2 = Car(1800, "Blue", "Honda")

if car1.weight > car2.weight:
    print("Car 1 is heavier")
elif car2.weight > car1.weight:
    print("Car 2 is heavier")
else:
    print("Both cars have the same weight")