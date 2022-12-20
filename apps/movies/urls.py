from django.urls import path
from apps.movies.views import movie_detail, movie_search

urlpatterns = [
    path('<int:id>/', movie_detail, name = 'movie_detail'),
    path('movie_search/', movie_search, name = 'movie_search')
]