from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class indexView(TemplateView):
    template_name = 'home/index.html'

class pruebaListaView(ListView):
    template_name = 'home/list.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'listaPrueba'