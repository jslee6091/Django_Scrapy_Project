from django.contrib import admin
from news.models import ItNews

class ItNewsAdmin(admin.ModelAdmin):
    list_display=('title','writer','preview')

admin.site.register(ItNews, ItNewsAdmin)
