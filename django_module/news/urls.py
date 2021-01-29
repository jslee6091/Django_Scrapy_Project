from django.contrib import admin
from django.urls import path, include
from news.views import ItDataSearchFormView, ItNewsView

app_name = 'news'

urlpatterns = [
    path('', ItNewsView.as_view(), name='itnewslist'),
    path('refresh/search', ItDataSearchFormView.as_view(), name='itsearch'),
]
