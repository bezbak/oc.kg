from django.contrib import admin
from apps.settings.models import Setting, Ads,About_us
# Register your models here.
admin.site.register(Setting)
admin.site.register(Ads)
admin.site.register(About_us)