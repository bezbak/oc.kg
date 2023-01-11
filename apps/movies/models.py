from django.db import models
from apps.categories.models import Category, Genre
from datetime import date
from apps.users.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.
class Actor(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=70)
    description = models.TextField(verbose_name='Описание', max_length= 500)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    image = models.ImageField("Image", upload_to = "actors/")

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Актёр и режисёр"
        verbose_name_plural = "Актёры и режисёры"
        
class Movie(models.Model):
    title = models.CharField('Название фильма', max_length=255)
    description = models.TextField('Описание фильма', max_length=500)
    poster = models.ImageField('Постер фильма', upload_to='movie_poster/')
    movie_trailer = models.FileField('Трейлер фильма', upload_to='movie_trailer/',validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    movie_file = models.FileField('Файл фильма', upload_to='movie_file/',validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    year = models.DateField("Дата выпуска", default=date.today)
    running_time = models.CharField('Длительность фильма', max_length=10)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Режисёр", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актёр", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанр")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    draft = models.BooleanField("Черновик", default=False)
    rating = models.FloatField(default=10)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Reviews(models.Model):
    title = models.CharField(max_length=50, default='da')
    text = models.CharField( max_length=450, default='da')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_movie')
    number = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.movie.title}: {self.number}'
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Comments(models.Model):
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    parent = models.ForeignKey(
        'self', verbose_name="parent", related_name='sons', on_delete=models.SET_NULL, blank=True,null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="movie",related_name='comment_movie', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

class CommentLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='likes')
    
class CommentDisLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='dis_likes')
    
class Gallery(models.Model):
    file = models.FileField( upload_to='gallery/', max_length=100)
    movie = models.ForeignKey(Movie, related_name='gallery', on_delete=models.CASCADE)