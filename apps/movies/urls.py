from django.urls import path
from apps.movies.views import movie_detail

urlpatterns = [
    path('<int:id>/', movie_detail, name = 'movie_detail')
]