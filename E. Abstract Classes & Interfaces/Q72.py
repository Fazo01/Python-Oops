# 72. Write an abstract class `Media` with subclasses `Audio` and `Video`.
from abc import ABC, abstractmethod

# Abstract Class
class Media(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration  # duration in minutes

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Subclass: Audio
class Audio(Media):
    def play(self):
        return f"Playing audio: {self.title} [{self.duration} min]"

    def stop(self):
        return f"Audio '{self.title}' stopped."


# Subclass: Video
class Video(Media):
    def play(self):
        return f"Playing video: {self.title} [{self.duration} min]"

    def stop(self):
        return f"Video '{self.title}' stopped."


# Example Usage
Media = [Audio("Shape of You", 4),Video("Inception", 148)]

for m in Media:
    print(m.play())
    print(m.stop())