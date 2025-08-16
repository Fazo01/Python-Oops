# 12. Implement a class `ComplexNumber` to add and subtract two complex numbers.
class ComplexNumber:
  def __init__(self,real,imag):
    self.real=real
    self.imag=imag
  def add(self,other):
    print(f"new number added in real: {self.real+other.real}")
    print(f"new number added in imag: {self.imag+other.imag}")
  def subtract(self,other):
    print(f"new number subtract in real: {self.real-other.real}")
    print(f"new number subtract in imag: {self.imag-other.imag}")
  def showNumbers(self):
    print(f"Real number {self.real}")
    print(f"Imag number {self.imag}")
c1=ComplexNumber(9,9)
c2=ComplexNumber(2,2)
c1.showNumbers()
c1.subtract(c2)
c1.add(c2)