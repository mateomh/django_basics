from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movie_list(req):
    if req.method == 'GET':
        movies = Movie.objects.all()
        serialized_movies = MovieSerializer(movies, many=True)
        return Response(serialized_movies.data, status=status.HTTP_200_OK)
    elif req.method == 'POST':
        serializer = MovieSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def movie_details(req, id):
    try:
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if req.method == 'GET':      
        serialized_movie = MovieSerializer(movie)
        return Response(serialized_movie.data, status=status.HTTP_200_OK)
    elif req.method == 'PUT' or req.method == 'PATCH':
        serializer = MovieSerializer(movie, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
