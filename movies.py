from urllib2 import Request, urlopen, URLError
import json
import tomatoes


class Movie():
    """A datastructure for movies.
    Contails Movie title, box art url, youtube trailer url"""
    def __init__(self, title, poster_url, video_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = video_url


# An array of type Movie
movies = []


# We pass an ID of the TMDB and get Youtube Trailer ID.
def get_youtube_url(_id):
    # Please add your TMDB API Here
    request = Request("https://api.themoviedb.org/3/movie/" + str(_id) + "/videos?api_key=ee7fc288d8f352dbd247fd51129cb18d")
    try:
        response = urlopen(request)
        video_result = json.loads(response.read())
        url = video_result["results"][1]["key"]
        return url
    except URLError, e:
        print("No trailers sorry : ", e)


# Start of getting popular Movies
print("Getting Popular Movies, Please wait...")

# URL from where to get the popular movies.
# Please add your TMDB API Here
request = Request("https://api.themoviedb.org/3/movie/popular?api_key=ee7fc288d8f352dbd247fd51129cb18d")
try:
    response = urlopen(request)
    # convert JSON to a dictionary for python use
    movie_result = json.loads(response.read())
    print("Total movies found: " + str(len(movie_result["results"])))
    for movie in movie_result["results"]:
        print(movie["title"])
        # Create an instance of the
        # Movie class by passing the parameters given in the constructor
        mov = Movie(movie["title"], "http://image.tmdb.org/t/p/w185/" + movie["poster_path"], get_youtube_url(movie["id"]))
        movies.append(mov)

except URLError, e:
    print 'No moviez. Got an error code:', e

tomatoes.open_movies_page(movies)
