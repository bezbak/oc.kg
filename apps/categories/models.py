from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=30)
    slug = models.SlugField('Понятный для',max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=30)
    slug = models.SlugField('Понятный для',max_length=255, unique=True  )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'