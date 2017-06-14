import webbrowser

""" This file creates a class called "Movie" """
""" to store information related to the movie for which information"""
"""should be displayed in the movie trailer website"""


class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_desc, poster_image, trailer_link):
        self.title = movie_title
        self.summary = movie_desc
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link
