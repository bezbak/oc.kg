from django.shortcuts import render
from apps.settings.models import Setting, About_us, Ads
from apps.users.models import User
from apps.movies.models import Movie
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    movies = Movie.objects.all().filter(draft = False).order_by('year')
    new_releases = Movie.objects.all().filter(draft = False).order_by('year')[:6]
    reviews = {}
    for movie in movies:
        rev_count = 0
        rev_num = 0
        for rev in movie.review_movie.all():
            rev_count += 1
            rev_num += rev.number
        try:
            rev_mid = rev_num/ rev_count
        except:
            rev_mid = 10
        reviews.setdefault(movie.title, str(rev_mid)[:4])
            
    context = {
        'setting': setting,
        'movies': movies,
        'reviews':reviews,
        'new_releases':new_releases
    }
    return  render(request, 'main/index.html', context)
