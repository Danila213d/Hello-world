from django.shortcuts import render
from django.http import HttpResponse

def HomePageView(request):
    return HttpResponse('Имран лох')
