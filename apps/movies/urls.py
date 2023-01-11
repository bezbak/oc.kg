from django.urls import path
from apps.movies.views import movie_detail, movie_search, movie_catalog

urlpatterns = [
    path('<int:id>/', movie_detail, name = 'movie_detail'),
    path('movie_search/', movie_search, name = 'movie_search'),
    path('movie_catalog/<slug:slug>/', movie_catalog, name='movie_catalog')
]