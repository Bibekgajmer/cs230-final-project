from BagOfDice import Die, DiceBag
from RPGCharacterCreator import CharacterGenerator  
# Create a list of Die objects with different sides
# Create a list of Die objects with different sides
dice_list = [Die(2), Die(4), Die(6), Die(10), Die(20), Die(50), Die(100)]

# Pass the list of dice into a DiceBag object
dice_bag = DiceBag(dice_list)

# Create a CharacterGenerator object and pass the DiceBag object to it
character_generator = CharacterGenerator(dice_bag)

# Call the buildCharacter method
character_generator.buildCharacter()

# Print the object using the __str__ method
print(character_generator)