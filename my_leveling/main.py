import random
from PIL import Image

class UpEnergy:
    def __init__ (self, energy = 0, power = 0):
        self.energy = energy
        self.power = power
    
    def push_up(self):
        self.energy += 5
        print(f"Your Energy Increase 5, Your Energy Now is {self.energy}\n")

    def sit_up(self):
        self.energy += 3
        print(f"Your Energy Increase 3, Your Energy Now is {self.energy}\n")

    def plank(self):
        self.energy += 7
        print(f"Your Energy Increase 7, Your Energy Now is {self.energy}\n")

class UpPower(UpEnergy):
    def __init__ (self, instance):
        super().__init__(instance.energy, instance.power)

        if self.energy < 50:
            print("Cannot Take Any Raid, Because Your Energy under 50\nGo Train First!\n")

    def raid_dungeon(self):
        enemies = random.randint(1, 50)
        if self.power < enemies:
            self.power = 0
            print(f"You Died!\n")
        else:
            self.power += 20
            print(f"You Win Raid! Your Power +20\n")
        
    def mini_dungeon(self):
        self.power += 5
        self.power -= 1
        print(f"You Take Mini Dungeon, Because This Your Power +5, but You Have Tired so -1 Power\n")
    
    def check_power(self):
        if self.power > 200:
            print(f"Your Current Power: {self.power}\nCongrats! you reach 200 power, this is for you <3\n")
            image = Image.open('./Cha Hae-In.jpg')
            image.show()
        else:
            print(f"Your Current Power: {self.power}\n")
    
energy = UpEnergy()
for _ in range(10):
    energy.push_up()

power = UpPower(energy)
for _ in range(51):
    power.mini_dungeon()

power.check_power()
# letakkan code disini