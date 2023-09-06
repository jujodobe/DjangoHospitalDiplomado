from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def saludo(request):
    HttpResponse("Hola mundo")

urlpatterns = [
    path('saludar/', saludo),
]