from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    url(r'^$',views.home, name="home"),
    url(r'imageprocess',views.imageprocess, name="imageprocess")
]
