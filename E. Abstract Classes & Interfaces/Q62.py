# 62. Implement an abstract class `Payment` with subclasses `CreditCardPayment` and `PayPalPayment`.
from abc import ABC,abstractmethod
class Payment(ABC):
  @abstractmethod
  def pay(self,amount):
    pass

class CreditCardPayment(Payment):
  def __init__(self,card_number,holder_name):
    self.card_number=str(card_number)
    self.holder_name=holder_name
  def pay(self,amount):
    return f"Paid {amount} using credit card: {self.card_number[-4:]}, Holder Name: {self.holder_name}"

class PayPalPayment(Payment):
  def __init__(self,email):
    self.email=email
  def pay(self,amount):
    return f"Paid {amount} from credit card email {self.email}"
  
Payment=[CreditCardPayment(12323323,"Muhammad Faizan"),PayPalPayment("fg7829098@gmail.com")]
for p in Payment:
  print(p.pay(100))
