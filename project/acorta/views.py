from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import URL

USAGE_ERROR = """<h1>Usage error</h1><br>
              Try (server)/ [GET/POST] or
              (server)/number [GET]"""

# Create your views here.
def current_url_links():
    html_code = "<p><h2>Shortened URLS:</h2></p>"
    url_list = URL.objects.all()
    for url in url_list:
        html_code += ("<p><a href=" + url.url + ">" + str(url.id) + "</a> " +
                      "-- " + "<a href=" + url.url + ">" + url.url + "</a></p>")
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
        return(HttpResponse('POST'))
    else:
        return(HttpResponse(USAGE_ERROR))

def numero(request, num):
    redirect_url = URL.objects.get(id=str(num))
    return(HttpResponseRedirect(redirect_url))

def notfound(request):
    return(HttpResponse(USAGE_ERROR))
