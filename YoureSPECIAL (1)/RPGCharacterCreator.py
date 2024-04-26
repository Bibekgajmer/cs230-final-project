import random
class CharacterGenerator:
    def __init__(self, dice):
        # governingSpecial maps each skill to a SPECIAL attribute.
        # For each point of its associated SPECIAL, skills will be increased by 2.
        self.governingSpecial = {
            "barter": "charisma",
            "energyweapons": "intelligence",
            "explosives": "perception",
            "guns": "agility",
            "lockpick": "perception",
            "medicine": "intelligence",
            "meleeweapons": "strength",
            "repair": "endurance",
            "science": "intelligence",
            "sneak": "agility",
            "speech": "charisma",
            "survival": "endurance",
            "unarmed": "strength",
        }
        # Create instance member variables
        self.dice = dice
        self.name = "Courier"
        self.age = 18
        self.gender = ""
        self.special = {
            "strength": 1,
            "perception": 1,
            "endurance": 1,
            "charisma": 1,
            "intelligence": 1,
            "agility": 1,
            "luck": 1
        }
        self.skills = {skill: 5 for skill in self.governingSpecial}
        self.attributes = {
            "hitpoints": 1,
            "actionpoints": 1,
            "carryweight": 1,
            "radiationresist": 1,
            "compassrange": 1,
            "movespeed": 1
        }

    def buildCharacter(self):
        # Prompt user for name
        self.name = input("Enter your character's name: ")

        # Check if name triggers special conditions
        if self.name == "Arnold":
            self.special["strength"] = 10
        elif self.name == "Lucky":
            self.special["luck"] = 10

        # Assign 33 points randomly to SPECIALs
        available_points = 33
        while available_points > 0:
            selected_special = random.choice(list(self.special.keys()))
            if self.special[selected_special] < 10:
                self.special[selected_special] += 1
                available_points -= 1

        # Set age
        self.age = random.randint(18, 65)
        if self.age < 25:
            self.special["agility"] += 2
        elif 25 <= self.age < 40:
            self.special["perception"] += 1
            self.special["endurance"] += 1
        else:
            self.special["intelligence"] += 1
            self.special["charisma"] += 1

        # Prompt user for gender
        valid_genders = ["M", "F", "O"]
        while self.gender not in valid_genders:
            self.gender = input("Enter your character's gender (M/F/O): ").upper()
            if self.gender == "M":
                self.special["strength"] += 1
                self.special["agility"] -= 1
            elif self.gender == "F":
                self.special["agility"] += 1
                self.special["strength"] -= 1

        # Increase skills based on SPECIAL and luck
        for skill, special_attribute in self.governingSpecial.items():
            self.skills[skill] += 2 * self.special[special_attribute] + self.special["luck"] // 2

        # Set attributes
        self.attributes["hitpoints"] = self.dice.multiRoll(100, self.special["endurance"]) + self.dice.singleRoll(20) * self.special["luck"] // 2
        self.attributes["actionpoints"] = self.dice.multiRoll(10, self.special["agility"])
        self.attributes["carryweight"] = 100 + self.dice.singleRoll(20) * self.special["strength"]
        self.attributes["radiationresist"] = self.dice.multiRoll(2, self.special["endurance"])
        self.attributes["compassrange"] = 100 + self.dice.multiRoll(6, self.special["perception"]) + self.dice.multiRoll(4, self.special["intelligence"])
        self.attributes["movespeed"] = self.dice.multiRoll(50, self.special["agility"]) // 2

    def __str__(self):
        character_info = f"Name: {self.name}\n"
        character_info += f"Age: {self.age}\n"
        character_info += f"Gender: {self.gender}\n"
        character_info += "\nSPECIAL\n"
        for special, value in self.special.items():
          character_info += f"{special.capitalize()}: {value}\n"
        character_info += "\nSkills\n" 
        for skill, value in self.skills.items():
          character_info += f"{skill.capitalize()}: {value}\n"
        character_info += "\nDerived Attributes\n" 
        for attribute, value in self.attributes.items():
          character_info += f"{attribute.capitalize()}: {value}\n"
        return character_info
