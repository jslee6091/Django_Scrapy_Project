from django.urls import path
from world_news.views import WorldNewsView, WorldSearchFormView, WorldRefreshFormView

app_name = 'world_news'

urlpatterns = [
    path('', WorldNewsView.as_view(), name='worldnews'),
    path('refresh/', WorldRefreshFormView.as_view(), name='worldrefresh'),
    path('search/', WorldSearchFormView.as_view(), name='worldsearch'),
]
