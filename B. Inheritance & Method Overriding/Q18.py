# 18. Write a program where a class `Animal` is inherited by `Dog` and `Cat`, both overriding a `speak()` method.
class Animal:
  def speak(self):
    print("Animal makes a sound")
class Dog(Animal):
  def speak(self):
    print("Woh woh")
class Cat(Animal):
  def speak(self):
    print("Meow Meow")

a=Animal()
a.speak()
b=Dog()
b.speak()
c=Cat()
c.speak()