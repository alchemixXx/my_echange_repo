from django.conf.urls import url
from AppTwo import views
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path('^help/', views.help, name='help'),
    re_path('users/', views.users, name='users'),
]