from economic_news.views import DataSearchFormView, EconomicNewsView, DataFormView
from django.urls import path

app_name = 'economic_news'
urlpatterns = [
    path('', EconomicNewsView.as_view(), name='economicnews'),
    path('refresh/', DataFormView.as_view(), name='ecorefresh'),
    path('refresh/search/', DataSearchFormView.as_view(), name='ecosearch'),
]

    