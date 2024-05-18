#!/usr/bin/python3
"""making a python class for pokemon"""


class Pokemon:
    """class that defines a Pokemon"""

    pokecounter = 0
    validtypes = ("bug", "dark", "dragon", "electric", "fairy", "fighting",
                  "fire", "flying", "ghost", "grass", "ground", "ice",
                  "normal", "poison", "psychic", "rock", "steel", "water")

    def __init__(self, name, type, owner):

        # handle Pokemon name
        if not name or len(name.strip()) == 0:
            raise ValueError("The Pokemon needs a valid name")
        if not isinstance(name, str):
            raise TypeError("Pokemon name needs to be a string")
        self._name = name.strip()

        # handle Pokemon Type
        if type.lower() not in Pokemon.validtypes:
            raise ValueError(f"{type} is not a valid type")
        self._type = type.capitalize()

        # hanlde Pokemon owner
        if not owner or len(owner.strip()) == 0:
            raise ValueError("The Pokemon needs an owner")
        if not isinstance(owner, str):
            raise TypeError("Owner name needs to be a string")
        self._owner = owner.strip()

        # increase pokecounter
        Pokemon.pokecount()

    @property
    def name(self):
        """name getter"""
        return self._name

    @name.setter
    def name(self, value):
        """name setter"""
        if not value or len(value.strip()) == 0:
            raise ValueError("The Pokemon needs a name")
        if not isinstance(value, str):
            raise TypeError("Pokemon name needs to be a string")
        self._name = value

    @property
    def type(self):
        """type getter"""
        return self._type

    @type.setter
    def type(self, value):
        """type setter"""
        if value.lower() not in Pokemon.validtypes:
            raise ValueError(f"{value} is not a valid type")
        self._type = value.capitalize()

    @property
    def owner(self):
        """owner getter"""
        return self._owner

    @owner.setter
    def owner(self, value):
        """owner setter"""
        if not value or len(value.strip()) == 0:
            raise ValueError("The Pokemon needs an owner")
        if not isinstance(value, str):
            raise TypeError("Owner name needs to be a string")
        self._owner = value.strip()

    def __str__(self):
        """builds a readable string for the Pokemon"""
        string = "{} is a {} type Pokemon and belongs to {}".format(
            self.name, self.type, self.owner)
        return string

    @classmethod
    def pokecount(cls):
        """increment pokecounter"""
        cls.pokecounter += 1

    @classmethod
    def getpokecount(cls):
        """return pokecounter current count"""
        return "Total Pokemon: {}".format(cls.pokecounter)


# example usage
gengar = Pokemon("Gengar", "ghost", "Charlie")
pikachu = Pokemon("Pikachu", "electric", "Ash")
print(gengar)
print(pikachu)
print(Pokemon.getpokecount())
