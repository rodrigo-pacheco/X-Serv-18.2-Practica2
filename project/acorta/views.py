from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def barra(request):
    HttpResponse('Hola')

def numero(request, num):
    HttpResponse('Adios')
