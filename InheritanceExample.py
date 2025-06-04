class Animal :
    def __init__(self, colour, age ):
        self.colour = colour
        self.age = age

    def name (self):
        print("Pet Animals")

class Dog(Animal):
    def name (self):
        print("Oggy")        

class Cat(Animal):
    def name(self):
        print("Kitty")

Animal1= Dog("Black", "5")
Animal2= Cat("white", "6")

for x in (Animal1, Animal2):
    print(x.colour)
    print(x.age) 
    x.name()           
