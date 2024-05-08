# Inheritance
# Parent class Animal
class Animal():

    def __init__(self, name):
        self.name = name

    def type_of_animal(self):
        print("This is an animal.")

# child class of Dog
class Dog(Animal):

    def type_of_animal(self):
        print("This is an dog.")
    
# child class of Cat
class Cat(Animal):

    def type_of_animal(self):
        print("This is an cat.")


dog1 = Dog("Rocky")
dog1.type_of_animal()
cat1 = Cat("Mia")
cat1.type_of_animal()