import random

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1
    def roll(self):
        self.value = random.randrange(1,self.sides+1)
        return self.value
    
class DiceBag:
    def __init__(self, dice):
        self.dice = dice
    def singleRoll(self, selectedDie):
        for die in self.dice:
            if die.sides == selectedDie:
                return die.roll()
        return -1
    def multiRoll(self, selectedDie, numberOfRolls):
        for die in self.dice:
            if die.sides == selectedDie:
                total = 0
                for i in range(0,numberOfRolls):
                    total += die.roll()
                return total
        return -1

fourSide = Die(4)
sixSide = Die(6)
tenSide = Die(10)
twentySide = Die(20)
fiftySide = Die(50)
hundredSide = Die(100)
diceBag = DiceBag([fourSide, sixSide, tenSide, twentySide, fiftySide, hundredSide])
print(diceBag.singleRoll(20))
print(diceBag.multiRoll(20, 16))