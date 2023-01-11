from django.shortcuts import render
from apps.settings.models import Setting, About_us, Ads
from apps.users.models import User
from apps.movies.models import Movie
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    movies = Movie.objects.all().filter(draft = False).order_by('year')
    new_releases = Movie.objects.all().filter(draft = False).order_by('year')[:6]
    context = {
        'setting': setting,
        'movies': movies,
        'new_releases':new_releases
    }
    return  render(request, 'main/index.html', context)
