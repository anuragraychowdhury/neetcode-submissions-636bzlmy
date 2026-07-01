class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
Batman = SuperHero("Batman", "Intelligence", 100)
Superman = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(Batman.name)
print(Batman.power)
print(Batman.health)
print(Superman.name)
print(Superman.power)
print(Superman.health)