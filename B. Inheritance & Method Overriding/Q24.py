# 24. Implement a class `Instrument` inherited by `Guitar` and `Piano`, each overriding `play()`.
class Instrument:
  def __init__(self,name):
    self.name=name
  def play(self):
    print(f"Instrument name is {self.name}")
class Guitar(Instrument):
  def __init__(self, name):
    super().__init__(name)
  def play(self):
    print(f"Strumming the {self.name}")
class Piano(Instrument):
  def __init__(self, name):
    super().__init__(name)
  def play(self):
    print(f"Playing the {self.name}")

a=Instrument("Piano")
a.play()
a1=Guitar("Guitar")
a1.play()
a2=Piano("Piano")
a2.play()