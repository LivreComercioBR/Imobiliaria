from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("Esta é a sua homepage")