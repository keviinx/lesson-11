# Polymorphism example
class Bird:

    def intro(self):
        print("There are many of birds.")

    def flights(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):

    def flights(self):
        print("Sparrows can fly.")

class Ostrich(Bird):

    def flights(self):
        print("Ostriches cannot fly.")

bird1 = Bird()
sparrow1 = Sparrow()
ostrich1 = Ostrich()

bird1.intro()
bird1.flights()

sparrow1.intro()
sparrow1.flights()

ostrich1.intro()
ostrich1.flights()