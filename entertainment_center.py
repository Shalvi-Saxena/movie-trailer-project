"""Stores details of movies and displays them on a website."""
import media
import fresh_tomatoes

harry_potter = media.Movie("Harry Potter",
                           "A young boy with a great destiny proves his"
                           "worth while attending Hogwarts School of "
                           "Witchcraft and Wizardry.",
                           "Adventure, Family, Fanatsy", "7.5",
                           "http://cdn.playbuzz.com/cdn/c1e7b97f-42d8-"
                           "41a5-8e14-0d816e3c1"
                           "160/37202648-8c3d-45ce-abcc-c7affcb612a7.jpg",
                           "https://www.youtube.com/watch?v=PbdM1db3JbY")

iron_man = media.Movie("Iron Man",
                       "After being held captive in an Afghan cave, "
                       "billionaire engineer TonyStark creates a unique "
                       "weaponized suit of armor to fight evil.",
                       "Action, Adventure, Sci-Fi", "7.9",
                       "https://images-na.ssl-images-amazon.com/images/I/"
                       "51n3xGJw0TL._SX940_.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

narnia = media.Movie("The Chronocles of Narnia",
                     "Four kids travel through a wardrobe to the land of "
                     "Narnia and learn of their destiny to free it with "
                     "the guidance of a mystical lion.",
                     "Adventure, Family,Fanatsy", "6.9",
                     "http://coolspotters.com/files/photos/420967/the"
                     "-chronicles-of-narnia-the-lion-the-witch-and-"
                     "the-wardrobe-profile.jpg",
                     "https://www.youtube.com/watch?v=lWKj41HZBzM")

shutter_island = media.Movie("Shutter Island",
                             "In 1954, a U.S. marshal investigates the "
                             "disappearance of a murderess who escaped from "
                             "a hospital for the criminally insane.",
                             "Mystry, Thriller", "8.1",
                             "https://images-na.ssl-images-amazon.com/images/"
                             "M/MV5BMTMxMTIyNzMxMV5BMl5BanBnXkFtZTcwOTc4OTI3Mg"
                             "@@._V1_UY1200_CR83,0,630,1200_AL_.jpg",
                             "https://www.youtube.com/watch?v=5iaYLCiq5RM")

titanic = media.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love "
                      "with a kind but poor artist aboard the luxurious"
                      ", ill-fated R.M.S. Titanic.",
                      "Drama, Romance", "7.7",
                      "https://images-na.ssl-images-amazon.com/images/M/"
                      "MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNj"
                      "k3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR88,"
                      "0,630,1200_AL_.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

star_wars = media.Movie("Star Wars: Te Force Awakens",
                        "The First Order attempts to rule the galaxy "
                        "and only a ragtag group of heroes can stop them,"
                        " along with the help of the Resistance.",
                        "Action, Adventure, Fanatsy", "8.1",
                        "https://lh3.googleusercontent.com/Pf8ju5xbWNzccZfb"
                        "Un6TR1CX-np9RgEl0S-zvs8ZmENWCsgAyoCDMBQIDlLplf0ro6"
                        "UL=w300",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

movies = [harry_potter, iron_man, narnia, shutter_island, titanic, star_wars]
fresh_tomatoes.open_movies_page(movies)
