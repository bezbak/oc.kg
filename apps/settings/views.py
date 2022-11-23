from django.shortcuts import render
from apps.settings.models import Setting, About_us, Ads
from apps.users.models import User
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting': setting
    }
    return  render(request, 'main/index.html', context)
