from django.shortcuts import render
from apps.settings.models import Setting, About_us, Ads
from apps.users.models import User
from apps.movies.models import Movie
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    movies = Movie.objects.all().filter(draft = False).order_by('year')
    context = {
        'setting': setting,
        'movies': movies
    }
    return  render(request, 'main/index.html', context)
