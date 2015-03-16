# media.py
# Full Stack Developer Nanodegree: P1
# Rhys Yorke
# 2015-03-14

import webbrowser

class Movie():
  # This class provides a way to store movie related information
  def __init__ (self, movie_title, movie_storyline, movie_poster, movie_trailer, release_date, movie_director):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = movie_poster
    self.trailer_youtube_url = movie_trailer
    self.release_date = release_date
    self.director = movie_director

  # Opens a Web Browser and shows the trailer
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)