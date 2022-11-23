from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from apps.users.models import User
from apps.settings.models import Setting
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
    context = {
        'setting':setting,
        'user': user
    }
    return render(request, 'main/profile.html', context)