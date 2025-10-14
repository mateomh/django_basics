from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view()
def movie_list(req):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(movies, many=True)

    return Response(serialized_movies.data)

@api_view()
def movie_details(req, id):
    movie = Movie.objects.get(pk=id)
    serialized_movie = MovieSerializer(movie)

    return Response(serialized_movie.data)