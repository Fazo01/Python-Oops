# 69. Write an abstract class `Report` with subclasses `PDFReport` and `ExcelReport`.
from abc import ABC,abstractmethod
class Report(ABC):
  def __init__(self,title,data):
    self.title=title
    self.data=data
  @abstractmethod
  def generate(self):
    pass
class PDFReport(Report):
  def generate(self):
    return f"Generating PDF Report: {self.title}\nData: {self.data}"
class ExcelReport(Report):
  def generate(self):
    return f"Generating Excel Report: {self.title}\nData: {self.data}"
  
Report=[PDFReport("Sales Report", {"Jan":1000,"Feb":1200,"Mar":1400}),ExcelReport("Inventory Report",["Item1","Item2","Item3"])]
for i in Report:
  print(i.generate())