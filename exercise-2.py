# Inheritance and Polymorphism
# use the above parent and child class, 
# DONE create more child classes and define Methods for them

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

# more child class here
class SUV(Car):

    def __init__(self, brand, model, engine):
        super().__init__(brand, model, engine, "2024")

    def print_brand(self):
        print("The brand is "+ self.brand)

class Van(Car):
    def __init__(self, brand):
        self.brand = brand


tesla = ElectricCar("Tesla", "M3", "2020")
tesla.drive()
suv1 = SUV("BMW", "X5M", "Diesel")
suv1.print_brand()
van1 = Van("Mercedes")
van1.drive()