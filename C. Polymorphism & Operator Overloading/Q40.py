# 40. Write a `Fraction` class to support addition and multiplication.
import math
class Fraction:
  def __init__(self,numinator,denominator):
    self.numinator=numinator
    self.denominator=denominator
    self.simplify()
  def simplify(self):
    gcd=math.gcd(self.numinator,self.denominator)
    self.numinator//=gcd
    self.denominator//=gcd
  def __add__(self,other):
    new_num=self.numinator*other.denominator+other.numinator*self.denominator
    new_den=self.denominator*other.numinator
    return Fraction(new_num,new_den)
  def __mul__(self,other):
    new_num=self.numinator*other.numinator
    new_den=self.denominator*other.denominator
    return Fraction(new_num,new_den)
  def __str__(self):
    return f"{self.numinator}/{self.denominator}"

f1=Fraction(9,9)
f2=Fraction(9,9)
print(f1+f2)
print(f1*f2)