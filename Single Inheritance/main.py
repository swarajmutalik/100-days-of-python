class Animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species 
    
    def make_sound(self):
        print("Sound made by the animal")

    
class Dog(Animal):
    def __init__(self,name,bread):
        Animal.__init__(self,name,species="Dog")
        self.bread = bread

    
    def make_sound(self):
        print("Bark!")

d = Dog('Dog','Doggerman')
d.make_sound()

a = Animal('Dog','Dog')
a.make_sound()
