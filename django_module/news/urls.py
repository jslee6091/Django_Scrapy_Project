from django.urls import path
from news.views import ItSearchFormView, ItNewsView, ItRefreshFormView

app_name = 'news'

urlpatterns = [
    path('', ItNewsView.as_view(), name='itnewslist'),
    path('refresh/', ItRefreshFormView.as_view(), name='itrefresh'),
    path('search/', ItSearchFormView.as_view(), name='itsearch'),
]
