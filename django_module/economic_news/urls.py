from economic_news.views import SearchFormView, EconomicNewsView, RefreshFormView
from django.urls import path

app_name = 'economic_news'
urlpatterns = [
    path('', EconomicNewsView.as_view(), name='economicnews'),
    path('refresh/', RefreshFormView.as_view(), name='ecorefresh'),
    path('search/', SearchFormView.as_view(), name='ecosearch'),
]

    