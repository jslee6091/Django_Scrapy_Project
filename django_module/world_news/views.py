from django.shortcuts import render
from django.views.generic import ListView
from world_news.models import WorldNews

# Create your views here.
class WorldNewsView(ListView):
    model = WorldNews
    template_name = 'world_news/world_list.html'
    paginate_by = 10
