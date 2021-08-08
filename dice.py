import random


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        roll_nums=(x,y)
        return roll_nums


dice = Dice()
print(dice.roll())