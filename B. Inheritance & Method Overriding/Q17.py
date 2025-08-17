# 17. Implement a class hierarchy for vehicles: `Vehicle` → `Car` → `ElectricCar`.
class Vehicles():
  def __init__(self,brand):
    self.brand=brand
  def drive(self):
    print(f"Car brand: {self.brand}")

class Car(Vehicles):
  def __init__(self, brand,model):
    super().__init__(brand)
    self.model=model
  def drive(self):
    print(f"Car brand: {self.brand}. \nCar model: {self.model}")

class ElectricCar(Car):
  def __init__(self, brand, model,battery):
    super().__init__(brand,model)
    self.battery=battery
  def drive(self):
    print(f"Car brand: {self.brand}. \nCar model: {self.model}. \nCar battery: {self.battery}.")
c1=Vehicles("Toyota")
c2=Car("Toyota","Grande")
c3=ElectricCar("Toyota","Grande","M820")
c1.drive()
c2.drive()
c3.drive()