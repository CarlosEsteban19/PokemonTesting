# Pokemon Class

A Python class for representing Pokémon entities.

## Overview

This Python class, `Pokemon`, provides a simple way to create and manage Pokémon objects. It allows you to define Pokémon with a name, type, and owner, while enforcing validation rules to ensure data integrity.

## Features

- Create Pokémon objects with a name, type, and owner.
- Enforce validation rules for each attribute to maintain data integrity.
- Keep track of the total number of Pokémon instances created.
- Get a string representation of Pokémon objects for easy display.

## Valid Types

The following Pokémon types are considered valid:

- Bug
- Dark
- Dragon
- Electric
- Fairy
- Fighting
- Fire
- Flying
- Ghost
- Grass
- Ground
- Ice
- Normal
- Poison
- Psychic
- Rock
- Steel
- Water

## Usage

### Installation

To use the `Pokemon` class in your project, you can simply copy the `pokemon.py` file into your project directory.

### Example

```python
from pokemon import Pokemon

# Create Pokémon instances
gengar = Pokemon("Gengar", "ghost", "Charlie")
pikachu = Pokemon("Pikachu", "electric", "Ash")

# Print Pokémon details
print(gengar)
print(pikachu)

# Get total number of Pokémon instances created
print(Pokemon.getpokecount())
