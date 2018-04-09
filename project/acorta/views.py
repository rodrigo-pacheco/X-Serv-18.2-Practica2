from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def barra(request):
    return(HttpResponse('Hola'))

def numero(request, num):
    return(HttpResponse('Adios'))

def notfound(request):
    return(HttpResponse('<h1>Usage error</h1><br>' + 
                        'Try (server)/ or (server)/number'))
