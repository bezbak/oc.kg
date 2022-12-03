from django.contrib import admin
from apps.movies.models import Actor, Movie, Reviews
# Register your models here.
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Reviews)