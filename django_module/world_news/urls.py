from django.urls import path
from world_news.views import WorldNewsView

app_name = 'world_news'

urlpatterns = [
    path('', WorldNewsView.as_view(), name='worldnews'),
]
