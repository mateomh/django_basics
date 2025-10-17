from django.urls import path, include
from watchlist_app.api.views import MovieListAV, MovieDetailsAV, WatchListsAV, WatchListDetailsAV, StreamPlatformListAV, StreamPlatformDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:id>', MovieDetailsAV.as_view(), name='movie-detail'),

    path('watchlist/', WatchListsAV.as_view(), name='watchlist-list'),
    path('watchlist/<int:id>', WatchListDetailsAV.as_view(), name='watchlist-detail'),

    path('platform/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:id>', StreamPlatformDetailsAV.as_view(), name='platform-detail'),
]
