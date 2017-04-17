"""Defines the Movie class that contains the details of a movie."""
import webbrowser


class Movie():
    """This class provides a way to store movie related information.
        Attributes:
            title: A string to store the title of the movie.
            storyline: A string to store the basic plot of the movie.
            genre: A string to store genre of movie.
            rating: A string to store rating of movie.
            poster_image_url: A string to store the URL of the movie poster.
            trailer_youtube_url: A string to store the URL of movie trailer.
    """
    def __init__(self, movie_title, movie_storyline, movie_genre,
                 movie_rating, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
