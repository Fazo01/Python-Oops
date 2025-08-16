# 14. Write a class `ShoppingCart` that allows adding and removing items, and calculating total price.
class ShoppingCart:
  def __init__(self):
    self.items={}

  def add(self,item,price):
    self.items[item]=price
    print(f"added {item} with the {price} ")
  def delete(self,item):
    if item in self.items:
      del self.items[item]
    else:
      print("No in cart")
  def CalculateTotalPrice(self):
    return sum(self.items.values())
  
  def show_cart(self):
    if not self.items:
      print("Cart is empty")
    else:
      print("Shopping Cart")
      for item,price in self.items.items():
        print(f"{item} : {price}")

S1=ShoppingCart()
S1.add("Chips",90)
S1.add("Chocolate",190)
S1.add("Orea",30)
S1.delete("Orea")
S1.show_cart()