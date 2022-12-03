from django.shortcuts import render
from apps.movies.models import Movie
from apps.settings.models import Setting
# Create your views here.
def movie_detail(request, id):
    setting = Setting.objects.latest('id')
    movie = Movie.objects.get(id = id)
    context = {
        'setting': setting,
        'movie': movie
    }
    
    return render(request, 'main/details1.html', context)