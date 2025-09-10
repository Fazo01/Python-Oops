# 59. Create a `Book` class where price can only be updated if discount is applied.
class Book:
  def __init__(self,title,price):
    self.title=title
    self.__price=price
  @property
  def price(self):
    return self.__price
  def apply_discount(self,discount_precent):
    if 0<discount_precent<100:
      discount_precent=self.__price*(discount_precent/100)
      self.__price-=discount_precent
    else:
      print("Invalid discount! Must be between 1 to 100")
b1=Book("48 law of power",900)
b1.apply_discount(50)
print(b1.price)