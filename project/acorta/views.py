#!/usr/bin/python3
"""
Simple HTTP Server: shortenrs URLs
Implemented with Django

Rodrigo Pacheco Martinez-Atienza
r.pachecom @ alumnos.urjc.es
SAT subject (Universidad Rey Juan Carlos)
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

from .models import URL

USAGE_ERROR = """<h1>Usage error</h1><br>
              Try (server)/ [GET/POST] or
              (server)/number [GET] or
              (server)/admin/ [GET]
              <p><a href=/>Back to home page</a></p>"""

LINK = """<a href=/{}>{}</a>"""

# Create your views here.
def correct_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return(url)
    else:
        return("http://" + url)


def current_url_links():
    html_code = "<p><h2>Shortened URLS:</h2></p>"
    url_list = URL.objects.all()
    for url in url_list:
        html_code += ("<p><a href=/" + str(url.id) + ">" + str(url.id) + "</a>"
                      " > " + "<a href=" + url.url + ">" + url.url + "</a></p>")
    return(html_code)

@csrf_exempt
def barra(request):
    if request.method == 'GET':
        return(HttpResponse("<html><body><h1>" +
                """<form method=post accept-charset="utf-8">URL:<br>
                <input type="text" name="URL" value="www.realmadrid.com"><br>
                <input type="submit" value="Submit"></form>""" +
                current_url_links() +
                "</body></html>"))
    elif request.method == 'POST':
        try:
            new_url = URL(url=correct_url(request.POST["URL"]))
            new_url.save()
        except IntegrityError:
            body = ("<html><body><h1>URL already added</h1>"
                    "<p><a href=/>Back to home page</a></p>")
            return(HttpResponse(body))
        body = ("<html><body><h1>Shortened URL: </h1>" +
               # "<p>"" + LINK{str(new_url.id), str(new_url.id)} +
               "<p><a href=/" + str(new_url.id) + ">" + str(new_url.id) + "</a>"
               " > " + "<a href=" + new_url.url + ">" + new_url.url + "</a></p>"
               "<p><a href=/>Back to home page</a></p>" +
               "</body></html>")
        return(HttpResponse(body))
    else:
        return(HttpResponseNotFound(USAGE_ERROR))

def numero(request, num):
    try:
        redirect_url = URL.objects.get(id=str(num))
        return(HttpResponseRedirect(redirect_url))
    except URL.DoesNotExist:
        return(HttpResponseNotFound("<html><body><h1>Number not in use</h1>"
                                    "<p><a href=/>Back to home page</a></p>"))

def notfound(request):
    return(HttpResponseNotFound(USAGE_ERROR))
