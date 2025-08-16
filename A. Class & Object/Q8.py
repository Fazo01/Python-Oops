# 8. Write a class `Movie` that keeps track of the number of movies created using a class variable.
class Movie:

  Movie_Count=0

  def __init__(self,movie,gerne):
    self.movie=movie
    self.gerne=gerne
    Movie.Movie_Count+=1
  @classmethod
  def NumberOfMovie(cls):
    return cls.Movie_Count
  
M1=Movie("JJK","Anime")
M2=Movie("Oggy","Cartoon")

print(f"Number of movie: {Movie.NumberOfMovie()}")