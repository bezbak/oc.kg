from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from apps.users.models import User
from apps.settings.models import Setting
from apps.movies.models import Movie
from django.db.models import Sum, Count
from django.http import HttpResponse
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
    return render(request, 'main/users/register.html', context)

def login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            auth_login(request, user)
            return redirect('index')
        except:
            return redirect('wrong_username_pass')
    context = {
            'setting': setting
    }
    return render(request, 'main/users/login.html', context)

def profile(request, id):
    user = User.objects.get(id =id)
    if request.user != user:
        return redirect('index')
    setting = Setting.objects.latest('id')
    recomandations=Movie.objects.all().order_by('?')[:6]
    if request.method =='POST':
        if 'profile_update' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            profile_image = request.FILES.get('image')
            print(profile_image)
            try:
                user.username = username
                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.profile_image = profile_image
                user.save()
                return redirect('profile', user.id)
            except:
                redirect.redirect('update_error')
        if 'update_password' in request.POST:
            old_password=request.POST.get('oldpass')
            new_password=request.POST.get('newpass')
            confirm_password=request.POST.get('confirmpass')
            if new_password == confirm_password:
                try:
                    user = User.objects.get(username = user.username)
                    if user.check_password(old_password):
                        user.set_password(new_password)
                        user.save()
                        return redirect('account', user.id)
                    else:
                        return HttpResponse('Неправильный пароль')
                except:
                    return HttpResponse('Пользователь не найден')
            else:
                return HttpResponse('Пароли отличаются')     
    context = {
        'setting':setting,
        'user': user,
        'recomandations':recomandations,
    }
    return render(request, 'main/users/profile.html', context)