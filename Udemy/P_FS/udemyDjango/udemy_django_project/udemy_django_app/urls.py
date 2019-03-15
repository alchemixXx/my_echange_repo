from django.conf.urls import url
from udemy_django_app import views
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
]