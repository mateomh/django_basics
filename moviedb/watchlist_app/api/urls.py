from django.urls import path, include
from watchlist_app.api.views import MovieListAV, MovieDetailsAV, ReviewListAV, ReviewDetailsAV, WatchListsAV, WatchListDetailsAV, StreamPlatformListAV, StreamPlatformDetailsAV

urlpatterns = [
    path('movie/', MovieListAV.as_view(), name='movie-list'),
    path('movie/<int:id>', MovieDetailsAV.as_view(), name='movie-detail'),

    path('watchlist/', WatchListsAV.as_view(), name='watchlist-list'),
    path('watchlist/<int:id>', WatchListDetailsAV.as_view(), name='watchlist-detail'),

    path('platform/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:id>', StreamPlatformDetailsAV.as_view(), name='platform-detail'),

    path('review/', ReviewListAV.as_view(), name='review-list'),
    path('review/<int:id>', ReviewDetailsAV.as_view(), name='review-detail'),

    path('movie/<int: id>/review', MovieDetailsAV.as_view(), 'movie-detail-reviews'),
]
