from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import URL

# Create your views here.

def barra(request):
    if request.method == 'GET':
        "<html><body><h1>" +
                """<form method=post accept-charset="utf-8">URL:<br>
                <input type="text" name="URL" value="www.realmadrid.com"><br>
                <input type="submit" value="Submit"></form>""" +
                current_url_links() +
                "</body></html>"
    return(HttpResponse('Hola'))

def numero(request, num):
    redirect_url = URL.objects.get(id=str(num))
    return(HttpResponseRedirect(redirect_url))

def notfound(request):
    return(HttpResponse('<h1>Usage error</h1><br>' +
                        'Try (server)/ or (server)/number'))
