from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import Movie, Review, WatchList, StreamPlatform
from watchlist_app.api.serializers import MovieSerializer, ReviewSerializer,  WatchListSerializer, StreamPlatformSerializer

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


class WatchListsAV(APIView):
    """
    View to list all the watchlists in the database
    """

    def get(self, req):
        watchlists = WatchList.objects.all()
        serialized_data = WatchListSerializer(watchlists, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, req):
        serializer = WatchListSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class WatchListDetailsAV(APIView):
    """
    """

    def get(self, req, id):
        try:
            watchlist = WatchList.objects.get(pk=id)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
             
        serialized_data = WatchListSerializer(watchlist)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def put(self, req, id):
        try:
            watchlist = WatchList.objects.get(pk=id)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(watchlist, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, id):
        try:
            watchlist = WatchList.objects.get(pk=id)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamPlatformListAV(APIView):
    """
    View to list all the stream platforms in the database
    """

    def get(self, req):
        platforms = StreamPlatform.objects.all()
        serialized_data = StreamPlatformSerializer(platforms, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, req):
        serializer = StreamPlatformSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StreamPlatformDetailsAV(APIView):
    """
    """

    def get(self, req, id):
        try:
            platform = StreamPlatform.objects.get(pk=id)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
             
        serialized_data = StreamPlatformSerializer(platform)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def put(self, req, id):
        try:
            platform = StreamPlatform.objects.get(pk=id)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, id):
        try:
            platform = StreamPlatform.objects.get(pk=id)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  

# # Class View with Mixins
# class ReviewListAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, req, *args, **kwargs):
#         return self.list(req, *args, **kwargs)
    
#     def post(self, req, *args, **kwargs):
#         return self.create(req, *args, **kwargs)
    

# # Class View with Mixins
# class ReviewDetailsAV(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, req, *args, **kwargs):
#         return self.retrieve(req, *args, **kwargs)
    

# Concrete view classes
class ReviewListAV(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Review.objects.filter(movie=id)


class ReviewDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        id = self.kwargs['id']
        movie = Movie.objects.get(pk=id)
        return serializer.save(movie=movie)
