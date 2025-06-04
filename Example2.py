class PetAnimal:
    def __init__(self, colour, year):
        self.colour = colour 
        self.year = year
    def name(self):
        print("Cat")

class WildAnimal:
    def __init__(self, colour , year):
        self.colour = colour 
        self.year = year
    def name(self):
        print("Tiger")

class AquaticAnimal:
    def __init__(self, colour, year ):
        self.colour = colour
        self.year = year   

    def name (self) :
        print("Fish")

Animal1 = PetAnimal ("white", "6") 
Animal2= WildAnimal ( "Yellow", "5")
Animal3 = AquaticAnimal ("Black", "1" )

for x in (Animal1, Animal2, Animal3):
    x.name()
