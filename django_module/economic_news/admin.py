from django.contrib import admin
from economic_news.models import EconomicNews

class EconomicNewsAdmin(admin.ModelAdmin):
    list_display=('title','writer','preview')

admin.site.register(EconomicNews, EconomicNewsAdmin)
