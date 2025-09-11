# 68. Implement an abstract class `Animal` with `eat()` and `sleep()` methods.
from abc import ABC,abstractmethod
class Animal(ABC):
  @abstractmethod
  def eat(self):
    pass
  @abstractmethod
  def sleep(self):
    pass
class Dog(Animal):
  def eat(self):
    return f"Dog is eating bones"
  def sleep(self):
    return f"Dog is sleeping"
class Cat(Animal):
  def eat(self):
    return f"Cat is eating meat"
  def sleep(self):
    return f"Cat is sleeping"
Animal=[Dog(),Cat()]
for a in Animal:
  print(a.eat(),"\n",a.sleep())