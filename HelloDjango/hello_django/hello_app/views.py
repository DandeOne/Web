from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(can_be_whatever_but_usually_named_request):
    return HttpResponse("<em>Hello World, I'm a hello app</em>")


def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'hello_app/help.html', context=helpdict)

def inner(request):
    return render(request, 'hello_app/inner.html', context={'text_variable': 'This is another site of hello_app'})

