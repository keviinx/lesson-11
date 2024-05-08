# Polymorphism example without inheritance
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplance is flying")

def make_it_fly(flyable):
    flyable.fly()

bird1 = Bird()
airplane1 = Airplane()

make_it_fly(bird1)
make_it_fly(airplane1)