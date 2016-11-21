import fresh_tomatoes
import media


# 1. Grey Gardens
grey_gardens = media.Movie("Grey Gardens",
                           "100 minutes",
                           "This film explores the daily lives of two eccentric relatives.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/0/08/Grey_Gardens_%281975_film%29_poster.jpg/220px-Grey_Gardens_%281975_film%29_poster.jpg", #NOQA
                           "https://youtu.be/xG5baCxTtgw")


# 2. Style Wars
style_wars = media.Movie("Style Wars",
                         "111 minutes",
                        "New Yorkers who practice break dancing and graffiti.",
                        "http://media.gettyimages.com/photos/movie-poster-advertises-style-wars-tony-silvers-hip-hop-and-graffiti-picture-id596445467", #NOQA
                        "https://youtu.be/L6GbbFXxNpw")

# 3. The Thin Blue Line
thin_blue = media.Movie("The Thin Blue Line",
                        "106 minutes",
                        "True story of the arrest and conviction of Randall Adams.",
                        "http://moviescounter.com/wp-content/uploads/2016/06/The-Thin-Blue-Line-1988.jpg", #NOQA
                        "https://youtu.be/dNL5A4D0G4g")


# 4. Man on Wire
man_on_wire = media.Movie("Man on Wire",
                          "94 minutes",
                          "A French tightrope-walker named Philippe Petit.",
                          "http://www.impawards.com/2008/posters/man_on_wire_ver2_xlg.jpg", #NOQA
                          "https://youtu.be/EIawNRm9NWM")


# 5. Jiro Dreams of Sushi
jiro = media.Movie("Jiro Dreams of Sushi",
                   "83 minutes",
                   "Jiro Dreams of Sushi is the story of 85 year-old Jiro Ono.",
                   "https://ctcmr.files.wordpress.com/2012/04/jiro_dreams_of_sushi_poster.jpg", #NOQA
                   "https://youtu.be/M-aGPniFvS0")


# Freaks and Geeks
freaks_geeks = media.Television("Freaks and Geeks",
                                "44 minutes",
                                "Daniel escapes his problems through punk rock.",
                                "https://fanart.tv/fanart/tv/76321/tvposter/freaks-and-geeks-52c6ba777cfda.jpg", #NOQA
                                "https://youtu.be/vH5bHHUmXqc",
                                "1",
                                "15")


movies = [grey_gardens, style_wars, thin_blue, man_on_wire, jiro, freaks_geeks]
fresh_tomatoes.open_movies_page(movies)





