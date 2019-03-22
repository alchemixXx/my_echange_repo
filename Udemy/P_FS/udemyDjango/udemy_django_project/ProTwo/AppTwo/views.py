from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users

# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    dictionary = {"help_request": "It's a help page, what you requested!!!!"}
    return render(request, 'AppTwo/help.html', context = dictionary)


def users(request):
    # users_dict = Users.objects.order_by('email')
    users_dict = "Hello world! It's working!"
    output = {'users_request': users_dict}
    return render(request, 'AppTwo/index.html', context=output)



#
# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records': webpages_list}
#     return render(request, 'udemy_django_app/index.html', context = date_dict)
