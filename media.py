import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_summary, poster_image):
        self.title = movie_title
        self.summary = movie_summary
        self.poster_image_url = poster_image
