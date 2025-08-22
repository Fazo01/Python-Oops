# 22. Create a base class `Appliance` inherited by `WashingMachine` and `Refrigerator`.
class Appliance:
  def __init__(self,name):
    self.name=name

  def show_info(self):
    return f"Name of the appliance {self.name}"
class WashingMachine(Appliance):
  def __init__(self, name,brand):
    super().__init__(name)
    self.brand=brand
  def show_info(self):
    return f"Name of the Washing Machine {self.name}. Brand name {self.brand}"

class Refrigerator(Appliance):
  def __init__(self, name,brand):
    super().__init__(name)
    self.brand=brand
  def show_info(self):
    return f"Name of the Refrigerator {self.name}. Brand name {self.brand}"
  
a=Appliance("Washing")
print(a.show_info())
w=WashingMachine("Washing Machine","Dawlance")
print(w.show_info())
r=Refrigerator("Refrigerator","Dawlance")
print(r.show_info())