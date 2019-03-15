from django.conf.urls import url
from AppTwo import views
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^$', views.help, name="help"),
]