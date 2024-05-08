# Inheritance:
# DONE create a parent class, e.g. Car
# DONE create a child class and define Attributes and Methods for the child class, e.g. ElectricCar

class Car():
    def __init__(self, brand, model, engine, year):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.year = year

    def drive(self):
        print("Car is driving forward")

class ElectricCar(Car):

    def __init__(self, brand, model, year):
        super().__init__(brand, model, "Electric", year)

    def drive(self):
        print("The electric car is driving forward")

tesla = ElectricCar("Tesla", "M3", "2020")
tesla.drive()