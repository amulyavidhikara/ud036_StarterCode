""" This file creates a class called "Movie" to store information related to the movie for which information should be displayed in the movie trailer website"""

import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_summary, poster_image, trailer_youtube):
        self.title = movie_title
        self.summary = movie_summary
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
