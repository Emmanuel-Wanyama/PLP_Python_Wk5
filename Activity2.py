class Animal:
    # The base class for all animals.
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        # This is a generic method that will be overridden.
        pass

class Cat(Animal):
    # This class inherits from Animal.
    def make_sound(self):
        # It provides its own implementation of make_sound.
        return f"{self.name} says meow!"

class Dog(Animal):
    # This class also inherits from Animal.
    def make_sound(self, intensity="woof"):
        # It has its own unique implementation.
        if intensity == "bark":
            return f"{self.name} says BARK BARK!"
        return f"{self.name} says woof!"

# Create instances of each class.
my_cat = Cat("Whiskers")
my_dog = Dog("Buddy")

# A list of animal objects.
animals = [my_cat, my_dog]

# Loop through the list and call the same method,
# but get different behaviors. This is polymorphism.
for animal in animals:
    print(animal.make_sound())

# You can also call the method with specific arguments.
print(my_dog.make_sound("bark"))
