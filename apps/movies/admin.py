from django.contrib import admin
from apps.movies.models import Actor, Movie, Reviews, Comments, CommentDisLikes, CommentLikes, Gallery
# Register your models here.
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Reviews)
admin.site.register(Comments)
admin.site.register(CommentDisLikes)
admin.site.register(CommentLikes)
admin.site.register(Gallery)