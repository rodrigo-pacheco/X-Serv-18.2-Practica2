from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import URL

# Create your views here.

def barra(request):
    return(HttpResponse('Hola'))

def numero(request, num):
    redirect_url = URL.objects.get(id=str(num))
    return(HttpResponseRedirect(redirect_url))

def notfound(request):
    return(HttpResponse('<h1>Usage error</h1><br>' +
                        'Try (server)/ or (server)/number'))
