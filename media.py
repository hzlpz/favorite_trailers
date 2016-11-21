import webbrowser


class Video(): # Parent Class

    """ This is the main class for all media """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # This method grabs the information from entertainment_center.py
    def __init__(self, title, runtime, storyline,poster_image, trailer_youtube):
        self.title = title
        self.runtime = runtime
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self): # links to url to youtube to display trailer
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video): # Movie (Child) Class

    """ This class provides a way to store movie related information. """

    def __init__(self, title, runtime, storyline,poster_image, trailer_youtube):
        Video.__init__(self,title, runtime, storyline,
                       poster_image, trailer_youtube)


class Television(Video): # Television (Child) Class

    """ This class provides a way to store television related information. """

    def __init__(self, title, runtime, storyline, poster_image, trailer_youtube,
                 season, episode):
        Video.__init__(self, title, runtime, storyline, poster_image,
                       trailer_youtube)

        self.season = season
        self.episode = episode



