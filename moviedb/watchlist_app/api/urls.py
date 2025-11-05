from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (MovieListAV, 
                                     MovieDetailsAV, 
                                     ReviewListAV, 
                                     ReviewCreate, 
                                     ReviewDetailsAV, 
                                     WatchListsAV, 
                                     WatchListDetailsAV, 
                                     StreamPlatformListAV, 
                                     StreamPlatformDetailsAV,
                                     StreamPlatformVS)

router = DefaultRouter()
router.register('platform', StreamPlatformVS, basename='stream-platform')

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:id>/', MovieDetailsAV.as_view(), name='movie-detail'),

    path('watchlist/', WatchListsAV.as_view(), name='watchlist-list'),
    path('watchlist/<int:id>', WatchListDetailsAV.as_view(), name='watchlist-detail'),

    path('', include(router.urls)),

    path('platform/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:id>', StreamPlatformDetailsAV.as_view(), name='platform-detail'),

    # path('review/', ReviewListAV.as_view(), name='review-list'),
    # path('review/<int:id>', ReviewDetailsAV.as_view(), name='review-detail'),

    path('<int:id>/review-create', ReviewCreate.as_view(), name='movie-review-create'),
    path('<int:id>/reviews', ReviewListAV.as_view(), name='movie-detail-reviews'),
    path('review/<int:pk>/', ReviewDetailsAV.as_view(), name='movie-review-detail'),
]
