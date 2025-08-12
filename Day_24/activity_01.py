#activity_04:

from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

# Subclass1
class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Subclass2
class Cat(Animal):
    def speak(self):
        return "Cat Meow"

animals = [Dog(),Cat()]

for animal in animals:
	print(animal.speak())
