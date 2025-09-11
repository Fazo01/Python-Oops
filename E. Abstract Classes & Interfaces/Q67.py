# 67. Create an abstract class `Notification` with subclasses `EmailNotification` and `SMSNotification`.
from abc import ABC,abstractmethod
class Notification(ABC):
  def __init__(self,recipient,massage):
    self.recipient=recipient
    self.massage=massage
  def send(self):
    pass
class EmailNotification(Notification):
  def send(self):
    return f"Sending email to {self.recipient}:{self.massage}"
class SMSNotification(Notification):
  def send(self):
    return f"Sending email to {self.recipient}:{self.massage}"
Notification=[EmailNotification("fg@gmail.com","Your order has been shipped!"),SMSNotification("Mm@gmail.com","Your OTP is 456789.")]
for n in Notification:
  print(n.send())