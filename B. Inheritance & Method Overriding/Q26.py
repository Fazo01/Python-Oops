# 26. Write a class `GameCharacter` inherited by `Warrior` and `Mage`, each with different attack methods.
class GameCharacter:
  def __init__(self,name,health):
    self.name=name
    self.health=health
  def show_status(self):
    print(f"Character name: {self.name}\nCharacter health: {self.health}")

class Warrior(GameCharacter):
  def __init__(self, name, health,strength):
    super().__init__(name, health)
    self.strength=strength
  def attack(self):
    print(f"{self.name} swing sword with strength {self.strength}")

class Mage(GameCharacter):
  def __init__(self, name, health,mana):
    super().__init__(name, health)
    self.mana=mana
  def attack(self):
    print(f"{self.name} cast a magic with mana {self.mana}")

p=GameCharacter("Muhammad Faizan",20)
p1=Warrior("Muhammad faizan",20,10)
p2=Mage("Muhammad Faizan",20,10)
p.show_status()
p1.attack()
p2.attack()