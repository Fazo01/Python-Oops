# 28. Create a class `Animal` inherited by `Bird` and `Fish`, both overriding a `move()` method.
class Animal:
  def __init__(self,name):
    self.name=name
  def move(self):
    print(f"{self.name} moves in some way.")
    
class Bird(Animal):
  def __init__(self, name):
    super().__init__(name)
  def move(self):
    print(f"{self.name} flies in the sky.")

class Fish(Animal):
  def __init__(self, name):
    super().__init__(name)
  def move(self):
    print(f"{self.name} swims in the sea.")

a=Animal("Lion")
a.move()
a1=Bird("Eagle")
a1.move()
a2=Fish("Shark")
a2.move()