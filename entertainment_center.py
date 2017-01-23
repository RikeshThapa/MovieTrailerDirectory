import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

americanPsycho = media.Movie("American Psycho",
                            "Patric Bateman 2 years old who believes in taking care of himself",
                            "https://upload.wikimedia.org/wikipedia/en/6/63/Americanpsychoposter.jpg",
                            "https://www.youtube.com/watch?v=RjKNbfA64EE")

'''
Tester Code:
print(toy_story.storyline)
avatar.show_trailer()
'''

movies = [toy_story, avatar, americanPsycho]
fresh_tomatoes.open_movies_page(movies)
