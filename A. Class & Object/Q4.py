# 4. Create a class `Laptop` that stores brand, model, and price. Add a method to apply a discount percentage.
class Laptop:
  def __init__(self,brand,model,price):
    self.brand=brand
    self.model=model
    self.price=price
  def discount(self,discount):
    print(f"Brand Name : {self.brand}")
    print(f"Model Name : {self.model}")
    print(f"Discount : {discount}")
    print(f"Price : {(discount/self.price)*100}")
  def ShowDetails(self):
    print(f"Brand Name : {self.brand}")
    print(f"Model Name : {self.model}")
    print(f"Price : {self.price}")
m1=Laptop("Lenovo","M-1001",90)
m1.ShowDetails()
m1.discount(50)