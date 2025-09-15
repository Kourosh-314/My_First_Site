from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def runserver(request):
    return HttpResponse("hello there")