from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("it's first view, just http response")

def help(request):
    dictionary = {"help_request": "It's a help page, what you requested!!!!"}
    return render(request, 'AppTwo/help.html', context = dictionary)