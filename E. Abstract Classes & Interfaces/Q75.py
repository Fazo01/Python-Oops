# 75. Write an abstract class `UserAuthentication` with subclasses `PasswordAuth` and `OTPAuth`.
from abc import ABC,abstractmethod
import random
class UserAuthentication(ABC):
  @abstractmethod
  def authentication(self):
    pass

class PasswordAuth(UserAuthentication):
  def __init__(self,correct_password):
    self.correct_password=correct_password
  def authentication(self,user_input):
    if user_input==self.correct_password:
      return "Password Authentication Successful"
    else:
      return "Password incorrect"
    
class OTPAuth(UserAuthentication):
  def __init__(self):
    self.otp=str(random.randint(1000,9999))
  def get_otp(self):
    return self.otp
  def authentication(self,user_input):
    if user_input==self.otp:
      return "Otp Authentication Successful"
    else:
      return "Otp incorrect"
    
p1=PasswordAuth("faizan")
print(p1.authentication("faizan"))
p2=OTPAuth()
print(p2.get_otp())
print(p2.authentication(4574))
