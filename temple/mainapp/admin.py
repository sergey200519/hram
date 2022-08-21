from django.contrib import admin

# Register your models here.
from mainapp.models import News, ImgNews, Timetable, Settings

admin.site.register(News)
admin.site.register(ImgNews)
admin.site.register(Timetable)
admin.site.register(Settings)
