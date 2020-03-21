from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dictionary = {'insert_me': "hello i am from views.py"}
    return render(request, 'appTwo/index.html', context=my_dictionary)


def help(request):
    my_dictionary = {'help_me': "Click here for help!"}
    return render(request, 'appTwo/help.html', context=my_dictionary)





