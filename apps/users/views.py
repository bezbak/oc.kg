from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from apps.users.models import User
from apps.settings.models import Setting
from apps.movies.models import Movie
from django.db.models import Sum, Count
# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, email = email)  
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            auth_login(request, user)
            return redirect('index')
    context = {
        'setting': setting
    }
    return render(request, 'main/register.html', context)

def login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        auth_login(request, user)
        return redirect('index')
    context = {
            'setting': setting
    }
    return render(request, 'main/login.html', context)

def profile(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id =id)
    recomandations=Movie.objects.all().order_by('?')[:6]
    reviews={}
    for movie2 in recomandations:
        test = movie2.review_movie.aggregate(
            numbers = Sum('number'),
            len = Count('id')
        )
        try:
            rev_mid= test['numbers']/ test['len']
        except:
            rev_mid=10
        reviews.setdefault(movie2.title, str(rev_mid)[:4])
        movie2.rating = rev_mid
        movie2.save()
    context = {
        'setting':setting,
        'user': user,
        'recomandations':recomandations,
    }
    return render(request, 'main/profile.html', context)