class Player:
    def __init__ (self, name, health = 100, energy=100): #constructor
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 1):
        target.health -= damage
        if self.energy > 0:
            self.energy -= damage
        else:
            print(f"{self.name} has no energy, cannot attack.")
        print(f"{self.name} attacking {damage} damage to {dragon.name} .. ")
        if target.is_attacked(player_name=self.name):
            self.health -= target.damage

    def show_info(self):
        if self.energy > 0:
            print(f"\n{self.name} health: {self.health}\n{self.name} energy: {self.energy}")
        else:
            print(f"{self.name} has no energy.")

class Monster:
    def __init__ (self, name, health = 100):
        self.name = name
        self.health = health #dinamic
        self.health_init = self.health #500
        self.damage = 10

    def is_attacked (self, player_name):
        print(f"{self.name} attack {self.damage} damage to {player_name}\n")
        return self.health < self.health_init

    def show_info(self):
        if self.health > 0:
            print(f"\n{self.name} health: {self.health}")
        else:
            print(f"{self.name} is defeated")

player1 = Player(name="Sung Jin Woo")
player2 = Player(name="Igris")

dragon = Monster(name="Kamish", health=500)
monarch = Monster(name="Antares", health=1000)

player1.attack(target=monarch, damage=780)
player2.attack(target=dragon, damage=500)

player1.show_info()
player2.show_info()
dragon.show_info()
monarch.show_info()