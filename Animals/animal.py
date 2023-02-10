class Animal:
    def __init__(self, name):
        self.name = name
        
    def reply(self):
        return self.speak()

class Mammal(Animal):
    def speak(self):
        return f"{self.name} makes a sound."

class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"

class Primate(Mammal):
    def speak(self):
        return f"{self.name} makes a grunting noise."

class ComputerScientist(Primate):
    def speak(self):
        Primate.speak(self)
