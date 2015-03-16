# entertainment_center.py
# Full Stack Developer Nanodegree: P1
# Rhys Yorke
# 2015-03-14

import fresh_tomatoes
import media

# Favourite Movies
# Title, Storyline, Poster Image, Youtube Trailer url, Release Date, Director

princess_bride = media.Movie("The Princess Bride",
                        "While home sick in bed, a young boy's grandfather reads him a story called The Princess Bride.",
                        "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                        "https://youtu.be/VYgcrny2hRs",
                        "9 October 1987",
                        "Rob Reiner")

iron_man = media.Movie("Iron Man",
                        "After being held captive in an Afghan cave, an industrialist creates a unique weaponized suit of armor to fight against evil. This leads him to conflict within his own company.",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://youtu.be/8hYlB38asDY",
                        "2 May 2008",
                        "Jon Favreau")

star_wars_4 = media.Movie("Star Wars: A New Hope",
                        "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the universe from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://youtu.be/1g3_CFmnU7k",
                        "25 May 1977",
                        "George Lucas")

back_to_the_future = media.Movie("Back to the Future",
                        "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                        "https://youtu.be/qvsgGtivCgs",
                        "3 July 1995",
                        "Robert Zemeckis")

memento = media.Movie("Memento",
                        "A man creates a strange system to help him remember things; so he can hunt for the murderer of his wife without his short-term memory loss being an obstacle.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                        "https://youtu.be/nHozKtsvag0",
                        "25 May 2001",
                        "Christopher Nolan")

lilo_and_stitch = media.Movie("Lilo and Stitch",
                        "A Hawaiian girl adopts an unusual pet who is actually a notorious extra-terrestrial fugitive from the law.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c6/LiloandStitchmovieposter.jpg",
                        "https://youtu.be/wAtaSKQ4-T0",
                        "21 June 2002",
                        "Dean DeBlois, Chris Sanders")

# Create a movies array
movies = [princess_bride, iron_man, star_wars_4, back_to_the_future, memento, lilo_and_stitch]

#Open a web page
fresh_tomatoes.open_movies_page(movies)