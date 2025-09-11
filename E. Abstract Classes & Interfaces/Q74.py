# 74. Implement an abstract class `Logger` with subclasses `FileLogger` and `ConsoleLogger`.
from abc import ABC,abstractmethod
import datetime
class logger(ABC):
  @abstractmethod
  def log(self,message):
    pass
  def _timestamp(self):
    return datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
  
class ConsoleLogger(logger):
  def log(self, message):
    print(f"[console] {self._timestamp()} {message}")

class FileLogger(logger):
  def __init__(self,filename):
    self.filename=filename
  def log(self, message):
    log_message=f"[File:{self.filename}] {self._timestamp()}-{message}"
    with open(self.filename,"a") as f:
      f.write(log_message+"\n")
    print(log_message)

console_logger = ConsoleLogger()
file_logger = FileLogger("app.log")

console_logger.log("Application started")
file_logger.log("Error: Something went wrong")
