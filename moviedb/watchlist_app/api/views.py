from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

class MovieListAV(APIView):
    """
    View to list all the movies in the database
    """

    def get(self, req):
        movies = Movie.objects.all()
        serialized_movies = MovieSerializer(movies, many=True)
        return Response(serialized_movies.data, status=status.HTTP_200_OK)
    
    def post(self, req):
        serializer = MovieSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class MovieDetailsAV(APIView):
    """
    """

    def get(self, req, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
             
        serialized_movie = MovieSerializer(movie)
        return Response(serialized_movie.data, status=status.HTTP_200_OK)
    
    def put(self, req, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
