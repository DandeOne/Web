from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(can_be_whatever_but_usually_named_request):
    return HttpResponse("<em>Hello World, I'm a hello app</em>")
