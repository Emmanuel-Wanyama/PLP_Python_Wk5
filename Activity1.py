class Superhero:
    # A class representing a generic superhero.
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
        print(f"{self.name} has arrived!")

    def introduce(self):
        # A method to introduce the superhero.
        return f"My name is {self.name} and my power is {self.power}!"

    def fight(self, villain):
        # A method for the superhero to fight a villain.
        self.health -= 10
        return f"{self.name} uses their {self.power} to fight {villain}. Health is now {self.health}."

class FlyingSuperhero(Superhero):
    # This class inherits from Superhero and adds a unique method.
    def __init__(self, name, power, health, speed):
        super().__init__(name, power, health)
        self.speed = speed

    def fly(self):
        # A specific method for a flying superhero.
        return f"{self.name} is flying at {self.speed} mph!"

    def fight(self, villain):
        # This method overrides the parent's fight method. This demonstrates polymorphism.
        super().fight(villain)
        return f"{self.name} quickly dodges a hit from {villain} and counters with a flying attack!"

# Create an instance of the parent class
hero = Superhero("Captain Cool", "ice breath", 100)
print(hero.introduce())
print(hero.fight("Dr. Evil"))
print("-" * 20)

# Create an instance of the inherited class
flying_hero = FlyingSuperhero("The Flash", "super speed", 100, 767)
print(flying_hero.introduce())
print(flying_hero.fly())
print(flying_hero.fight("The Joker"))
