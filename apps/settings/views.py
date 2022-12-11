from django.shortcuts import render
from apps.settings.models import Setting, About_us, Ads
from apps.users.models import User
from apps.movies.models import Movie
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    movies = Movie.objects.all().filter(draft = False).order_by('year')
    reviews = {}
    for movie in movies:
        rev_count = 0
        rev_num = 0
        for rev in movie.review_movie.all():
            rev_count += 1
            rev_num += rev.number
        rev_mid = rev_num/ rev_count
        reviews.setdefault(movie.title, rev_mid)
            
    context = {
        'setting': setting,
        'movies': movies,
        'reviews':reviews
    }
    return  render(request, 'main/index.html', context)
