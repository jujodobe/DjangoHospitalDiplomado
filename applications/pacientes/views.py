from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Pacientes
from .serializer import PacientesSerializer

# Create your views here.
class PacientesListView(ListView):
    model = Pacientes
    template_name = "pacientes/listPacientes.html"

class PacientesListApiView(ListAPIView):
   serializer_class = PacientesSerializer

   def get_queryset(self):
       return Pacientes.objects.all()

class PacientesRegisterApiView(CreateAPIView):
    serializer_class = PacientesSerializer




