from django.urls import path
from apps.settings.views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('update_error/', update_error, name = 'update_error'),
    path('wrong_username_pass/', wrong_username_pass, name = 'wrong_username_pass'),
]