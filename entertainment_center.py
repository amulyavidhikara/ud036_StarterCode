import media
import fresh_tomatoes


casualties_of_war = media.Movie("Casualties of War (1989)", "During the Vietnam War, a soldier finds himself the outsider of his own squad when they unnecessarily kidnap a female villager.",
                                "http://www.suggestmemovie.com/fotolar2/14126885131152669056.jpg", "https://youtu.be/5YaLbyXh59A")


kiss_kiss_bang_bang = media.Movie("Kiss Kiss Bang Bang (2005)", "A murder mystery brings together a private eye, a struggling actress, and a thief masquerading as an actor.",
                                  "http://www.suggestmemovie.com/fotolar/1296323193171865407.jpg", "https://youtu.be/__PnD1HWXSo")


godfather = media.Movie("The Godfather (1972)", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,704,1000_AL_.jpg", "https://youtu.be/sY1S34973zA")

ice_age = media.Movie("Ice Age (2002)", "Set during the Ice Age, a sabertooth tiger, a sloth, and a wooly mammoth find a lost human infant, and they try to return him to his tribe.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg", "https://youtu.be/cMfeWyVBidk")

chak_de_india = media.Movie("Chak De India! (2007)", "The story of a hockey player who returns to the game as a coach of a women's hockey team.",
                            "http://www.suggestmemovie.com/fotolar/1340968445715474218.jpg", "https://youtu.be/6a0-dSMWm5g")

the_shawshank_redemption = media.Movie(
    "The Shawshank Redemption (1994)", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "http://www.suggestmemovie.com/fotolar/12963093141508567041.jpg", "https://youtu.be/K_tLp7T6U1c")

crouching_tiger_hidden_dragon = media.Movie("Crouching Tiger, Hidden Dragon (2000)",
                                            "Two warriors in pursuit of a stolen sword and a notorious fugitive are led to an impetuous, physically-skilled, teenage nobleman's daughter, who is at a crossroads in her life.", "http://www.suggestmemovie.com/fotolar/1315469934430905131.jpg", "https://youtu.be/gLpZ_5bHmo8")

enemy_at_the_gates = media.Movie("Enemy at the Gates (2001)",
                                 "Two Russian and German snipers play a game of cat-and-mouse during the Battle of Stalingrad.", "http://www.suggestmemovie.com/fotolar/1296323989194981211.jpg", "https://youtu.be/4O-sMh_DO6I")


march_of_the_penguins = media.Movie("March of the Penguins (2005)",
                                    "In the Antarctic, every March since the beginning of time, the quest begins to find the perfect mate and start a family.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM1NDc5MDYxMl5BMl5BanBnXkFtZTcwMjMzNDAzMQ@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg", "https://youtu.be/L7tWNwhSocE")

pink = media.Movie("Pink (2016)",
                   "When three young women are implicated in a crime, a retired lawyer steps forward to help them clear their names.", "http://www.suggestmemovie.com/fotolar4/14837116191793903737.jpg", "https://youtu.be/AL2TShb6fFs")


movies = [casualties_of_war, kiss_kiss_bang_bang, godfather, ice_age, chak_de_india,
          the_shawshank_redemption, crouching_tiger_hidden_dragon, enemy_at_the_gates, march_of_the_penguins, pink]

fresh_tomatoes.open_movies_page(movies)
