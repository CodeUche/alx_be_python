# Exercise 1

"""
Create a base class Shape with a method calculate_area().
Create a subclass Rectangle that inherits from Shape and overrides
calculate_area() to calculate the area of a rectangle.
"""

class Shape:

    def __init__(self, area):
        self.area = area

    def calculate_area(self):
        return f"Area us equal to {self.area}"


class Rectangle(Shape):
    
    def calculate_area(self):
        return f"Area us equal to {self.area}"
    

# Exercise 2: Multiple Inheritance Instruction:

"""
    Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
    Create a subclass Bat that inherits from both Bird and Mammal and implements 
    fly() and run() methods
"""

# Create first parent class Bird
class Bird:

    def __init__(self, bird):
        self.bird = bird

    def fly(self):
        return f"{self.bird} flies in the sky"

# Create second parent class Mammal  
class Mammal:
    def __init__(self, mammal):
        self.mammal = mammal

    def run(self):
        return f"{self.mammal} is a mammal and runs on land."
    
class Bat(Bird, Mammal):
    def __init__(self, bird, mammal):
        Bird.__init__(self, bird)
        Mammal.__init__(self, mammal)
    
    def bat_fr(self):
        return f"A {self.bird} is both a bird and mammal.\n{self.fly()}\n{self.run()}"
    
mammalia = Bat("bat", "fruit bat")

print(mammalia.bat_fr())


# Exercise 3:
"""
 Polymorphism with Duck Typing Instruction:
Create classes Dog, Cat, and Bird, each with a method make_sound().
Implement different behaviors for make_sound() in each class.
Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.
"""

class Dog:
    def make_sound():
        return "Dogs bark, Woof!"
class Cat:
    def make_sound():
        return "Cats unapologetically Meows!"
    
class Aves:
    def make_sound():
        return "Birds sing and Chirp!"

dog_obj = Dog()
cat_obj = Cat()
aves_obj = Aves()

print(f"{Dog.make_sound()}")
print(f"{Cat.make_sound()}")
print(f"{Aves.make_sound()}")
