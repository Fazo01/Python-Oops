# 13. Create a class `Car` with attributes make, model, and mileage. Add a method to update mileage.
class Car:
  
  def __init__(self,make,model,milage):
    self.make=make
    self.model=model
    self.milage=milage

  def UpdateMilage(self,newmilage):
    self.milage=newmilage

  def showdetails(self):
    print(f"Make: {self.make}, Model: {self.model}, Milage: {self.milage}")

c=Car("Toyota","Corola","99")
c.showdetails()
c.UpdateMilage(200)
c.showdetails()