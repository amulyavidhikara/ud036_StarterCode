import media
import fresh_tomatoes

""" This file stores all the data related to the movies that
should be displayed in the Movies trailer website

Format to add new movie entries :

attribute_name = media.Movie(
    movie title,
    short description of the movie plot,
    url of poster image,
    url of trailer)

Once you have added a new entry please add the new attribute entry to
the 'movies' list at the bottom of the script
"""

# Instance for the movie casualties of war
casualties_of_war = media.Movie(
    "Casualties of War (1989)",
    "During the Vietnam War, a soldier finds himself the outsider of \
    his own squad when they unnecessarily kidnap a female villager.",
    "https://goo.gl/KFpvUo", "https://youtu.be/5YaLbyXh59A")

# Instance for the movie kiss kiss bang bang
kiss_kiss_bang_bang = media.Movie(
    "Kiss Kiss Bang Bang (2005)",
    "A murder mystery brings together a private eye, a struggling actress\
    , and a thief masquerading as an actor.",
    "https://goo.gl/jy732j", "https://youtu.be/__PnD1HWXSo")

# Instance for the movie Godfather
godfather = media.Movie(
    "The Godfather (1972)",
    "The aging patriarch of an organized crime dynasty transfers control\
    of his clandestine empire to his reluctant son.",
    "https://goo.gl/GW5OeF", "https://youtu.be/sY1S34973zA")

# Instance for the movie Ice Age
ice_age = media.Movie(
    "Ice Age (2002)", "Set during the Ice Age, a \
    sabertooth tiger, a sloth, and a wooly mammoth find a lost human\
    infant, and they try to return him to his tribe.",
    "https://goo.gl/xfAHyk", "https://youtu.be/cMfeWyVBidk")

# Instance for the hindi movie Chak De India!
chak_de_india = media.Movie(
    "Chak De India! (2007)",
    "The story of a hockey player who returns to the game as a coach of\
    a women's hockey team.",
    "https://goo.gl/AjZwW2", "https://youtu.be/6a0-dSMWm5g")

# Instance for the movie The Shawshank Redemption
the_shawshank_redemption = media.Movie(
    "The Shawshank Redemption (1994)",
    "Two imprisoned men bond over a number of years, finding solace\
    and eventual redemption through acts of common decency.",
    "http://bit.ly/2soSl4i", "https://youtu.be/K_tLp7T6U1c")

# Instance for the movie Crounching Tiger, Hidden Dragon
crouching_tiger_hidden_dragon = media.Movie(
    "Crouching Tiger, Hidden Dragon (2000)",
    "Two warriors in pursuit of a stolen sword and a notorious\
    fugitive are led to an impetuous, physically-skilled, \
    teenage nobleman's daughter, who is at a crossroads in her life.",
    "http://bit.ly/2soRhxe", "https://youtu.be/gLpZ_5bHmo8")

# Instance for the movie Enemy at the gates
enemy_at_the_gates = media.Movie(
    "Enemy at the Gates (2001)",
    "Two Russian and German snipers play a game of cat-and-mouse\
    during the Battle of Stalingrad.",
    "http://bit.ly/2sp5avw", "https://youtu.be/4O-sMh_DO6I")

# Instance for the documentary March of the penguins
march_of_the_penguins = media.Movie(
    "March of the Penguins (2005)",
    "In the Antarctic, every March since the beginning of time,\
    the quest begins to find the perfect mate and start a family.",
    "http://bit.ly/2sp2E8b", "https://youtu.be/L7tWNwhSocE")

# Instance for the movie Pink
pink = media.Movie(
    "Pink (2016)",
    "When three young women are implicated in a crime, \
    a retired lawyer steps forward to help them clear their names.",
    "http://bit.ly/2soQnAO", "https://youtu.be/AL2TShb6fFs")

# List of movies to be displayed in the movies trailers websites
movies = [casualties_of_war, kiss_kiss_bang_bang,
          godfather, ice_age, chak_de_india,
          the_shawshank_redemption, crouching_tiger_hidden_dragon,
          enemy_at_the_gates, march_of_the_penguins, pink]

# Call to the fresh tomatoes script to generate the output html
fresh_tomatoes.open_movies_page(movies)
