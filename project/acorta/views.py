from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from .models import URL

USAGE_ERROR = """<h1>Usage error</h1><br>
              Try (server)/ [GET/POST] or
              (server)/number [GET] or
              (server)/admin/ [GET]"""

# Create your views here.
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
            new_url = URL(url=request.POST["URL"])
            new_url.save()
        except:
            print("EXCEEEEEEEEEEEEEPT")
        body = ("<html><body><h1>Shortened URL: </h1>" +
               "<p><a href=/" + str(new_url.id) + ">" + str(new_url.id) + "</a>"
               " > " + "<a href=" + new_url.url + ">" + new_url.url + "</a></p>"
               "<p><a href=/>Back to start page</a></p>" +
               "</body></html>")
        return(HttpResponse(body))
    else:
        return(HttpResponseNotFound(USAGE_ERROR))

def numero(request, num):
    redirect_url = URL.objects.get(id=str(num))
    return(HttpResponseRedirect(redirect_url))

def notfound(request):
    return(HttpResponseNotFound(USAGE_ERROR))
