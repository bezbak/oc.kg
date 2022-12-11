from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    logo = models.FileField(upload_to='logo/')
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    facebook = models.URLField(verbose_name="Facebook", max_length=50, blank = True, null = True)
    instagram = models.URLField(verbose_name=("instagram"), max_length=50, blank = True, null = True)
    twitter = models.URLField(verbose_name=("twitter"), max_length=50, blank = True, null = True)
    vk = models.URLField(verbose_name=("vk"), max_length=50, blank = True, null = True)
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        
class Ads(models.Model):
    name = models.CharField(verbose_name=("Название рекламы"), max_length=50)
    image = models.ImageField(verbose_name=("Фото рекламы"), upload_to='ads_image/', height_field=None, width_field=None, max_length=None)
    link = models.URLField(verbose_name=("Ссылка рекламы"), max_length=200)

    class Meta:
        verbose_name = ("Реклама")
        verbose_name_plural = ("Рекламы")

    def __str__(self):
        return self.name

class About_us(models.Model):
    description = models.TextField(verbose_name=("О нас текст"), max_length=500)
    

    class Meta:
        verbose_name = ("О нас")
        verbose_name_plural = ("О нас")

    def __str__(self):
        return self.description
    


