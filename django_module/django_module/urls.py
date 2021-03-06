"""django_module URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_module.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('itnews/', include('news.urls', namespace='itnews')),
    path('economicnews/', include('economic_news.urls', namespace='economicnews')),
    path('worldnews/', include('world_news.urls', namespace='worldnews')),
    path('', HomeView.as_view(), name='home'),
]
