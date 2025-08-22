# 29. Write a class `Document` inherited by `WordDocument` and `PDFDocument` with different `save()` methods.
class Document:
  def __init__(self,title):
    self.title=title
  def save(self):
    print(f"Saving document {self.title}")
class WordDocument(Document):
  def __init__(self, title):
    super().__init__(title)
  def save(self):
    print(f"Saving Word Document {self.title} as .docx")
class PDFDocument(Document):
  def __init__(self, title):
    super().__init__(title)
  def save(self):
    print(f"Saving PDF Document {self.title} as .pdf")

d=Document("Generic")
d.save()
w=WordDocument("Myreport")
w.save()
p=PDFDocument("Invoice")
p.save()