from django.shortcuts import render
from django.http import HttpResponse

def mainhome(request):
    return HttpResponse('<h4>Hey its main page</h4>')