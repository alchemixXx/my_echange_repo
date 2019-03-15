from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': "Now I'm form udemy_django_app"}
    return render(request, 'udemy_django_app/index.html', context = my_dict)
