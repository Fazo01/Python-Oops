# 35. Create a `Currency` class that supports conversion between USD and EUR using `*` operator.
class Curreny:
  USD_TO_EUR=0.85
  EUR_TO_USD=1.17
  def __init__(self,amount,currency):
    self.amount=amount
    self.currency=currency
  def __mul__(self,other):
    if self.currency=="USD":
      return Curreny(self.amount*self.USD_TO_EUR,"EUR")
    elif self.currency=="EUR":
      return Curreny(self.amount*self.EUR_TO_USD,"USD")
  def __str__(self):
    return f"{self.amount:2f} {self.currency}"
c1=Curreny(2,"USD")

c2=Curreny(2,"EUR")
print(c1*1)
print(c2*1)