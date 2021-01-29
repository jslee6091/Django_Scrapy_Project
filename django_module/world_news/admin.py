from django.contrib import admin
from world_news.models import WorldNews

class WorldNewsAdmin(admin.ModelAdmin):
    list_display=('title','writer','preview')

admin.site.register(WorldNews, WorldNewsAdmin)
